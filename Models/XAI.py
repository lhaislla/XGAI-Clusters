import os
from DefaultConfig import DefaultConfig
from LoadFile import LoadFile
import pandas as pd

from Load_clusters import LoadClusters
from IAGenModel import IAGenModel

class ClusterXAI(DefaultConfig):

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

    
    def create_instruction(self,prompt_file):
        with open(os.path.join("./Prompts", prompt_file), 'r', encoding='utf-8') as file:
            linhas = "".join(file.readlines())
        return linhas
    


def main(prompt_file='Fase 1 - Direto.txt', cluster_type="K-means"):

    if (cluster_type not in ["K-means", 'Agglomerative']):
        raise Exception('Algoritmo não mapeado')
    
    if (not os.path.isdir(os.path.join(os.getcwd(), "results"))):
        os.makedirs(os.path.join(os.getcwd(), "results"))

    model = ClusterXAI()

    cluster_paths = model.clusters_path[cluster_type].items()

    results = pd.DataFrame([], columns=['algorithm', 'cluster', 'temperature', 'prompt', 'result'])

    for alias, path in cluster_paths:
        print(alias,path)
        file_gemini = model.load_image_to_gemini(path)
    
        prompt = model.create_instruction(prompt_file)

        LoadFile.wait_for_files_active([file_gemini])

        temperatures = [
            0, 
            0.5, 
            1 , 
            1.5, 
            2
        ]

        for temperature in temperatures:
            print(alias, temperature)

            ia_gen_model = IAGenModel(temperature=temperature)

            ia_gen_model.create_model(initial_instruction=prompt)

            chat_session = ia_gen_model.model.start_chat( history=[] )

            response = chat_session.send_message(file_gemini)

            model.add_item_to_dataframe(results, [cluster_type, alias, temperature, prompt_file, response.text])
            
    results.to_csv(os.path.join(os.getcwd(), "results", f"{cluster_type}_{prompt_file.split(" - ")[0]}_results.csv"), index=False)



import sys
if __name__ == "__main__":

    #main('Fase 1 - Direto.txt', 'K-means')
    main('Fase 1 - Direto.txt', 'Agglomerative')
    main('Fase 2 - Cadeia de pensamento.txt', 'K-means')
    main('Fase 2 - Cadeia de pensamento.txt', 'Agglomerative')
    main('Fase 3 - Descrição.txt', 'K-means')
    main('Fase 3 - Descrição.txt', 'Agglomerative')
    main('Fase 4 - Com modelo.txt', 'K-means')
    main('Fase 4 - Com modelo.txt', 'Agglomerative')