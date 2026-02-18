#### Agente conversacional de arquitetura reflexiva (simples)

#regras - se X, então Y
regras_respostas = {
    "olá": "Olá! Bem-vindo à Cafeteria Python. Como posso ajudar?",
    "menu": "Temos Café Expresso, Latte e Cappuccino. Qual você prefere?",
    "preço": "Nossos cafés variam de R$ 5,00 a R$ 15,00.",
    "tchau": "Até logo! Volte sempre para um café.",
    "ajuda": "Eu posso te mostrar o menu, falar sobre preços ou apenas dizer oi!"
}

#função do agente relfexivo
def agente_reflexivo(entrada):
    #normalizando para minúsculo para evitar erros "bobos"
    entrada = entrada.lower()

    #lógica de reflexo (percorrendo as regras)
    for condicao, acao in regras_respostas.items():
        if condicao in entrada:
            return acao
    
    # se o cliente não disser algo que está no escopo
    return "Desculpe, o que você disse não está no meu escopo de resposta! Reclame com o RH para fazer uma arquitetura mais bem elaborada, rsrss"

print("BoTeste: Atendente de Arquitetura Reflexiva Ativo")


while True:
    entrada_usuario = input("Você: ")

    #saída do loop
    if entrada_usuario.lower() == "sair":
        print("Ok, estou encerrando por aqui! \n Tchau tchau!!")
        break

    resposta = agente_reflexivo(entrada_usuario)
    print("BoTeste: ", resposta)