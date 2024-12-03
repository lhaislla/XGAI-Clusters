# Projeto: XGAI para Explicação de Clusters em Dados Educacionais 

Este projeto utiliza técnicas de **Explainable Generative AI (XGAI)** para explicar a formação de clusters em dados de Instituições de Ensino Superior (IES), com foco na identificação e compreensão de outliers. O uso de XGAI permite agrupar os dados e gerar explicações sobre os padrões observados.


## Configurações de Ambiente

* Crie um ambiente virtual do python: `python -m venv venv`
* Declare as variaveis de ambiente no arquivo `.env`
* Atualize o pip: `python -m pip install --upgrade pip`
* Atualize as libs: `pip install -r requirements.txt --upgrade`

## Descrição

O objetivo é aplicar modelos generativos que proporcionem insights sobre a estrutura dos clusters e destaquem os fatores que levam determinados pontos de dados a serem considerados outliers.

## Estrutura do Projeto

- **Models/**: Diretório contendo arquivos para a criação das análises de clusters.
  - **Prompts/**: Conjunto de prompts utilizados para interagir com os modelos generativos.
  - **results/**: Resultados gerados.
  - **WebUI**: Diretório da API de execução de outros modelos Generativos (que podem ser alterados no arquivo `APIWebUI.py`). Para execução do projeto, rodar o arquivo `XAI.py`deste diretório.
  - O Arquivo `Xai.py` do diretorio **Models/** executa o projeto utilizando a IA Generativa do Gemini. 

- **data/**: Diretório que contém as bases de dados utilizadas no projeto.
  - **Agglomerative**
  - **K-means**
  - **Base final.csv**

- **Analise resultados XGAI Cluster.ipynb**: Notebook com as metricas de análsie dos resultados.
- **.env**: Arquivo de configuração para variáveis de ambiente necessárias à execução do projeto. O arquivo `env_models.txt` detalha as variaveis de ambiente necessárias. 

- **requirements.txt**: Arquivo que lista as dependências do projeto.

- **README.md**: Documento de apresentação do projeto, incluindo instruções de instalação e execução.

 