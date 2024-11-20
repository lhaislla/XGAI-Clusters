# Projeto: XGAI para Explicação de Clusters em Dados Educacionais 

Este projeto utiliza técnicas de **Explainable Generative AI (XGAI)** para explicar a formação de clusters em dados de Instituições de Ensino Superior (IES), com foco na identificação e compreensão de outliers. O uso de XGAI permite agrupar os dados e gerar explicações sobre os padrões observados.


## Cobnfigurações de Ambiente

* Crie um ambiente virtual do python: `python -m venv venv`
* Atualize o pip: `python -m pip install --upgrade pip`
* Atualize as libs: `pip install -r requirements.txt --upgrade`

## Descrição

O objetivo é aplicar modelos generativos explicáveis que proporcionem insights sobre a estrutura dos clusters e destaquem os fatores que levam determinados pontos de dados a serem considerados outliers.

## Estrutura do Projeto

- **Models/**: Diretório contendo arquivos para a criação das análises de clusters.
  - **Prompts/**: Conjunto de prompts utilizados para interagir com os modelos generativos.
   - **results/**: Resultados gerados.

- **data/**: Diretório que contém as bases de dados utilizadas no projeto.
  - **Agglomerative**
  - **K-means**
  - **Base final.csv**

- **.env**: Arquivo de configuração para variáveis de ambiente necessárias à execução do projeto.

- **requirements.txt**: Arquivo que lista as dependências do projeto.

- **README.md**: Documento de apresentação do projeto, incluindo instruções de instalação e execução.

- **run.py**: Arquivo principal para a execução do projeto.
