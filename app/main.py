"""
Aplicação Principal - Processador de PDF para Excel
"""

import logging
import sys
from .utils.styles import apply_custom_styles
from .components import (
    render_header,
    render_welcome_message,
    render_file_uploader,
    render_download_button,
    render_sidebar_info,
    render_error_message,
    render_footer
)
from .services.pdf_processor import PDFProcessor
from . import config
import streamlit as st
from datetime import datetime
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler(stream=sys.stdout)
    ]
)
# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# Importações dos módulos da aplicação (importações relativas)


def initialize_session_state():
    """
    Inicializa as variáveis de estado da sessão
    """
    if 'current_file' not in st.session_state:
        st.session_state.current_file = None
    if 'excel_output' not in st.session_state:
        st.session_state.excel_output = None
    if 'processing' not in st.session_state:
        st.session_state.processing = False


def configure_page():
    """
    Configura a página do Streamlit
    """
    st.set_page_config(**config.PAGE_CONFIG)
    apply_custom_styles()


def main():
    """
    Função principal da aplicação
    """
    # Configuração inicial
    configure_page()
    initialize_session_state()

    # Renderiza a sidebar
    render_sidebar_info()

    # Renderiza o header
    render_header()

    # Mensagem de boas-vindas
    render_welcome_message()

    # Área de upload
    uploaded_file = render_file_uploader()

    # Processa o arquivo se foi enviado
    if uploaded_file is not None:
        st.markdown("---")

        # Verifica se já foi processado
        if st.session_state.excel_output is not None:
            # Mostra botão de download
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"resultado_{timestamp}.xlsx"

            render_download_button(st.session_state.excel_output, filename)

            # Mostra informações adicionais
            with st.expander("📊 Informações do processamento"):
                st.write(f"**Arquivo original:** {uploaded_file.name}")
                st.write(
                    f"**Processado em:** {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}")

            # Botão para processar outro arquivo
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("🔄 Processar Novo Arquivo", use_container_width=True, type="secondary"):
                    st.session_state.excel_output = None
                    st.rerun()
        else:
            # Botão para processar
            col1, col2, col3 = st.columns([1, 2, 1])

            with col2:
                process_button = st.button(
                    "🚀 Processar Arquivo",
                    use_container_width=True,
                    type="primary",
                    disabled=st.session_state.get('processing', False)
                )

            if process_button:
                # Marca como processando e faz rerun para atualizar o botão
                st.session_state.processing = True
                st.rerun()

            # Se está processando, executa o processamento
            if st.session_state.get('processing', False):
                try:
                    # Mostra progresso
                    progress_bar = st.progress(0)
                    status_text = st.empty()

                    # Inicializa o processador
                    status_text.text("⚙️ Inicializando processador...")
                    progress_bar.progress(25)
                    processor = PDFProcessor()

                    # Valida o PDF
                    status_text.text("🔍 Validando arquivo PDF...")
                    progress_bar.progress(50)

                    if not processor.validate_pdf(uploaded_file):
                        st.error("❌ Arquivo PDF inválido ou corrompido!")
                        st.session_state.processing = False
                        st.stop()

                    # Volta ao início do arquivo após validação
                    uploaded_file.seek(0)

                    # Processa o arquivo
                    status_text.text("🔄 Processando arquivo...")
                    progress_bar.progress(75)

                    excel_output = processor.process_pdf(uploaded_file)

                    # Completa o progresso
                    status_text.text("✅ Processamento concluído!")
                    progress_bar.progress(100)

                    # Armazena o resultado
                    st.session_state.excel_output = excel_output
                    st.session_state.processing = False

                    # Limpa a barra de progresso após um momento
                    import time
                    time.sleep(1)
                    progress_bar.empty()
                    status_text.empty()

                    # Recarrega a página para mostrar o resultado
                    st.rerun()

                except Exception as e:
                    st.session_state.processing = False
                    render_error_message(str(e))
                    st.info(
                        "💡 **Dica:** Verifique se o arquivo PDF não está corrompido ou protegido por senha.")

    else:
        # Instruções quando nenhum arquivo foi enviado
        st.markdown("---")
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.info("""
                ### 📋 Instruções
                
                1. **Selecione** um arquivo PDF usando o botão acima
                2. **Clique** em "Processar Arquivo"
                3. **Aguarde** o processamento
                4. **Baixe** o arquivo Excel gerado

                """)

    # Rodapé
    render_footer()


if __name__ == "__main__":
    main()
