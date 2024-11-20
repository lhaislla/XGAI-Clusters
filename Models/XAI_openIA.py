import os
import pandas as pd
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from DefaultConfig import DefaultConfig
from Load_clusters import LoadClusters

api_key = os.getenv("OPENAI_API_KEY")
chat_model = ChatOpenAI(openai_api_key=api_key)

class ClusterXAI_LangChain(DefaultConfig):

    def __init__(self):
        super().__init__()
        loadClusters = LoadClusters()
        self.clusters_path = {
            'K-means': {
                'primeiro': loadClusters.get_path_cluster('K-means', 'Primeiro agrupamento (K-means).csv'),
                'segundo': loadClusters.get_path_cluster('K-means', 'Segundo agrupamento (K-means).csv'),
                'terceiro': loadClusters.get_path_cluster('K-means', 'Terceiro agrupamento (K-means).csv'),
                'quarto': loadClusters.get_path_cluster('K-means', 'Quarto agrupamento (K-means).csv'),
                'quinto': loadClusters.get_path_cluster('K-means', 'Quinto agrupamento (K-means).csv'),
                'sexto': loadClusters.get_path_cluster('K-means', 'Sexto agrupamento (K-means).csv'),
                'setimo': loadClusters.get_path_cluster('K-means', 'Sétimo agrupamento (K-means).csv'),
            },
            'Agglomerative': {
                'primeiro': loadClusters.get_path_cluster('Agglomerative', 'Primeiro agrupamento (Agglomerative).csv'),
                'segundo': loadClusters.get_path_cluster('Agglomerative', 'Segundo agrupamento (Agglomerative).csv'),
                'terceiro': loadClusters.get_path_cluster('Agglomerative', 'Terceiro agrupamento (Agglomerative).csv'),
                'quarto': loadClusters.get_path_cluster('Agglomerative', 'Quarto agrupamento (Agglomerative).csv'),
                'quinto': loadClusters.get_path_cluster('Agglomerative', 'Quinto agrupamento (Agglomerative).csv'),
            }
        }
        self.chat_model = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

    def create_instruction(self, prompt_file):
        with open(os.path.join("./Prompts", prompt_file), 'r', encoding='utf-8') as file:
            linhas = "".join(file.readlines())
        return linhas

    def process_cluster(self, cluster_type, alias, path, prompt_file, temperatures):
        prompt = self.create_instruction(prompt_file)

        
        try:
            df = pd.read_csv(path, sep=',')  
        except pd.errors.ParserError:
            try:
                df = pd.read_csv(path, sep=';') 
            except pd.errors.ParserError:
                print(f"Erro ao ler o arquivo CSV: {path}. Verifique o delimitador.")
                return None

       
        file_content = df.to_csv(index=False) 

       
        results = pd.DataFrame([], columns=['algorithm', 'cluster', 'temperature', 'prompt', 'result'])

        for temperature in temperatures:
            print(alias, temperature)
            
            prompt_template = PromptTemplate(input_variables=["file_content"], template=prompt)
            chain = LLMChain(llm=self.chat_model, prompt=prompt_template)

            response = chain.run(file_content=file_content)
           
            self.add_item_to_dataframe(results, [cluster_type, alias, temperature, prompt_file, response])

        return results


def main(prompt_file='Fase 1 - Direto.txt', cluster_type="K-means"):

    if cluster_type not in ["K-means", 'Agglomerative']:
        raise Exception('Algoritmo não mapeado')
    
    if not os.path.isdir(os.path.join(os.getcwd(), "results")):
        os.makedirs(os.path.join(os.getcwd(), "results"))

    model = ClusterXAI_LangChain()

    cluster_paths = model.clusters_path[cluster_type].items()

    for alias, path in cluster_paths:
        print(alias, path)
        temperatures = [0, 0.5, 1, 1.5, 2]

        results = model.process_cluster(cluster_type, alias, path, prompt_file, temperatures)

       
        results.to_csv(os.path.join(os.getcwd(), "results", f"{cluster_type}_{prompt_file.split(' - ')[0]}_results.csv"), index=False)


if __name__ == "__main__":
    main('Fase 1 - Direto.txt', 'Agglomerative')
    main('Fase 2 - Cadeia de pensamento.txt', 'K-means')
    main('Fase 2 - Cadeia de pensamento.txt', 'Agglomerative')
    main('Fase 3 - Descrição.txt', 'K-means')
    main('Fase 3 - Descrição.txt', 'Agglomerative')
    main('Fase 4 - Com modelo.txt', 'K-means')
    main('Fase 4 - Com modelo.txt', 'Agglomerative')
