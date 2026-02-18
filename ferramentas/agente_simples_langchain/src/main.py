from langchain_core.messages import HumanMessage, AIMessage

# Importações internas do nosso projeto modular
from src.utils.config import get_llm
from src.tools.custom_tools import ferramentas_disponiveis
from src.prompts.prompts import get_agent_prompt
from src.agents.base_agent import criar_agente_vendas

def executar_fluxo_conversa():
    # 1. Inicializar componentes base
    llm = get_llm()
    tools = ferramentas_disponiveis
    prompt = get_agent_prompt()

    # 2. Construir o agente usando nossa fábrica em src/agents/
    agente_vendas = criar_agente_vendas(llm, tools, prompt)

    # 3. Gerenciar o histórico de chat (Memória)
    # Em um sistema real, isso poderia ser recuperado de um Redis ou SQL.
    chat_history = []

    print("--- Assistente de Vendas Inicializado (Digite 'sair' para encerrar) ---")

    while True:
        # Captura a entrada do usuário
        user_input = input("\nVocê: ")
        
        #Método reflexivo para evitar latência e custos desnecessários
        if user_input.lower() in ["sair", "exit", "quit"]:
            break

        # Invocação do Agente
        # Passamos o input atual e o histórico acumulado
        resposta = agente_vendas.invoke({
            "input": user_input,
            "chat_history": chat_history
        })

        # Exibimos a resposta final (o campo 'output' contém a string de resposta)
        agente_msg = resposta["output"]
        print(f"\nAgente: {agente_msg}")

        # ATUALIZAÇÃO DA MEMÓRIA:
        # Adicionamos a pergunta e a resposta ao histórico para a próxima iteração
        chat_history.append(HumanMessage(content=user_input))
        chat_history.append(AIMessage(content=agente_msg))

if __name__ == "__main__":
    executar_fluxo_conversa()