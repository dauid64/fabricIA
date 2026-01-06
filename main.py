"""Script principal para processamento de documentos via CLI."""
import logging
import sys

from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI

from src.rag.llamaindex_rag import LlamaindexRAG
from src.parsers.llama_parser import LlammaParser

load_dotenv()
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

PERGUNTAS = [
    "Qual a empresa que está sendo avaliada no laudo? Retorno somente o nome da empresa.",
    "Qual a empresa que está realizando a avaliação no laudo? Retorno somente o nome da empresa.",
    "Qual a data do laudo? Retorno somente a data do laudo.",
]

if __name__ == "__main__":
    llama_parser = LlammaParser()
    llama_rag = LlamaindexRAG(input_file="data/raw/")

    query_engine = llama_rag.create_query_engine()

    for question in PERGUNTAS:
        sentence_response = query_engine.query(
            question
        )
        print(sentence_response)
