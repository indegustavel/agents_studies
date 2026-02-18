# helper para formatar a reposta do agente, independente do que ele retornar.

def formatar_resposta_agente(raw_output) -> str:
    """
    Limpa a resposta do agente, lidando com listas, dicionários
    ou strings puras, garantindo que o retorno seja sempre texto legível.
    """
    texto_final = ""
    
    # Caso 1: A resposta é uma lista (comum em novas versões do LangChain/OpenAI)
    if isinstance(raw_output, list):
        for item in raw_output:
            if isinstance(item, dict):
                # Tenta pegar 'text', se não tiver, pega 'content', se não, ignora
                texto_final += item.get("text", item.get("content", ""))
            elif isinstance(item, str):
                texto_final += item
                
    # Caso 2: A resposta é um dicionário isolado
    elif isinstance(raw_output, dict):
        texto_final = raw_output.get("text", raw_output.get("content", str(raw_output)))
        
    # Caso 3: A resposta já é uma string
    else:
        texto_final = str(raw_output)
        
    # Limpeza final de espaços extras
    return texto_final.strip()