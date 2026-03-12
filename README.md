# LangChain — Estudos Práticos

Repositório de estudos progressivos com o framework **LangChain**, cobrindo desde conceitos fundamentais até agentes autônomos com banco de dados vetorial. Cada pasta representa uma etapa de aprendizado independente e autocontida.

---

## Estrutura do Projeto

### `fundamentos/`
Introdução ao ecossistema LangChain e integração com modelos de linguagem.

| Arquivo | O que ensina |
|---|---|
| `hellow-world.py` | Primeira chamada a um LLM (OpenAI) via LangChain — invocação simples com `ChatOpenAI` |
| `init-chat-model.py` | Como usar `init_chat_model` para instanciar qualquer provider (ex: Google Gemini) de forma agnóstica |
| `prompt-template.py` | Criação de templates reutilizáveis com `PromptTemplate` e variáveis dinâmicas |
| `chat-prompt-template.py` | Templates para conversas com múltiplos papéis (system/user) usando `ChatPromptTemplate` |

---

### `chains-e-processamento/`
Composição de pipelines de processamento com o padrão LCEL (LangChain Expression Language).

| Arquivo | O que ensina |
|---|---|
| `iniciando-com-chains.py` | Criação de uma chain simples com operador `\|` encadeando prompt → modelo |
| `pipeline-de-processamento.py` | Pipeline multi-etapa: tradução → resumo, com `StrOutputParser` entre as chains |
| `chains-com-decorators.py` | Uso do decorator `@chain` para transformar funções Python em Runnables composáveis |
| `runnable-lambda.py` | Como transformar qualquer função em um Runnable com `RunnableLambda` |
| `sumarizacao.py` | Sumarização de texto longo com divisão em chunks via `RecursiveCharacterTextSplitter` |
| `pipeline-de-sumarizacao.py` | Pipeline Map-Reduce para sumarização: sumariza chunks individualmente e depois combina |
| `sumarizacao-com-map-reduce.py` | Implementação alternativa de Map-Reduce usando `chain.map()` para processamento paralelo de chunks |

---

### `3-agentes-e-tools/`
Criação de agentes ReAct que decidem autonomamente quais ferramentas usar.

| Arquivo | O que ensina |
|---|---|
| `1-agente-react-e-tools.py` | Construção de um agente com ferramentas customizadas (`@tool`): calculadora e busca mock de capitais |
| `2-agente-react-usando-prompt-hub.py` | Variação do agente ReAct com `create_agent` e configuração de prompt de sistema personalizado |

---

### `4-gerenciamento-de-memoria/`
Persistência de contexto conversacional entre múltiplas interações.

| Arquivo | O que ensina |
|---|---|
| `1-armazenamento-de-historico.py` | Memória de sessão com `InMemoryChatMessageHistory` e `RunnableWithMessageHistory` |
| `2-historico-baseado-em-sliding-window.py` | Janela deslizante de memória com `trim_messages` para controlar o tamanho do histórico enviado ao LLM |

---

### `5-loaders-e-banco-de-dados-vetoriais/`
Carregamento de documentos externos, vetorização e busca semântica com PostgreSQL.

| Arquivo | O que ensina |
|---|---|
| `1-carregamento-usando-WebBaseLoader.py` | Carregamento de páginas web com `WebBaseLoader` e divisão em chunks |
| `2-carregamento-de-pdf.py` | Leitura e chunking de arquivos PDF com `PyPDFLoader` |
| `3-ingestion-pgvector.py` | Pipeline completo de ingestão: PDF → chunks → embeddings (OpenAI) → armazenamento no PGVector |
| `4-search-vector.py` | Busca semântica por similaridade no PGVector com `similarity_search_with_score` |

---

## Pré-requisitos

- Python 3.11+
- Docker e Docker Compose (para o banco vetorial)
- Chave de API da OpenAI
- Chave de API do Google Gemini (opcional, apenas para `init-chat-model.py`)

---

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/FelipeCararo/langchain.git
cd langchain
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

```bash
cp .env.example .env
```

Edite o `.env` e preencha suas chaves:

```env
OPENAI_API_KEY=sk-...
GOOGLE_API_KEY=...          # opcional
OPENAI_MODEL=text-embedding-3-small
PGVECTOR_URL=postgresql+psycopg://postgres:postgres@localhost:5432/rag
PGVECTOR_COLLECTION=gpt5_collection
```

### 5. Suba o banco de dados vetorial (apenas para a pasta `5-loaders-e-banco-de-dados-vetoriais`)

```bash
docker compose up -d
```

Aguarde o container ficar saudável antes de executar os scripts de ingestão.

### 6. Execute qualquer script

```bash
# Exemplos
python fundamentos/hellow-world.py
python chains-e-processamento/pipeline-de-processamento.py
python 3-agentes-e-tools/1-agente-react-e-tools.py

# Para o banco vetorial, rode na ordem:
python 5-loaders-e-banco-de-dados-vetoriais/3-ingestion-pgvector.py
python 5-loaders-e-banco-de-dados-vetoriais/4-search-vector.py
```

---

## Tecnologias

- [LangChain](https://www.langchain.com/) — framework principal
- [LangGraph](https://langchain-ai.github.io/langgraph/) — orquestração de agentes
- [OpenAI API](https://platform.openai.com/) — modelos GPT e embeddings
- [Google Gemini](https://ai.google.dev/) — modelo alternativo
- [PGVector](https://github.com/pgvector/pgvector) — banco de dados vetorial sobre PostgreSQL
- [Docker](https://www.docker.com/) — containerização do banco de dados
