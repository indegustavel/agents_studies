# 🤖 Agente de Vendas Inteligente (LangChain + OpenRouter)

Este repositório contém um **Agente de Inteligência Artificial** construído com Python e LangChain, projetado para atuar como um assistente de vendas da loja fictícia "TechFlow".

O projeto foca em **arquitetura modular**, separação de responsabilidades e uso de **Tools (Ferramentas)** personalizadas para realizar ações reais (consultas e cálculos).

![Status](https://img.shields.io/badge/Status-Funcional-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-v0.1%2B-orange)
![OpenRouter](https://img.shields.io/badge/LLM-OpenRouter-purple)

## 🧠 O que este Agente faz?

O agente utiliza o padrão **ReAct (Reasoning + Acting)**. Ele não apenas responde com texto, mas:
1.  **Entende** a intenção do usuário.
2.  **Decide** qual ferramenta usar (Buscar Preço ou Calcular Imposto).
3.  **Executa** a ferramenta em Python.
4.  **Processa** o resultado e responde em linguagem natural.

### Funcionalidades Principais
- **Busca Flexível (Fuzzy Search):** Encontra produtos mesmo se o usuário digitar o nome incompleto (ex: "monitor" encontra "Monitor Gamer").
- **Cálculo Matemático:** Realiza cálculos de impostos precisos via código (evitando erros de matemática comuns em LLMs).
- **Memória de Conversação:** Mantém o contexto do chat (sabe o que é "ele" ou "o produto anterior").
- **Tratamento de Erros:** Sistema robusto para limpar respostas "sujas" (JSON/Listas) vindas do LLM.

---

## 📂 Estrutura do Projeto

O projeto segue uma arquitetura profissional baseada em pacotes `src`:

```text
meu-agente-ia/
├── src/
│   ├── agents/          # Lógica de construção do Agente e Executor
│   │   ├── base_agent.py
│   │   └── __init__.py
│   ├── tools/           # Ferramentas personalizadas (Funções Python)
│   │   ├── custom_tools.py
│   │   └── __init__.py
│   ├── prompts/         # Templates de instruções (System Prompts)
│   │   ├── prompts.py
│   │   └── __init__.py
│   ├── utils/           # Configurações de API e Helpers
│   │   ├── config.py    # Configuração do LLM (OpenRouter)
│   │   ├── helpers.py   # Limpeza de respostas
│   │   └── __init__.py
│   ├── __init__.py      # Torna a pasta src um pacote
│   └── main.py          # Ponto de entrada (CLI)
├── .env                 # Chaves de API (NÃO COMITAR)
├── .gitignore
├── README.md
└── requirements.txt

🚀 Como Rodar o Projeto

1. Pré-requisitos
Python 3.10 ou superior.

Uma chave de API da OpenRouter.

2. Instalação
Clone o repositório e entre na pasta:

Bash

git clone [https://github.com/seu-usuario/seu-repo.git](https://github.com/seu-usuario/seu-repo.git)
cd seu-repo
Crie e ative um ambiente virtual:

Bash

# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
Instale as dependências:

Bash

pip install langchain langchain-community langchain-openai python-dotenv
3. Configuração (.env)
Crie um arquivo .env na raiz do projeto e configure para usar a OpenRouter:

Snippet de código

# Sua chave da OpenRouter (começa com sk-or-...)
OPENAI_API_KEY=sk-or-vv-xxxxxxxxxxxxxxxxxxxxxxxxxxxx

# URL Base da OpenRouter (Essencial para substituir a OpenAI padrão)
OPENAI_API_BASE=[https://openrouter.ai/api/v1](https://openrouter.ai/api/v1)

# Nome do Modelo (ex: openai/gpt-4o-mini, anthropic/claude-3-haiku, meta-llama/llama-3-8b-instruct)
MODEL_NAME=openai/gpt-4o-mini

# Opcional: Monitoramento com LangSmith
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=sua-chave-langsmith
LANGCHAIN_PROJECT=agente-vendas-openrouter

🚀 Como Rodar o Projeto
1. Pré-requisitos
Python 3.10 ou superior.
Uma chave de API da OpenRouter.

2. Instalação
Clone o repositório e entre na pasta:

git clone [https://github.com/seu-usuario/seu-repo.git](https://github.com/seu-usuario/seu-repo.git)
cd seu-repo

Crie e ative um ambiente virtual:

# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate

Instale as dependências:

pip install requirements.txt

4. Execução
⚠️ Importante: Como o projeto usa estrutura de módulos, execute sempre a partir da raiz usando a flag -m:

python -m src.main

Troubleshooting Comum
Erro: ModuleNotFoundError: No module named 'src'

Causa: Você tentou rodar com python src/main.py.

Solução: Rode com python -m src.main na raiz do projeto.

Erro: O agente entra em loop ou repete a resposta

Causa: O histórico do chat recebeu lixo (JSON/dicionários) em vez de texto limpo.

Solução: O projeto já inclui um formatar_resposta_agente no main.py para evitar isso.

Este projeto é para fins educacionais.