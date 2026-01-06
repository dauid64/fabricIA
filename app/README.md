# Processador de PDF para Excel - Streamlit App

Uma aplicação modular desenvolvida em Streamlit para processar arquivos PDF e convertê-los em Excel.

## 📁 Estrutura do Projeto

```
app/
├── main.py                 # Aplicação principal
├── config.py              # Configurações (cores, logo, mensagens)
├── __init__.py
├── components/            # Componentes reutilizáveis da UI
│   ├── __init__.py
│   └── ui_components.py
├── services/              # Lógica de negócio
│   ├── __init__.py
│   └── pdf_processor.py   # Processador de PDF (ADICIONE SEU ALGORITMO AQUI)
├── utils/                 # Utilitários
│   ├── __init__.py
│   └── styles.py          # Estilos CSS customizados
└── assets/                # Recursos (logos, imagens)
    └── logo.png           # Coloque sua logo aqui
```

## 🚀 Como Executar

```bash
streamlit run app/main.py
```

## ⚙️ Personalização

### 1. Adicionar seu Algoritmo

Edite o arquivo `app/services/pdf_processor.py`:

```python
def process_pdf(self, pdf_file) -> Optional[BytesIO]:
    # ADICIONE SEU ALGORITMO AQUI
    # Processe o PDF e retorne um DataFrame
    # O código atual é apenas um exemplo
```

### 2. Customizar Cores e Estilo

Edite o arquivo `app/config.py`:

```python
# Altere as cores
PRIMARY_COLOR = "#FF4B4B"
BACKGROUND_COLOR = "#FFFFFF"
SECONDARY_BACKGROUND_COLOR = "#F0F2F6"
TEXT_COLOR = "#262730"
ACCENT_COLOR = "#FF6B6B"

# Altere mensagens
APP_TITLE = "Seu Título"
APP_SUBTITLE = "Seu Subtítulo"
```

### 3. Adicionar Logo

1. Coloque sua logo em `app/assets/logo.png`
2. Atualize o caminho em `app/config.py`:

```python
LOGO_PATH = "app/assets/logo.png"
```

## 📦 Dependências

Instale as dependências necessárias:

```bash
pip install streamlit pandas openpyxl PyPDF2
```

## 🎨 Funcionalidades

✅ Upload de arquivos PDF  
✅ Processamento customizável  
✅ Download de arquivo Excel  
✅ Interface amigável e responsiva  
✅ Customização de cores e logo  
✅ Barra de progresso  
✅ Validação de arquivos  
✅ Estatísticas de processamento  
✅ Mensagens de erro detalhadas

## 📝 Notas

- O algoritmo de processamento atual é apenas um exemplo
- Substitua o código em `pdf_processor.py` pelo seu algoritmo
- Todas as configurações estão centralizadas em `config.py`
- Os componentes da UI são modulares e reutilizáveis
