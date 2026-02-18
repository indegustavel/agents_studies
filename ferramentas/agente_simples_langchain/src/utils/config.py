import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. Carrega as variáveis de ambiente definidas no arquivo .env
# Isso garante que suas chaves de API não fiquem expostas no código principal.
load_dotenv()

def get_llm(model_name: str = "gemini-2.5-flash", temperature: float = 0.5):
    """
    Instancia e configura o modelo de linguagem (LLM).
    
    Args:
        model_name (str): O nome do modelo a ser usado. 
                         'gpt-4o-mini' é excelente para testes pelo custo-benefício.
        temperature (float): Controla a 'criatividade' do modelo. 
    
    Returns:
        ChatOpenAI: Uma instância configurada do modelo pronto para uso.
    """
    
    # Verificamos se a chave de API está presente antes de tentar criar o modelo
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("A variável GEMINI_API_KEY não foi encontrada no arquivo .env")

    # Criamos o objeto do LLM.
    # O LangChain abstrai a chamada da API, facilitando a troca de modelos no futuro.
    llm = ChatGoogleGenerativeAI(
        model=model_name,
        temperature=temperature,
        api_key=api_key
    )
    
    return llm

# Caso queira testar este arquivo isoladamente, descomente as linhas abaixo:
#if __name__ == "__main__":
#    teste_llm = get_llm()
#    print(f"Modelo {teste_llm.model_name} configurado com sucesso!")