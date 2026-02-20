import os
from graph.state import AgentState
from tools.git_utils import clone_repository

def fetch_repo_node(state: AgentState) -> dict:
    """
    Nó responsável por baixar o código fonte e preparar o terreno.
    
    Este é o primeiro nó do grafo. Ele recebe a URL, realiza o clone
    e gera um inventário de arquivos para que os próximos agentes
    não precisem 'adivinhar' o que existe no repositório.
    """
    
    # 1. Extrai a URL do estado (que virá do input inicial do usuário)
    url = state["repo_url"]
    
    try:
        # 2. Executa a ferramenta de clone (GitPython)
        # Retorna o caminho absoluto do diretório temporário
        local_path = clone_repository(url)
        
        # 3. Faz um inventário de arquivos para facilitar a filtragem nos próximos nós
        # Como você é de DevOps/MLOps, sabe que indexar arquivos ajuda a evitar 
        # recursividade desnecessária em larga escala.
        all_files = []
        for root, dirs, files in os.walk(local_path):
            # Removemos diretórios ocultos (como .git) da busca
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            for file in files:
                # Armazenamos o caminho relativo para o agente de documentos ler depois
                relative_path = os.path.relpath(os.path.join(root, file), local_path)
                all_files.append(relative_path)

        # RETORNO: No LangGraph, você retorna apenas as chaves que deseja ATUALIZAR.
        # local_path: de None para o path real
        # files_list: lista de strings com os nomes dos arquivos
        return {
            "local_path": local_path,
            "files_list": all_files
        }
        
    except Exception as e:
        # Em um sistema real, aqui poderíamos direcionar para um nó de erro
        print(f"[FETCH NODE] Erro crítico: {e}")
        raise e