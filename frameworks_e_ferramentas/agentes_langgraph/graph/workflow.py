from langgraph.graph import StateGraph, END
from graph.state import AgentState

from langgraph.constants import Send

# Importação dos nós que criamos nos passos anteriores
from agents.fetch_agent import fetch_repo_node
from agents.sast_agent import sast_node
from agents.sca_agent import sca_node
from agents.docs_agent import docs_node
from agents.aggregator import aggregator_node
from tools.git_utils import cleanup_repository

def create_audit_graph():
    """
    Constrói e compila o grafo de estados para a auditoria de segurança.
    """
    
    # 1. Inicializamos o Grafo com o esquema do nosso AgentState
    workflow = StateGraph(AgentState)

    # 2. Adicionamos os nós ao grafo
    # O primeiro argumento é o nome do nó, o segundo é a função que o executa
    workflow.add_node("fetch_repo", fetch_repo_node)
    workflow.add_node("sast_scan", sast_node)
    workflow.add_node("sca_scan", sca_node)
    workflow.add_node("docs_analysis", docs_node)
    workflow.add_node("aggregator", aggregator_node)

    # 3. Definição das Bordas (O Fluxo)
    
    # O fluxo sempre começa pelo clone do repositório
    workflow.set_entry_point("fetch_repo")

    # FAN-OUT: Após o fetch_repo, disparamaos os 3 nós de análise em PARALELO.
    # No LangGraph, passar uma lista de destinos cria essa execução simultânea.
    def fan_out(state):
        return [
            Send("sast_scan", state),
            Send("sca_scan", state),
            Send("docs_analysis", state)
        ]

    workflow.add_conditional_edges("fetch_repo", fan_out)
    # FAN-IN: Cada nó de análise, ao terminar, aponta para o agregador.
    # O LangGraph garante que o 'aggregator' só execute quando TODOS os 
    # nós que apontam para ele tiverem concluído sua tarefa.
    workflow.add_edge("sast_scan", "aggregator")
    workflow.add_edge("sca_scan", "aggregator")
    workflow.add_edge("docs_analysis", "aggregator")

    # FIM: Após o agregador gerar o relatório, o fluxo termina.
    workflow.add_edge("aggregator", END)

    # 4. Compilação do Grafo
    return workflow.compile()

# Nó extra de utilidade (opcional mas recomendado para MLOps/Limpeza)
def cleanup_node(state: AgentState):
    """Nó final para limpar os arquivos temporários do disco."""
    if state.get("local_path"):
        cleanup_repository(state["local_path"])
    return state