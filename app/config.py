"""
Configurações da aplicação Streamlit
Aqui você pode personalizar cores, logos e outras configurações da interface
"""

# ===========================
# CONFIGURAÇÕES VISUAIS
# ===========================

# Cores do tema (formato hexadecimal)
PRIMARY_COLOR = "#FF4B4B"  # Cor principal (botões, links)
BACKGROUND_COLOR = "#FFFFFF"  # Cor de fundo
SECONDARY_BACKGROUND_COLOR = "#F0F2F6"  # Cor de fundo secundária
TEXT_COLOR = "#262730"  # Cor do texto
ACCENT_COLOR = "#FF6B6B"  # Cor de destaque

# ===========================
# LOGO E BRANDING
# ===========================

# Caminho para a logo (coloque sua logo em app/assets/)
LOGO_PATH = "app/assets/logo.png"  # Altere para o caminho da sua logo

# Título da aplicação
APP_TITLE = "FabricIA"
APP_SUBTITLE = "Converta seus arquivos PDF em Excel"

# ===========================
# CONFIGURAÇÕES DA PÁGINA
# ===========================

PAGE_CONFIG = {
    "page_title": "FabricIA",
    "page_icon": "📄",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
}

# ===========================
# CONFIGURAÇÕES DE UPLOAD
# ===========================

# Tamanho máximo de arquivo (em MB)
MAX_FILE_SIZE_MB = 200

# Tipos de arquivo aceitos
ACCEPTED_FILE_TYPES = ["pdf"]

# ===========================
# MENSAGENS DA INTERFACE
# ===========================

MESSAGES = {
    "welcome": "Olá, eu sou a FabricIA! sua agente analista de empresas.",
    "upload_instruction": "Faça o upload de um arquivo PDF para começar",
    "processing": "Processando seu arquivo...",
    "success": "Arquivo processado com sucesso! ✅",
    "error": "Ocorreu um erro ao processar o arquivo.",
    "download_ready": "Seu arquivo Excel está pronto para download!",
}
