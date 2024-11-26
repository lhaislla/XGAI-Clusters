import os
from DefaultConfig import DefaultConfig
from Load_clusters import LoadClusters
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

    def create_instruction(self, prompt_file):
       
        with open(os.path.join("./Prompts", prompt_file), 'r', encoding='utf-8') as file:
            linhas = "".join(file.readlines())
        return linhas
