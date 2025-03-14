DOCUMENTAÇÃO DO PROJETO DE ANÁLISE DE ÓBITOS E INDICADORES SOCIOECONÔMICOS

INTRODUÇÃO

Este projeto tem como objetivo analisar a relação entre condições socioeconômicas e óbitos, considerando indicadores como o Índice de Vulnerabilidade Social (IVS) e o Índice de Equidade e Dimensionamento (IED).

ESTRUTURA DO PROJETO
Semana 1: Planejamento e Estruturação do Projeto, definição dos objetivos do projeto e fontes de dados:

          1.1.	Webscrapping de dados de saúde (Processo utilizando alguma das bibliotecas ministradas no curso).
          1.2.	Projeto no GitHub (Com documentação e README).
          1.3.	Desenvolvimento de um pipeline, detalhando as etapas envolvidas desde o webscrapping até a entrega de uma base pronta para análise (ferramentas, sistema, linguagem utilizados). Pode ser em formato de texto usando fluxo de tarefas, com imagens usando um fluxograma e texto para complementar com descrição de cada tarefa.
          1.4.	Manipulação de dados e transformação (avaliados através de scripts de manipulação usando técnicas similares as ministradas em aula).
          1.5.	Agregação de dados e junção (merge) de bases de dados (também avaliado através dos scripts).
          1.6.	Descritiva simples de pelo menos 10 variáveis da base final (se for numérica, avaliar média, mediana e fazer um boxplot, se for categórica mostrar percentuais de preenchimento em cada categoria, se for data, avaliar mínimo e máximo).
          1.7.	Entregar um dicionário das principais variáveis na base de dados (entre 10-15 variáveis) contendo o nome da variável, uma descrição breve, o tipo, e a completude na base de dados.
          1.8.	Levantamento das bibliotecas necessárias (ex: requests, BeautifulSoup, pandas, numpy, matplotlib, seaborn, scikit-learn, stats). Em sua maioria as bibliotecas, serão utilizadas para ajustes, leitura e interpretação, assim como criação de gráficos.
          1.9.	Definição do pipeline geral do projeto, coletando informações sobre: Sobre óbito, se o evento está relacionado ao processo de trabalho, se houve correção ou alteração da causa do óbito após investigação;
          1.10.	O (s) CID (s) informados no atestado de óbito, a causa básica da declaração do óbito (CID 10);
          1.11.	O código do município de residência, a data de nascimento e data de óbito;
          1.12.	Também tem interesse em saber o nível de escolaridade do indivíduo e escolaridade da mãe (se disponível);
          1.13.	E informações sobre raça/cor do indivíduo;
          1.14.	E para informações socioeconômicas queremos os valores de IED e IVS, além do número de habitantes e a faixa de porte populacional segundo o IBGE;
          1.15.	Criação de repositório no GitHub com documentação inicial (README).

Semana 2: Coleta de Dados via Web Scraping

          2.1.	Implementação da coleta de dados de saúde usando bibliotecas como BeautifulSoup, Selenium fazendo webscraping da página através do link https://www.in.gov.br/en/web/dou/-/portaria-gm/ms-n-3.493-de-10-de-abril-de-2024-553573811.          
          2.2.	Extração de dados.          
          2.3.	Óbitos e causas (CID-10).          
          2.4.	Relação com o trabalho          
          2.5.	Correção de causa          
          2.6.	Informações demográficas (município, escolaridade, raça/cor)          
          2.7.	Testes e validação da integridade dos dados coletados.
          
Semana 3: Obtenção de Dados Socioeconômicos

          3.1.	Coleta dos valores de IED e IVS por município.          
          3.2.	Obtenção do número de habitantes e faixa de porte populacional segundo o IBGE.
          3.3.	Limpeza e padronização dos dados.
          
Semana 4: Construção do Pipeline de Processamento

          4.1.	Definição do fluxo de tarefas: 
          4.2.	Coleta via web scraping
          4.3.	Tratamento de dados ausentes
          4.4.	Conversão de tipos de variáveis
          4.5.	Padronização e junção das bases
          4.6.	Geração da base final para análise
          4.7.	Elaboração de um fluxograma ilustrando as etapas do pipeline.
          
Semana 5: Manipulação e Transformação dos Dados

          5.1.	Criação de scripts para limpeza e padronização dos dados utilizando pandas.
          5.2.	Tratamento de valores nulos, conversão de datas e normalização de categorias.
          
Semana 6: Agregação e Junção das Bases de Dados

          6.1.	Uso de merge e joins para consolidar as informações.
          6.2.	Criação de chaves de ligação entre bases (ex: código do município).
          6.3.	Validação da integridade da base final.
          
Semana 7: Análise Descritiva das Variáveis

          7.1.	Análise de pelo menos 10 variáveis principais: 
          7.2.	Variáveis numéricas: cálculo de média, mediana, geração de boxplots.
          7.3.	Variáveis categóricas: cálculo de percentuais de cada categoria.
          7.4.	Variáveis de data: avaliação de mínimo e máximo.

Semana 8: Documentação e Entrega Final

          8.1.	Criação de um dicionário de variáveis contendo: 
          8.2.	Nome da variável
          8.3.	Descrição breve
          8.4.	Tipo de dado
          8.5.	Completude na base de dados
          8.6.	Melhoria do README do repositório do GitHub.
          8.7.	Organização e documentação dos scripts.
          8.8.	Submissão final do projeto para revisão.

Tecnologias Utilizadas
Linguagem: Python 3.11.7/Vscode
Bibliotecas: pandas, numpy, matplotlib, seaborn, requests, BeautifulSoup, Scrapy, selenium
Ferramentas: Jupyter Notebook, [GitHub](https://github.com/Macedosouza2024/Engenharia-de-dados)
