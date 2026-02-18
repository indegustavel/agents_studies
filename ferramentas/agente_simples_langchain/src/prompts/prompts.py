from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# 1. Definimos a "Instrução de Sistema" (System Message)
# É aqui que moldamos o comportamento do agente.
INSTRUCOES_AGENTE = """
Você é um Assistente de Vendas especializado em eletrônicos da loja 'TechFlow'.
Sua principal função é ajudar os clientes a encontrar preços e calcular impostos.

Quando o cliente precisar consultar preços de produtos, acione a tool buscar_preco_produto.
Quando o cliente solicitar calcular impostos de importação, acione a tool calcular_imposto_importacao

Regras de comportamento:
1. Sempre use as ferramentas disponíveis para consultar preços. Não invente valores.
2. Se o cliente perguntar sobre um produto que não está na base, informe educadamente.
3. Para cálculos de imposto, sempre use a ferramenta 'calcular_imposto_importacao'.
4. Seja profissional, prestativo e responda em Português do Brasil.
5. Se você não souber a resposta e nenhuma ferramenta ajudar, admita que não sabe.
"""

def get_agent_prompt():
    """
    Cria e retorna o template de prompt configurado para o agente.
    """
    
    # Criamos o template que combina a instrução fixa com os campos dinâmicos
    prompt = ChatPromptTemplate.from_messages([
        # System Prompt: O "manual" do agente
        ("system", INSTRUCOES_AGENTE),
        
        # Placeholder para o histórico de conversa
        MessagesPlaceholder(variable_name="chat_history"),
        
        # Mensagem do Usuário: O que ele acabou de perguntar
        ("human", "{input}"),
        
        # O 'agent_scratchpad' é OBRIGATÓRIO para agentes.
        # É aqui que o LangChain anota os pensamentos intermediários ("Pensando...", "Usando ferramenta...")
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    
    return prompt

# Para importar como string pura
SYSTEM_PROMPT_STR = INSTRUCOES_AGENTE