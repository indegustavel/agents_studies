from langchain_classic.agents import AgentExecutor, create_openai_tools_agent


def criar_agente_vendas(llm, tools, prompt):
    """
    Cria a estrutura lógica do agente de vendas.
    
    Parâmetros:
        llm: A instância do modelo de linguagem (configurada no utils/config.py).
        tools: Lista de ferramentas (definidas no tools/custom_tools.py).
        prompt: O template de instruções (definido no prompts/prompts.py).
        
    Returns:
        AgentExecutor: O motor pronto para receber comandos.
    """
    
    # 1. 'agent' define COMO o LLM deve processar os inputs e decidir pelas ferramentas.
    # O create_openai_tools_agent é específico para modelos que usam 'Tool Calling'.
    agent = create_openai_tools_agent(llm, tools, prompt)
    
    # 2. 'AgentExecutor' é o ambiente que realmente roda o loop de pensamento.
    # Ele lida com erros, chama as ferramentas e gerencia o scratchpad.
    executor = AgentExecutor(
        agent=agent, 
        tools=tools, 
        verbose=True,           # Exibe os pensamentos no console para debug
        handle_parsing_errors=True # Se o LLM cometer um erro de formatação, o executor tenta corrigir
    )
    
    return executor