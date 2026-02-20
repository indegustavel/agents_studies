from graph.state import AgentState
from tools.scanners import run_bandit_scan
import os

def sast_node(state: AgentState) -> dict:
    """
    Agente responsável pela análise estática (SAST).
    Lê o código fonte e identifica padrões perigosos (ex: shell=True, senhas hardcoded).
    """
    path = state["local_path"]
    
    # Chama a ferramenta que criamos acima
    findings = run_bandit_scan(path)
    
    # Preparamos o formato para o nosso estado
    # Adicionamos uma tag de 'source' para o agregador saber quem encontrou o quê
    vulnerabilities_update = []
    for f in findings:
        vulnerabilities_update.append({
            "agent": "SAST (Bandit)",
            "severity": f.get("issue_severity"),
            "file": os.path.basename(f.get("filename", "unknown")),
            "description": f.get("issue_text"),
            "line": f.get("line_number")
        })
        
    # IMPORTANTE: Retornamos apenas a chave 'vulnerabilities'. 
    # O LangGraph vai usar o operator.add para concatenar esta lista.
    return {"vulnerabilities": vulnerabilities_update}