import os
from langchain_openrouter import ChatOpenRouter

def get_llm(model_name: str = None, temperature: float = 0.2):
    """
    Retorna uma instância configurada do LLM da OpenRouter.
    
    Args:
        model_name (str): Nome do modelo. Se None, usa o modelo padrão.
        temperature (float): Controla a criatividade do modelo (0.0 a 1.0).
    
    Returns:
        ChatOpenRouter: Instância configurada do modelo.
    
    Modelos gratuitos disponíveis na OpenRouter (Fevereiro 2026):
        - meta-llama/llama-3.2-3b-instruct:free (Padrão - Rápido e eficiente)
        - deepseek/deepseek-chat-v3-0324:free (Bom para código)
        - google/gemini-flash-1.5:free (Rápido, boa qualidade)
        - meta-llama/llama-4-maverick:free (Mais recente, se disponível)
    
    Nota: Modelos gratuitos podem ter limitações de rate limit.
    Para produção, considere usar modelos pagos.
    """
    
    # Modelo padrão
    if model_name is None:
        model_name = "arcee-ai/trinity-large-preview:free"
    
    # Verifica se a API key está configurada
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENROUTER_API_KEY não encontrada no arquivo .env. "
            "Por favor, configure sua chave de API da OpenRouter."
        )
    
    # Cria e retorna a instância do LLM
    llm = ChatOpenRouter(
        model=model_name,
        base_url="https://openrouter.ai/api/v1",
        temperature=temperature,
        api_key=api_key
    )
    
    return llm

