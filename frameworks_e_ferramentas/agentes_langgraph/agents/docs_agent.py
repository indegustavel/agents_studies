import os
from langchain_core.messages import SystemMessage, HumanMessage
from graph.state import AgentState
from utils.llm_config import get_llm

def docs_node(state: AgentState) -> dict:
    """
    Agente baseado em LLM que analisa a documentação do repositório.
    Busca por instruções inseguras que ferramentas estáticas ignoram.
    """
    local_path = state["local_path"]
    files = state["files_list"]
    
    # 1. Localiza o README (independente de maiúsculas/minúsculas)
    readme_path = next((f for f in files if f.lower() == "readme.md"), None)
    
    if not readme_path:
        return {"documentation_report": "README.md não encontrado para análise."}

    # 2. Leitura do arquivo com limite de segurança (Token Window)
    full_path = os.path.join(local_path, readme_path)
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            # Lemos apenas os primeiros 10k caracteres para evitar estouro de contexto
            # Em um cenário de MLOps real, você poderia usar RAG se o doc fosse imenso
            content = f.read(10000) 
    except Exception as e:
        return {"documentation_report": f"Erro ao ler documentação: {e}"}

    # 3. Configuração do LLM (Certifique-se de ter OPENROUTER_API_KEY no .env)
    # Usando a função centralizada para obter o LLM
    llm = get_llm(temperature=0.2)

    # 4. Prompt focado em Segurança (System Message)
    system_prompt = (
        "Você é um Especialista em Segurança de Infraestrutura e DevOps. "
        "Sua tarefa é analisar o README de um projeto e encontrar instruções perigosas. "
        "Exemplos: sugestões de chmod 777, desativação de firewall, exposição de chaves, "
        "ou comandos 'curl | sudo bash' sem explicação."
    )

    user_prompt = f"Analise o seguinte trecho da documentação e liste riscos potenciais:\n\n{content}"

    # 5. Chamada ao Modelo
    print(f"[AGENT] Docs Agent analisando {readme_path}...")
    response = llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ])

    return {"documentation_report": response.content}