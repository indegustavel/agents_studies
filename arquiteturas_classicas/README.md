# Arquiteturas de Agentes

Folder destinado aos estudos em arquiteturas

## 1 - Arquitetura Reflexiva

- Arquitetura mais simples dos agentes. Aqui eles tomam decisões puramente baseado no estado atual do ambiente. Não tem memória, não aprendem e são rule-based. Respondem apenas de acordo com o que veem atualmente.

## 2 - Arquitetura Baseada em Modelo

- Aqui, o agente começa a ter uma representação interna do mundo para tomar decisões mais inteligentes baseadas em sua "memória". Ou seja, além de reagir ao que está vendo agora, ele mantém um histórico do que já ocorreu, tornando suas próximas decisões mais acertadas.

## 3 - Arquitetura Híbrida

- A arquitetura híbrida surge para juntar o melhor dos dois mundos: A rapidez da arquitetura reflexiva + a memória da arquitetura baseada em modelo, o objetivo é juntar a rapidez de um e a inteligência de outro para melhorar seus processos. Normalmente, tem 3 camadas: Camada reflexiva (para ações rápidas e críticas), camada deliberativa (para ações estratégicas e "complexas") e camada de coordenação (para orquestrar as duas anteriores e definir ambientes de prioridade.)

## Qual arquitetura escolher?

A resposta que serve para quase todas as perguntas serve para essa: Depende!
É necessário uma análise profunda sobre o escopo do projeto. Deve-se considerar complexidade do ambiente, dados necessários e disponíveis, custos envolvidos, requisitos de latência, etc.