### Arquitetura de Agentes baseada em modelo

# definindo estado inicial do mundo/modelo
modelo_mundo = {
    "estado_conversa": "inicio", # estados da conversa: inicio, escolhendo, confirmando, finalizado
    "item_escolhido": None,
    "valor_total": 0
}

# tabela de preços
PRECOS = {"expresso": 5.0, "latte": 10.0, "cappuccino": 15.0}

#criando a função de atualizar o modelo/estado/mundo do agente
def atualizar_estado(entrada):
    global modelo_mundo
    entrada = entrada.lower()

    # transicionando o estado: Início -> Escolhendo
    if modelo_mundo["estado_conversa"] == "inicio" and "olá" in entrada:
        modelo_mundo["estado_conversa"] = "escolhendo"
        return "Olá! Temos Expresso, Latte e Cappuccino. Qual você vai querer?"

    # transicionando o estado: Escolhendo -> Confirmando
    if modelo_mundo["estado_conversa"] == "escolhendo":
        for cafe in PRECOS.keys():
            if cafe in entrada:
                modelo_mundo["item_escolhido"] = cafe
                modelo_mundo["valor_total"] = PRECOS[cafe]
                modelo_mundo["estado_conversa"] = "confirmando"
                return f"Um {cafe.capitalize()}! Custa R$ {modelo_mundo['valor_total']:.2f}. Posso fechar o pedido?"

    # transicionando o estado: Confirmando -> Finalizado
    if modelo_mundo["estado_conversa"] == "confirmando":
        if "sim" in entrada or "pode" in entrada:
            modelo_mundo["estado_conversa"] = "finalizado"
            return f"Pedido de {modelo_mundo['item_escolhido']} confirmado! Prepare o Pix."
        elif "não" in entrada:
            modelo_mundo["estado_conversa"] = "escolhendo"
            return "Sem problemas. O que você gostaria no lugar?"

    return "Desculpe, não entendi. Estamos no meio de um pedido de café!"

# loop de execução
print("--- BoTeste 2.0: Arquitetura Baseada em Modelo ---")
while modelo_mundo["estado_conversa"] != "finalizado":
    user_input = input("Você: ")
    if user_input.lower() == "sair": break
    
    resposta = atualizar_estado(user_input)
    print(f"BoTeste: {resposta}")