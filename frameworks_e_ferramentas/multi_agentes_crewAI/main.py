import os
from dotenv import load_dotenv
from crew import StockAnalystCrew
from datetime import datetime

# 1. Carregamos as chaves de API do arquivo .env
load_dotenv()

def run():
    """
    Função principal que inicia a execução da equipe.
    """
    print("### BEM-VINDO AO SEU ANALISTA DE INVESTIMENTOS AI ###")
    print("-" * 50)
    
    # 2. Definimos qual ação queremos analisar
    # Você pode mudar para 'AAPL', 'NVDA', 'ITUB4.SA', etc.
    inputs = {
        'ticket': 'NVDA',
        'data': datetime.now().strftime("%m-%d")
    }

    try:
        # 3. Instanciamos a nossa classe de equipe (criada no passo 3)
        # O método .crew() retorna o objeto Crew pronto para o combate
        # O método .kickoff() inicia o processo enviando os inputs
        resultado = StockAnalystCrew().crew().kickoff(inputs=inputs)

        print("\n\n" + "-" * 50)
        print("### ANÁLISE CONCLUÍDA COM SUCESSO! ###")
        print("-" * 50)
        
        # O resultado final também aparece aqui no console
        print(resultado)

    except Exception as e:
        print(f"Ocorreu um erro durante a execução: {e}")

if __name__ == "__main__":
    run()