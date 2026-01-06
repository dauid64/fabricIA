"""
Serviço de processamento de PDF
Este é o módulo onde você deve adicionar seu algoritmo de processamento
"""

import pandas as pd
from io import BytesIO
from typing import Optional
import PyPDF2
from streamlit.runtime.uploaded_file_manager import UploadedFile

from src.rag.llamaindex_rag import LlamaindexRAG


class PDFProcessor:
    """
    Classe responsável por processar arquivos PDF e convertê-los em Excel
    """
    PERGUNTAS = {
        "nome": "Qual a empresa que está sendo avaliada no laudo? Retorno somente o nome da empresa.",
        "avaliadora": "Qual a empresa que está realizando a avaliação no laudo? Retorno somente o nome da empresa.",
        "data": "Qual a data do laudo? Retorno somente a data do laudo.",
        "metodologia": "Quais as metodologias de avaliação escolhidas pela empresa avaliadora neste laudo? Retorne somente o nome ou sigla das metodologias conforme o texto separadas por vírgula caso tenha mais de uma."
    }

    def __init__(self):
        self.pdf_content = None
        self.processed_data = None

    def process_pdf(self, pdf_file: UploadedFile) -> Optional[BytesIO]:
        """
        Processa o arquivo PDF e retorna um arquivo Excel

        Args:
            pdf_file: Arquivo PDF enviado pelo usuário

        Returns:
            BytesIO: Arquivo Excel processado
        """
        try:
            # Exemplo básico: extrai texto do PDF
            documents = LlamaindexRAG.load_from_uploaded_file(pdf_file)
            rag = LlamaindexRAG(documents)
            query_engine = rag.create_query_engine()

            # Converte os dados em DataFrame
            dataframe = {}
            for titulo, pergunta in self.PERGUNTAS.items():
                resposta = query_engine.query(
                    pergunta
                )
                dataframe[titulo] = resposta

            df = pd.DataFrame([dataframe])

            # Cria o arquivo Excel em memória
            excel_buffer = BytesIO()
            with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
                df.to_excel(writer, index=False,
                            sheet_name='Dados Processados')

            excel_buffer.seek(0)
            return excel_buffer

        except Exception as e:
            raise Exception(f"Erro ao processar PDF: {str(e)}")

    def extract_text_from_pdf(self, pdf_file) -> str:
        """
        Método auxiliar para extrair texto do PDF

        Args:
            pdf_file: Arquivo PDF

        Returns:
            str: Texto extraído
        """
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

    def validate_pdf(self, pdf_file) -> bool:
        """
        Valida se o arquivo é um PDF válido

        Args:
            pdf_file: Arquivo a ser validado

        Returns:
            bool: True se válido, False caso contrário
        """
        try:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            _ = len(pdf_reader.pages)
            return True
        except:
            return False


# ============================================
# FUNÇÕES AUXILIARES
# ============================================

def create_sample_excel(filename: str = "sample.xlsx") -> BytesIO:
    """
    Cria um arquivo Excel de exemplo

    Args:
        filename: Nome do arquivo

    Returns:
        BytesIO: Arquivo Excel de exemplo
    """
    data = {
        'Coluna 1': [1, 2, 3, 4, 5],
        'Coluna 2': ['A', 'B', 'C', 'D', 'E'],
        'Coluna 3': [10.5, 20.3, 30.1, 40.8, 50.2]
    }

    df = pd.DataFrame(data)
    excel_buffer = BytesIO()

    with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Exemplo')

    excel_buffer.seek(0)
    return excel_buffer
