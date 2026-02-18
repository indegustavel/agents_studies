from langchain_core.tools import tool
import unicodedata

def normalizar_texto(texto: str) -> str:
    """Remove acentos e coloca em minúsculo para facilitar a busca."""
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII').lower()

@tool
def buscar_preco_produto(consulta_usuario: str) -> str:
    """
    Útil para consultar o preço de um produto.
    Funciona mesmo se o nome não for exato (ex: 'monitor gamer' acha 'monitor').
    Acione a tool quando o cliente solicitar o preço de algum produto, ou quando você precisar saber o preço de algum produto
    """
    # Nossa "Base de Dados"
    base_dados_precos = {
        "laptop": "R$ 4500,00",
        "mouse": "R$ 150,00",
        "teclado": "R$ 300,00",
        "monitor": "R$ 1200,00",
        "smartphone": "R$ 2500,00"
    }
    
    # 1. Normalização (para "Teclado" achar "teclado")
    consulta_norm = normalizar_texto(consulta_usuario)
    
    # 2. Busca Inteligente (Iterativa)
    # Verifica se alguma chave do banco está DENTRO do que o usuário pediu
    # Ex: Se usuário pediu "preço do monitor ultra", a chave "monitor" será encontrada.
    produto_encontrado = None
    
    for produto_db, preco in base_dados_precos.items():
        produto_db_norm = normalizar_texto(produto_db)
        
        # Lógica: Se "monitor" (banco) está dentro de "monitor gamer" (pesquisa)
        # OU se "monitor gamer" (pesquisa) contém "monitor" (banco)
        if produto_db_norm in consulta_norm or consulta_norm in produto_db_norm:
            produto_encontrado = (produto_db, preco)
            break # Paramos no primeiro match
            
    if produto_encontrado:
        nome, valor = produto_encontrado
        return f"Encontrado: O {nome} custa {valor}."
    
    # 3. Fail-safe: Se não achou nada, retorna a lista para o Agente saber o que tem.
    produtos_disponiveis = ", ".join(base_dados_precos.keys())
    return f"Não encontrei '{consulta_usuario}'. Temos apenas estes produtos: {produtos_disponiveis}."

@tool
def calcular_imposto_importacao(valor_base: float) -> float:
    """Calcula 60% de imposto sobre o valor numérico informado."""
    return valor_base * 0.60

# Lista exportável
ferramentas_disponiveis = [buscar_preco_produto, calcular_imposto_importacao]