# Centraliza o esquema de dados. 
# Como você usará operator.add para a lista de vulnerabilidades, mantê-lo em um arquivo separado 
# evita dependências circulares quando os nós precisarem importar o tipo do estado.

from typing import TypedDict, List, Annotated, Optional
import operator

# O AgentState define a estrutura de dados que o Grafo irá manipular.
# Cada nó recebe esse estado e retorna uma versão atualizada dele.
class AgentState(TypedDict):
    # URL do repositório Git que será analisado (Input do usuário)
    repo_url: str
    
    # Caminho local onde o repositório será clonado temporariamente
    local_path: Optional[str]
    
    # Annotated[List[dict], operator.add] é a "mágica" do LangGraph.
    # Quando múltiplos nós rodam em paralelo e retornam uma lista em 'vulnerabilities',
    # o LangGraph usa o operator.add para concatenar as listas em vez de sobrescrever.
    vulnerabilities: Annotated[List[dict], operator.add]
    
    # Relatório textual gerado pela análise do README via LLM
    documentation_report: Optional[str]
    
    # String ou JSON final consolidando todos os achados
    final_audit: Optional[str]
    
    # Lista de arquivos relevantes encontrados (útil para filtrar o que o LLM lê)
    files_list: List[str]