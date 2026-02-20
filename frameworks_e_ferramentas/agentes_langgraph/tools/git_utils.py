# Aqui isolamos a lógica de sistema (GitPython).

import os
import tempfile
import shutil
from git import Repo # Import da biblioteca GitPython

def clone_repository(repo_url: str) -> str:
    """
    Clona um repositório remoto em um diretório temporário do sistema.
    Retorna o caminho (path) absoluto do diretório.
    """
    try:
        # Criamos um diretório temporário que persiste durante a execução do grafo
        target_dir = tempfile.mkdtemp(prefix="agent_audit_")
        
        print(f"[GIT] Clonando {repo_url} para {target_dir}...")
        
        # Faz o clone (pode demorar dependendo do tamanho do repo)
        # O depth=1 faz um "shallow clone", pegando apenas o último commit (mais rápido)
        Repo.clone_from(repo_url, target_dir, depth=1)
        
        return target_dir
    except Exception as e:
        print(f"[ERROR] Erro ao clonar repositório: {e}")
        raise e

def cleanup_repository(path: str):
    """Remove o diretório temporário após a conclusão do processo."""
    if path and os.path.exists(path):
        shutil.rmtree(path)
        print(f"[GIT] Diretório {path} removido com sucesso.")