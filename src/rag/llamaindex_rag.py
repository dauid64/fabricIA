from typing import List
import chromadb

from llama_index.llms.openai import OpenAI
from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex
from llama_index.core.query_engine import BaseQueryEngine
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, load_index_from_storage
from llama_index.core.node_parser import SentenceWindowNodeParser
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.schema import Document
from llama_index.core.postprocessor import MetadataReplacementPostProcessor
from llama_index.postprocessor.cohere_rerank import CohereRerank


class LlamaindexRAG:
    def __init__(self, documents: List[Document]) -> None:
        # self.file_extractor: dict[str, BaseReader] = {".pdf": PDFReader()}
        # self.db = chromadb.PersistentClient(path="data/chromadb/")
        # self.chroma_collection = self.db.get_or_create_collection(
        #     name="laudos"
        # )

        self.sentence_node_parser = SentenceWindowNodeParser.from_defaults(
            window_size=5,
            window_metadata_key="window",
            original_text_metadata_key="original_text"
        )
        self.documents = documents
        self.llm = OpenAI(model="gpt-5-mini-2025-08-07", temperature=0.1)
        self.embed_model = OpenAIEmbedding(embed_batch_size=50)
        self.query_engine = None

    @staticmethod
    def load_from_uploaded_file(uploaded_file) -> List:
        """
        Carrega um arquivo enviado (ex.: Streamlit `UploadedFile`) e cria
        uma lista de `Document` compatível com LlamaIndex.

        Aceita PDFs (usa PyPDF2) e arquivos de texto simples.
        """
        from io import BytesIO
        try:
            import PyPDF2
        except Exception:
            raise ImportError(
                "PyPDF2 é necessário para ler PDFs. Instale com pip install PyPDF2")

        # lê bytes do arquivo enviado
        file_bytes = uploaded_file.read()
        filename = getattr(uploaded_file, "name", "uploaded")

        # extrai texto dependendo da extensão
        text = ""
        if filename.lower().endswith(".pdf"):
            pdf_reader = PyPDF2.PdfReader(BytesIO(file_bytes))
            parts = []
            for page in pdf_reader.pages:
                parts.append(page.extract_text() or "")
            text = "\n".join(parts)
        else:
            # tenta decodificar como UTF-8, cai para latin-1 se necessário
            try:
                text = file_bytes.decode("utf-8")
            except Exception:
                text = file_bytes.decode("latin-1", errors="ignore")

        # importa Document de acordo com a versão do llama_index
        try:
            from llama_index.core.schema import Document
        except Exception:
            try:
                from llama_index.core import Document
            except Exception:
                raise ImportError(
                    "Não foi possível importar Document de llama_index")

        doc = Document(text=text, extra_info={"source": filename})
        documents = [doc]
        return documents

    def create_query_engine(self) -> BaseQueryEngine:
        if self.query_engine is not None:
            return self.query_engine

        nodes = self.sentence_node_parser.get_nodes_from_documents(
            self.documents)

        sentence_index = VectorStoreIndex(
            nodes,
            llm=self.llm,
            embed_model=self.embed_model,
            node_parser=self.sentence_node_parser
        )

        # Removido: persist e load_index_from_storage

        cohere_rerank = CohereRerank(top_n=5)

        self.query_engine = sentence_index.as_query_engine(
            similarity_top_k=15,
            verbose=True,
            node_postprocessors=[
                MetadataReplacementPostProcessor(target_metadata_key="window"),
                cohere_rerank
            ],
        )

        return self.query_engine
