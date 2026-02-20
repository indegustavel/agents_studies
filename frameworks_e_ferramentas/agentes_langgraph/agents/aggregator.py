from utils.llm_config import get_llm
from langchain_core.messages import SystemMessage, HumanMessage
from graph.state import AgentState
import json

def aggregator_node(state: AgentState) -> dict:
    """
    O Agregador atua como o 'CISO' (Chief Information Security Officer).
    Ele consolida os achados técnicos do SAST, SCA e Docs em um relatório final.
    """
    vulnerabilities = state["vulnerabilities"]
    doc_report = state["documentation_report"]
    
    llm = get_llm (temperature=0.2)

    system_prompt = (
        "Você é um Auditor de Segurança Sênior. Você receberá uma lista de vulnerabilidades "
        "técnicas (JSON) e um relatório de documentação. Sua meta é gerar um relatório "
        "final estruturado que classifique a gravidade geral do projeto e sugira correções."
    )

    # Convertemos a lista de vulnerabilidades acumulada para string
    vulnerabilities_str = json.dumps(vulnerabilities, indent=2)

    user_prompt = (
        f"--- ACHADOS TÉCNICOS ---\n{vulnerabilities_str}\n\n"
        f"--- ANÁLISE DE DOCUMENTAÇÃO ---\n{doc_report}\n\n"
        "Por favor, consolide tudo em um relatório final com: "
        "1. Resumo Executivo, 2. Riscos Críticos, 3. Plano de Remediação."
    )

    print("[AGENT] Agregador consolidando relatório final...")
    response = llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ])

    return {"final_audit": response.content}