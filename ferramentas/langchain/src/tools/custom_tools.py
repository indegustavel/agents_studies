from langchain_core.tools import tool

# O decorador @tool transforma uma função comum em uma ferramenta que o LangChain entende.
# O nome da função e o docstring são enviados ao LLM como 'manual de instruções'.

@tool
def buscar_preco_produto(nome_produto: str) -> str:
    """
    Útil para consultar o preço de um produto específico na nossa base de dados.
    O nome do produto deve ser fornecido de forma clara.
    """
    # Aqui você conectaria com um banco de dados real ou uma API.
    # Por enquanto, vamos simular uma base de dados (Mock).
    base_dados_precos = {
        "laptop": "R$ 4500,00",
        "mouse": "R$ 150,00",
        "teclado": "R$ 300,00",
        "monitor": "R$ 1200,00",
        "mousepad": "R$ 67,00",
        "smartphone": "R$ 2000,00"
    }
    
    # Normalizamos o input para busca (ex: tudo em minúsculo)
    produto_formatado = nome_produto.lower().strip()
    
    # Retornamos o preço ou uma mensagem amigável caso não exista.
    # Método reflexivo para evitar latência e custo desnecessário
    return base_dados_precos.get(produto_formatado, f"Desculpe, o produto '{nome_produto}' não foi encontrado.")

@tool
def calcular_imposto_importacao(valor_base: float) -> float:
    """
    Calcula o imposto de importação simplificado (60%) sobre o valor de um produto.
    Recebe um valor numérico e retorna o valor do imposto.
    """
    # Exemplo de lógica de negócio que o LLM não saberia fazer sozinho com precisão
    taxa = 0.60
    imposto = valor_base * taxa
    return imposto

# Lista exportável para facilitar a importação no arquivo principal do agente
# Agrupar as ferramentas facilita passar todas de uma vez para o agente depois.
ferramentas_disponiveis = [buscar_preco_produto, calcular_imposto_importacao]