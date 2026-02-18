#### Arquitetura Híbrida Básica (SEM LLM ou frameworks robustos)

import random

class BoTesteHibrido:
    def __init__(self):
        self.meta_venda = "oferecer_acompanhamento"

        # banco de dados
        self.cardapio = {
            "expresso": "um clássico intenso e encorpado, com grãos 100% arábica (R$ 6,00)",
            "latte": "suave e cremoso, com aquela camada perfeita de leite vaporizado (R$ 12,00)",
            "cappuccino": "o equilíbrio ideal entre café, leite e um toque de cacau e canela (R$ 14,00)",
            "cold brew": "extraído a frio por 12h, super refrescante e com baixa acidez (R$ 15,00)"
        }
        self.estoque_cookies = 3

    # CAMADA 1: REFLEXIVA (Instinto/Velocidade)
    def camada_reflexiva(self, entrada):
        gatilhos = {
            "ajuda": "Claro! Posso te mostrar o menu, falar os preços ou fechar seu pedido.",
            "tchau": "Até mais! O cheirinho de café vai estar te esperando.",
            "onde": "Estamos no Instituto de Informática, na Universidade Federal de Goiás!"
        }
        return gatilhos.get(entrada, None)

    # CAMADA 2: DELIBERATIVA (Raciocínio e Objetivos)
    def camada_deliberativa(self, entrada):

        # gera menu para conversa natural
        if "menu" in entrada or "cardápio" in entrada or "opções" in entrada:
            menu_texto = "Com certeza! Olha só o que preparei para você hoje:\n"
            for item, desc in self.cardapio.items():
                menu_texto += f"☕ {item.capitalize()}: {desc}.\n"
            menu_texto += "\nQual desses mais te agrada agora?"
            return menu_texto

        # lógica de venda (sub-objetivo)
        for cafe in self.cardapio.keys():
            if cafe in entrada:
                if self.estoque_cookies > 0:
                    self.estoque_cookies -= 1
                    return (f"Excelente escolha! O nosso {cafe} sai em 2 minutinhos. "
                            f"Aceita um de nossos últimos {self.estoque_cookies + 1} cookies artesanais "
                            f"para acompanhar? Combina muito bem!")
                return f"Perfeito! Vou preparar o seu {cafe} agora mesmo."

        return "Não consegui identificar o pedido. Que tal dar uma olhadinha no nosso 'menu'?"

    # CAMADA 3: COORDENAÇÃO
    def coordenador(self, entrada):
        entrada = entrada.lower().strip()

        # Prioridade 1: Filtro Reativo (Segurança/Comandos Rápidos)
        reacao = self.camada_reflexiva(entrada)
        if reacao: return f"[REATIVO]: {reacao}"

        # Prioridade 2: Processamento Deliberativo (Inteligência/Vendas)
        decisao = self.camada_deliberativa(entrada)
        return f"[DELIBERATIVO]: {decisao}"

# Execução
bot = BoTesteHibrido()
print("--- BoTeste 3.0: Atendimento Gourmet Ativo ---")

while True:
    user_input = input("\nVocê: ")
    if user_input.lower() == "sair": break
    
    print(f"Bot: {bot.coordenador(user_input)}")