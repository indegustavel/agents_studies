from graph.state import AgentState
from tools.scanners import run_safety_scan
import os

def sca_node(state: AgentState) -> dict:
    """
    Agente responsável por verificar vulnerabilidades em pacotes externos (SCA).
    """
    path = state["local_path"]
    
    findings = run_safety_scan(path)
    
    vulnerabilities_update = []
    for f in findings:
        # O Safety tem um formato de retorno diferente, mapeamos conforme necessário
        # Nota: Ajustar campos de acordo com a versão do Safety instalada
        vulnerabilities_update.append({
            "agent": "SCA (Safety)",
            "severity": "HIGH", # Safety free nem sempre traz a severidade detalhada
            "package": f[0] if isinstance(f, list) else f.get("package"),
            "description": f[3] if isinstance(f, list) else f.get("advisory"),
            "version": f[2] if isinstance(f, list) else f.get("installed")
        })
        
    return {"vulnerabilities": vulnerabilities_update}