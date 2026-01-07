# FabricIA

Agente inteligente para processamento e análise de laudos de avaliação em PDF, extraindo informações estruturadas e gerando planilhas Excel.

## 🔄 Arquitetura do Sistema

```mermaid
graph TD
    user((Usuário))
    web[Streamlit<br>Web App]
    cli[CLI<br>main.py]
    processor(PDF<br>Processor)
    rag(LlamaIndex<br>RAG)
    query(Query<br>Engine)

    user <--> web
    user <--> cli
    web --> processor
    cli --> processor
    processor --> rag
    rag --> query
    query <--> openai[OpenAI<br>Embeddings + GPT]
    query <--> cohere[Cohere<br>Rerank]
    query --> results[Resultados]
    results --> excel[Arquivo<br>Excel]
    results --> console[Console<br>Output]
```

### Componentes

- **Interfaces**: Streamlit Web App e CLI para entrada de PDFs
- **PDF Processor**: Valida e extrai texto dos laudos
- **LlamaIndex RAG**: Pipeline de indexação vetorial e recuperação
- **Query Engine**: Motor de consulta com reranking inteligente
- **Serviços Externos**: OpenAI (embeddings/LLM) e Cohere (reranking)
- **Outputs**: Excel estruturado ou saída no console

## 📋 Funcionalidades

- **Upload de PDF**: Interface web para upload de laudos de avaliação
- **Extração Inteligente**: Usa RAG (Retrieval-Augmented Generation) para extrair informações específicas
- **Perguntas Pré-configuradas**:
  - Nome da empresa avaliada
  - Nome da empresa avaliadora
  - Data do laudo
  - Metodologias de avaliação utilizadas

## 🚀 Como Usar

### Interface Web (Streamlit)

```bash
streamlit run run_app.py
```

### CLI

```bash
python main.py
```

## 🛠️ Tecnologias

- **LlamaIndex**: Framework RAG
- **OpenAI**: Embeddings e LLM (GPT-4)
- **Cohere**: Reranking de resultados
- **Streamlit**: Interface web
- **PyPDF2**: Extração de texto de PDFs
- **Pandas**: Manipulação de dados
