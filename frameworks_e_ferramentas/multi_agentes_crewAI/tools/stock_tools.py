import yfinance as yf
from crewai.tools import tool
from duckduckgo_search import DDGS 

class StockTools:
    
    @tool
    def fetch_stock_data(ticket: str):
        """
        Esta ferramenta busca preços, indicadores financeiros e estatísticas 
        de uma ação específica. O parâmetro 'ticket' deve ser o símbolo 
        da empresa na bolsa (ex: 'AAPL' para Apple ou 'PETR4.SA' para Petrobras).
        Use esta ferramenta sempre que precisar de dados numéricos e técnicos.
        """
        try:
            # Iniciamos a conexão com o Yahoo Finance
            stock = yf.Ticker(ticket)
            
            # Buscamos o histórico do último mês (preços diários)
            hist = stock.history(period="1mo")
            
            # Buscamos informações fundamentais (P/L, Dividendos, etc)
            info = stock.fast_info
            
            #Adicionar data da última atualização
            last_updated = stock.history(period="1d").index[-1]
            
            # Criamos uma resposta organizada para o agente ler
            return f"""
            Relatório de Dados para {ticket}:
            - Preço Atual: ${info.get('currentPrice', 'N/A')}
            - P/L (Price to Earnings): {info.get('forwardPE', 'N/A')}
            - Dividend Yield: {info.get('dividendYield', 0) * 100:.2f}%
            - Variação Mensal: {((hist['Close'][-1] / hist['Close'][0]) - 1) * 100:.2f}%
            - Resumo do Negócio: {info.get('longBusinessSummary', 'Sem descrição')[:300]}...
            """
        except Exception as e:
            return f"Erro ao coletar dados da ação {ticket}: {e}"

    @tool
    def search_market_news(query: str):
        """
        Busca notícias recentes na internet sobre empresas, setores ou o mercado financeiro.
        O parâmental 'query' deve ser uma busca otimizada (ex: 'últimas notícias PETR4').
        Use esta ferramenta para entender o sentimento do mercado e eventos atuais.
        """
        from datetime import datetime, timedelta
        # Adicionar filtro de data na query
        data_recente = (datetime.now() - timedelta(days=7)).strftime("%d/%m/%Y")
        query_com_filtro = f"{query} after:{data_recente}"

        # DuckDuckGoSearchRun é uma ferramenta pronta que não exige chave de API (grátis!)
        search = DDGS()
        results = search.news(query, max_results=5)
        return str(results)