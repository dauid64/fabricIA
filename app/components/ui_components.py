"""
Componentes reutilizáveis da UI
"""

import streamlit as st
import base64
from pathlib import Path
from .. import config


def _get_image_base64(image_path: Path) -> str:
    """
    Converte imagem para base64
    """
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


def render_header():
    """
    Renderiza o cabeçalho da aplicação com logo centralizada
    """
    # Tenta carregar a logo se existir
    logo_path = Path(config.LOGO_PATH)

    # Tenta diferentes caminhos possíveis
    if not logo_path.exists():
        # Tenta caminho absoluto baseado no arquivo atual
        current_file = Path(__file__).parent.parent
        logo_path = current_file / "assets" / "logo.png"

    # Centraliza a logo
    col1, col2, col3 = st.columns([2, 3, 2])
    with col2:
        if logo_path.exists():
            st.markdown(
                f"""
                <div style="display: flex; justify-content: center;">
                    <img src="data:image/png;base64,{_get_image_base64(logo_path)}" width="300">
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown("<h1 style='text-align: center;'>📄</h1>",
                        unsafe_allow_html=True)

    st.markdown("---")


def render_welcome_message():
    """
    Renderiza a mensagem de boas-vindas
    """
    st.info(f"👋 {config.MESSAGES['welcome']}")


def render_file_uploader():
    """
    Renderiza o componente de upload de arquivo

    Returns:
        Arquivo PDF enviado pelo usuário ou None
    """
    st.subheader("📤 Upload de Arquivo")

    uploaded_file = st.file_uploader(
        config.MESSAGES['upload_instruction'],
        type=config.ACCEPTED_FILE_TYPES,
        help=f"Tamanho máximo: {config.MAX_FILE_SIZE_MB}MB",
        label_visibility="collapsed"
    )

    if uploaded_file:
        # Mostra informações do arquivo
        file_details = {
            "Nome do arquivo": uploaded_file.name,
            "Tamanho": f"{uploaded_file.size / 1024:.2f} KB",
            "Tipo": uploaded_file.type
        }

        with st.expander("ℹ️ Informações do arquivo", expanded=False):
            for key, value in file_details.items():
                st.text(f"{key}: {value}")

    return uploaded_file


def render_processing_status(status: str = "processing"):
    """
    Renderiza o status do processamento

    Args:
        status: 'processing', 'success', ou 'error'
    """
    if status == "processing":
        with st.spinner(config.MESSAGES['processing']):
            st.empty()
    elif status == "success":
        st.success(config.MESSAGES['success'])
    elif status == "error":
        st.error(config.MESSAGES['error'])


def render_download_button(excel_file, filename: str = "resultado.xlsx"):
    """
    Renderiza o botão de download do arquivo Excel

    Args:
        excel_file: Arquivo Excel processado (BytesIO)
        filename: Nome do arquivo para download
    """
    st.markdown("---")
    st.subheader("📥 Download")
    st.success(config.MESSAGES['download_ready'])

    st.download_button(
        label="⬇️ Baixar arquivo Excel",
        data=excel_file,
        file_name=filename,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        use_container_width=True
    )


def render_sidebar_info():
    """
    Renderiza informações na barra lateral
    """
    with st.sidebar:
        st.markdown("## ℹ️ Sobre")
        st.markdown("""
        FabricIA é uma agente que estrutura uma analise da empresas a partir de dados de laudos que estão disponíveis na CVM.
        
        **Como usar:**
        1. Faça upload do laudo em formato PDF
        2. Aguarde o processamento
        3. Faça o download do arquivo Excel
        """)


def render_error_message(error: str):
    """
    Renderiza uma mensagem de erro formatada

    Args:
        error: Mensagem de erro
    """
    st.error(f"❌ {config.MESSAGES['error']}")
    with st.expander("🔍 Detalhes do erro"):
        st.code(error)


def render_footer():
    """
    Renderiza o rodapé da aplicação
    """
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666; padding: 20px;'>
            <p>Desenvolvido por Carlos David Neto @ LAMFO</p>
        </div>
        """,
        unsafe_allow_html=True
    )
