from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from tools import StockTools # Importa as ferramentas que criamos no passo anterior
from datetime import datetime

@CrewBase
class StockAnalystCrew():
    """
    Esta classe organiza a lógica da nossa equipe de analistas.
    O decorador @CrewBase faz o trabalho 'sujo' de carregar os arquivos 
    YAML e preparar tudo para nós automaticamente.
    """

    # 1. Indicamos onde estão os arquivos de texto com as definições
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # Criamos um objeto de configuração da LLM
    # Aqui você tem controle total sobre o modelo e a 'criatividade' (temperature)
    main_llm = LLM(
        model="openrouter/z-ai/glm-4.5-air:free", 
        base_url="https://openrouter.ai/api/v1",
        temperature=0.2,
        # Você pode até forçar o idioma aqui se o modelo insistir em inglês
        extra_headers={"language": "pt-br"}
    )

    # --- Definição dos Agentes ---

    @agent
    def researcher(self) -> Agent:
        """
        Cria o Agente Pesquisador. 
        self.agents_config['researcher'] busca as instruções no YAML.
        """
        return Agent(
            config=self.agents_config['researcher'],
            tools=[StockTools.fetch_stock_data], # Damos a 'ferramenta' de dados técnicos para ele
            verbose=True, # Permite que você veja o agente 'pensando' no terminal
            allow_delegation=False, # Ele foca apenas na sua tarefa, sem pedir ajuda
            llm=self.main_llm
        )

    @agent
    def news_analyst(self) -> Agent:
        """Cria o Analista de Notícias."""
        return Agent(
            config=self.agents_config['news_analyst'],
            tools=[StockTools.search_market_news], # Este agente pode usar a busca na internet
            verbose=True,
            llm=self.main_llm
        )

    @agent
    def investment_advisor(self) -> Agent:
        """Cria o Consultor Final (O Tomador de Decisão)."""
        return Agent(
            config=self.agents_config['investment_advisor'],
            verbose=True,
            llm=self.main_llm
            # Note: Ele não precisa de ferramentas, ele usa a lógica da LLM
        )
    
    @agent
    def validator(self) -> Agent:
        """Cria o agente validador"""
        return Agent(
            config=self.agents_config['validator'],
            verbose=True,
            llm=self.main_llm
        )

    # --- Definição das Tarefas ---

    @task
    def research_task(self) -> Task:
        """Tarefa de coleta de dados técnicos."""
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def news_analysis_task(self) -> Task:
        """Tarefa de análise de notícias e sentimento."""
        return Task(
            config=self.tasks_config['news_analysis_task'],
        )

    @task
    def recommendation_task(self) -> Task:
        """Tarefa final de compilação do relatório."""
        data = datetime.now().strftime("%m-%d")
        return Task(
            config=self.tasks_config['recommendation_task'],
            output_file='relatorio_final_{data}.md' # O resultado final será gravado neste arquivo
        )
    
    @task
    def validation_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['validation_research_task']
        )
        
    @task
    def validation_news_task(self) -> Task:
        return Task(
            config=self.tasks_config['validation_news_task']
        )

    # --- O Processo (A Equipe) ---

    @crew
    def crew(self) -> Crew:
        """
        Aqui é onde juntamos os agentes e as tarefas em uma 'Equipe' (Crew).
        O CrewAI gerencia como eles interagem.
        """
        return Crew(
            agents=self.agents, # Lista de agentes criados acima
            tasks=[
                self.research_task(),                   # 1º - Researcher executa
                self.validation_research_task(),        # 2º - Validator revisa pesquisas
                self.news_analysis_task(),              # 3º - News Analyst executa
                self.validation_news_task(),            # 4º - Validator revisa notícias
                self.recommendation_task()              # 5º - Investment Advisor finaliza
                ],   # Lista de tarefas criadas acima
            process=Process.sequential, # Processo Linear: Agente 1 -> Agente 2 -> Agente 3 -> Agente 4
            verbose=True,
        )