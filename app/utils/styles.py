"""
Estilos CSS customizados para a aplicação
"""

from .. import config


def get_custom_css() -> str:
    """
    Retorna o CSS customizado baseado nas configurações

    Returns:
        str: CSS customizado
    """
    return f"""
    <style>
        /* Cores principais */
        :root {{
            --primary-color: {config.PRIMARY_COLOR};
            --background-color: {config.BACKGROUND_COLOR};
            --secondary-bg-color: {config.SECONDARY_BACKGROUND_COLOR};
            --text-color: {config.TEXT_COLOR};
            --accent-color: {config.ACCENT_COLOR};
        }}
        
        /* Estilo do header */
        .main-header {{
            background: linear-gradient(135deg, {config.PRIMARY_COLOR} 0%, {config.ACCENT_COLOR} 100%);
            padding: 2rem;
            border-radius: 10px;
            color: white;
            margin-bottom: 2rem;
        }}
        
        /* Botões customizados */
        .stButton>button {{
            background-color: {config.PRIMARY_COLOR};
            color: white;
            border-radius: 8px;
            padding: 0.75rem 2rem;
            font-weight: 600;
            border: none;
            transition: all 0.3s ease;
        }}
        
        .stButton>button:hover {{
            background-color: {config.ACCENT_COLOR};
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }}
        
        /* Cards */
        .upload-card {{
            background-color: {config.SECONDARY_BACKGROUND_COLOR};
            padding: 2rem;
            border-radius: 10px;
            border: 2px dashed {config.PRIMARY_COLOR};
            text-align: center;
            transition: all 0.3s ease;
        }}
        
        .upload-card:hover {{
            border-color: {config.ACCENT_COLOR};
            background-color: #E8EAED;
        }}
        
        /* Download section */
        .download-section {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            border-radius: 10px;
            color: white;
            margin-top: 2rem;
        }}
        
        /* File uploader customization */
        .stFileUploader {{
            background-color: {config.SECONDARY_BACKGROUND_COLOR};
            padding: 2rem;
            border-radius: 10px;
        }}
        
        /* Info boxes */
        .stAlert {{
            border-radius: 10px;
            border-left: 4px solid {config.PRIMARY_COLOR};
        }}
        
        /* Sidebar */
        .css-1d391kg {{
            background-color: {config.SECONDARY_BACKGROUND_COLOR};
        }}
        
        /* Expander */
        .streamlit-expanderHeader {{
            background-color: {config.SECONDARY_BACKGROUND_COLOR};
            border-radius: 8px;
        }}
        
        /* Metrics */
        .stMetric {{
            background-color: {config.SECONDARY_BACKGROUND_COLOR};
            padding: 1rem;
            border-radius: 8px;
        }}
        
        /* Progress bar */
        .stProgress > div > div {{
            background-color: {config.PRIMARY_COLOR};
        }}
        
        /* Animation for upload */
        @keyframes fadeIn {{
            from {{
                opacity: 0;
                transform: translateY(20px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        .fade-in {{
            animation: fadeIn 0.5s ease-in;
        }}
        
        /* Responsive adjustments */
        @media (max-width: 768px) {{
            .stButton>button {{
                width: 100%;
            }}
        }}
    </style>
    """


def apply_custom_styles():
    """
    Aplica os estilos customizados na aplicação Streamlit
    """
    import streamlit as st
    st.markdown(get_custom_css(), unsafe_allow_html=True)
