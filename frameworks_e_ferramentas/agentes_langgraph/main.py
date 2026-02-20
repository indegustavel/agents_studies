import os
import sys
from dotenv import load_dotenv

# Adiciona o diretório 'src' ao path para que os imports funcionem corretamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from graph.workflow import create_audit_graph

# 1. Carregar variáveis de ambiente (Chave da OpenAI)
load_dotenv()

def run_security_audit(url: str):
    """
    Função principal para executar o fluxo de auditoria.
    """
    # 2. Instanciar o grafo compilado
    app = create_audit_graph()
    
    # 3. Configurar o estado inicial
    # O 'vulnerabilities' começa como lista vazia por causa do operator.add
    initial_state = {
        "repo_url": url,
        "vulnerabilities": [],
        "files_list": []
    }
    
    print(f"\n{'='*50}")
    print(f"🔍 Iniciando Auditoria: {url}")
    print(f"{'='*50}\n")
    
    # 4. Execução em Stream (permite ver cada agente trabalhando)
    final_output = None
    for output in app.stream(initial_state):
        for node_name, state_update in output.items():
            print(f"✅ Nó concluído: {node_name}")
            # Guardamos o último estado para exibir o relatório final
            final_output = state_update

    # 5. Exibir o Relatório Final do Aggregator
    print(f"\n{'='*50}")
    print("📄 RELATÓRIO FINAL DE AUDITORIA")
    print(f"{'='*50}\n")
    
    # O aggregator salva o resultado na chave 'final_audit'
    # Como o stream retorna o update de cada nó, pegamos o do último estado conhecido
    if "final_audit" in final_output:
        print(final_output["final_audit"])
    else:
        # Fallback caso o stream se comporte de forma diferente na sua versão
        print("Erro ao recuperar o relatório final.")

if __name__ == "__main__":
    # Teste com um repositório real de exemplo (ou o seu próprio)
    test_repo = "https://github.com/flavorjones/loofah" # Exemplo de repo Ruby/Python
    run_security_audit(test_repo)