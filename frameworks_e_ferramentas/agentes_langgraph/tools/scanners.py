import subprocess
import json
import os

def run_bandit_scan(local_path: str) -> list:
    """
    Executa o Bandit (SAST) no diretório do repositório.
    O Bandit procura por problemas de segurança comuns em código Python.
    """
    print(f"[TOOL] Iniciando Bandit Scan em: {local_path}")
    
    try:
        # Executamos o bandit via subprocess. 
        # -r: recursivo | -f json: output em formato legível para o agente | -quiet: menos ruído
        result = subprocess.run(
            ["bandit", "-r", local_path, "-f", "json", "-q"],
            capture_output=True,
            text=True
        )
        
        # O Bandit retorna exit code 1 se encontrar problemas, por isso não usamos check=True
        if result.stdout:
            data = json.loads(result.stdout)
            # Retornamos apenas a lista de 'results' (vulnerabilidades)
            return data.get("results", [])
        return []
        
    except Exception as e:
        print(f"[TOOL ERROR] Erro ao rodar Bandit: {e}")
        return [{"error": "Falha na execução do Bandit", "details": str(e)}]

def run_safety_scan(local_path: str) -> list:
    """
    Executa o Safety (SCA) para verificar vulnerabilidades em bibliotecas.
    Procura por arquivos 'requirements.txt'.
    """
    req_path = os.path.join(local_path, "requirements.txt")
    
    if not os.path.exists(req_path):
        print("[TOOL] Safety ignorado: requirements.txt não encontrado.")
        return []

    print(f"[TOOL] Iniciando Safety Scan no arquivo: {req_path}")
    
    try:
        # O Safety checa as versões das dependências contra um banco de dados de vulnerabilidades
        result = subprocess.run(
            ["safety", "check", "-r", req_path, "--json"],
            capture_output=True,
            text=True
        )
        
        if result.stdout:
            # O output do Safety pode variar conforme a versão
            # Quando não há vulnerabilidades, retorna texto (não JSON)
            try:
                return json.loads(result.stdout)
            except json.JSONDecodeError:
                # Safety retornou texto (sem vulnerabilidades encontradas)
                return []
        return []
        
    except Exception as e:
        print(f"[TOOL ERROR] Erro ao rodar Safety: {e}")
        return [{"error": "Falha na execução do Safety", "details": str(e)}]