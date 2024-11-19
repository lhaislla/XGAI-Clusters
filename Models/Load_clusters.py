# Load_clusters.py

import pandas as pd
from DefaultConfig import DefaultConfig

class LoadClusters:
    
    def __init__(self):
        self.config = DefaultConfig()
        self.clusters = None
     
    def load_clusters(self, type_algorithm, cluster_file):
        """
        Carrega os dados de clusters a partir de um arquivo específico.
        """
        cluster_path = self.get_path_cluster(type_algorithm, cluster_file)
        self.clusters = pd.read_csv(cluster_path)
        print("Clusters carregados com sucesso!")
        return self.clusters
    
    def get_path_cluster(self, type_algorithm, cluster_file):
        return f"{self.config.data_directory}/{type_algorithm}/{cluster_file}"
    
    def analyze_clusters(self):
        """
        Analisa os clusters carregados e identifica características principais.
        """
        if self.clusters is None:
            print("Nenhum cluster carregado. Carregue os clusters primeiro.")
            return
        

        cluster_summary = self.clusters.describe()
        print("Resumo dos clusters:")
        print(cluster_summary)
        
        self.identify_outliers()   # Análises para identificação de outliers
        
    def identify_outliers(self):
        """
        Identifica e analisa outliers nos clusters.
        """
       
        for column in self.clusters.select_dtypes(include=['float64', 'int64']).columns:
            mean = self.clusters[column].mean()
            std_dev = self.clusters[column].std()
            outlier_condition = (self.clusters[column] < mean - 3 * std_dev) | (self.clusters[column] > mean + 3 * std_dev)
            outliers = self.clusters[outlier_condition]
            print(f"Outliers na coluna '{column}':")
            print(outliers)

if __name__ == "__main__":
    loader = LoadClusters()
    loader.load_clusters("clusters_data.xlsx")  # Substituir pelo nome do arquivo de clusters
    loader.analyze_clusters()
