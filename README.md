DOCUMENTAÇÃO DO PROJETO DE ANÁLISE DE ÓBITOS E INDICADORES SOCIOECONÔMICOS
INTRODUÇÃO
Este projeto tem como objetivo analisar a relação entre condições socioeconômicas e óbitos, considerando indicadores como o Índice de Vulnerabilidade Social (IVS) e o Índice de Equidade e Dimensionamento (IED).
ESTRUTURA DO PROJETO
Semana 1: Planejamento e Estruturação do Projeto
Definição dos objetivos do projeto e fontes de dados.
1.1.	Webscrapping de dados de saúde (Processo utilizando alguma das bibliotecas ministradas no curso).
1.2.	Projeto no GitHub (Com documentação e README).
1.3.	Desenvolvimento de um pipeline, detalhando as etapas envolvidas desde o webscrapping até a entrega de uma base pronta para análise (ferramentas, sistema, linguagem utilizados). Pode ser em formato de texto usando fluxo de tarefas, com imagens usando um fluxograma e texto para complementar com descrição de cada tarefa.
1.4.	Manipulação de dados e transformação (avaliados através de scripts de manipulação usando técnicas similares as ministradas em aula).
1.5.	Agregação de dados e junção (merge) de bases de dados (também avaliado através dos scripts).
1.6.	Descritiva simples de pelo menos 10 variáveis da base final (se for numérica, avaliar média, 
1.7.	Mediana e fazer um boxplot, se for categórica mostrar percentuais de preenchimento em cada categoria, se for data, avaliar mínimo e máximo).
1.8.	Entregar um dicionário das principais variáveis na base de dados (entre 10-15 variáveis)
1.9.	Contendo o nome da variável, uma descrição breve, o tipo, e a completude na base de dados.
1.10.	Levantamento das bibliotecas necessárias (ex: requests, BeautifulSoup, pandas, numpy, matplotlib, seaborn, scikit-learn, stats). Em sua maioria as bibliotecas, serão utilizadas para ajustes, leitura e interpretação, assim como criação de gráficos.
1.11.	Definição do pipeline geral do projeto, coletando informações sobre:
1.12.	Sobre óbito;
1.13.	Se o evento está relacionado ao processo de trabalho;
1.14.	Se houve correção ou alteração da causa do óbito após investigação;
1.15.	O (s) CID (s) informados no atestado de óbito, a causa básica da declaração do óbito (CID 10);
1.16.	O código do município de residência, a data de nascimento e data de óbito;
1.17.	Também tem interesse em saber o nível de escolaridade do indivíduo e escolaridade da mãe (se disponível);
1.18.	E informações sobre raça/cor do indivíduo.
1.19.	E para informações socioeconômicas queremos os valores de IED e IVS, além do número de habitantes e a faixa de porte populacional segundo o IBGE.
1.20.	Criação de repositório no GitHub com documentação inicial (README).
Semana 2: Coleta de Dados via Web Scraping
2.1	Implementação da coleta de dados de saúde usando bibliotecas como BeautifulSoup, Selenium fazendo webscraping da página através do link https://www.in.gov.br/en/web/dou/-/portaria-gm/ms-n-3.493-de-10-de-abril-de-2024-553573811.
2.2	Extração de dados:
2.3	Óbitos e causas (CID-10)
2.4	Relação com o trabalho
2.5	Correção de causa
2.6	Informações demográficas (município, escolaridade, raça/cor)
2.7	Testes e validação da integridade dos dados coletados.
Semana 3: Obtenção de Dados Socioeconômicos
3.1	Coleta dos valores de IED e IVS por município.
3.2	Obtenção do número de habitantes e faixa de porte populacional segundo o IBGE.
3.3	Limpeza e padronização dos dados.
Semana 4: Construção do Pipeline de Processamento
•	Definição do fluxo de tarefas: 
o	Coleta via web scraping
o	Tratamento de dados ausentes
o	Conversão de tipos de variáveis
o	Padronização e junção das bases
o	Geração da base final para análise
•	Elaboração de um fluxograma ilustrando as etapas do pipeline.
Semana 5: Manipulação e Transformação dos Dados
•	Criação de scripts para limpeza e padronização dos dados utilizando pandas.
•	Tratamento de valores nulos, conversão de datas e normalização de categorias.
Semana 6: Agregação e Junção das Bases de Dados
•	Uso de merge e joins para consolidar as informações.
•	Criação de chaves de ligação entre bases (ex: código do município).
•	Validação da integridade da base final.
Semana 7: Análise Descritiva das Variáveis
•	Análise de pelo menos 10 variáveis principais: 
o	Variáveis numéricas: cálculo de média, mediana, geração de boxplots.
o	Variáveis categóricas: cálculo de percentuais de cada categoria.
o	Variáveis de data: avaliação de mínimo e máximo.
Semana 8: Documentação e Entrega Final
•	Criação de um dicionário de variáveis contendo: 
o	Nome da variável
o	Descrição breve
o	Tipo de dado
o	Completude na base de dados
•	Melhoria do README do repositório do GitHub.
•	Organização e documentação dos scripts.
•	Submissão final do projeto para revisão.
Tecnologias Utilizadas
•	Linguagem: Python
•	Bibliotecas: pandas, numpy, matplotlib, seaborn, requests, BeautifulSoup, Scrapy
•	Ferramentas: Jupyter Notebook, GitHub
