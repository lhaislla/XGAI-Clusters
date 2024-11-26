import os
import pandas as pd
from ClusterXAI import ClusterXAI
from IALlamaModel import IALlamaModel


def main(prompt_file='Fase 1 - Direto.txt', cluster_type="K-means"):
    if cluster_type not in ["K-means", "Agglomerative"]:
        raise Exception("Algoritmo não mapeado")

    if not os.path.isdir(os.path.join(os.getcwd(), "results")):
        os.makedirs(os.path.join(os.getcwd(), "results"))

    model = ClusterXAI()
    cluster_paths = model.clusters_path[cluster_type].items()

    results = pd.DataFrame([], columns=["algorithm", "cluster", "temperature", "prompt", "result"])

    for alias, path in cluster_paths:
        print(f"Processando cluster: {alias}, caminho: {path}")
        
       
        prompt = model.create_instruction(prompt_file)

       
        temperatures = [0, 0.5, 1, 1.5, 2]

        for temperature in temperatures:
            print(f"Usando temperatura: {temperature}")

            ia_gen_model = IALlamaModel(temperature=temperature)
            ia_gen_model.create_model(initial_instruction=prompt)

          
            response_text = ia_gen_model.send_message(prompt)
            print(f"Resposta obtida: {response_text}")

          
            model.add_item_to_dataframe(results, [cluster_type, alias, temperature, prompt_file, response_text])
            
    results.to_csv(
        os.path.join(os.getcwd(), "results", f"{cluster_type}_{prompt_file.split(' - ')[0]}_results.csv"),
        index=False
    )

if __name__ == "__main__":
    main("Fase 1 - Direto.txt", "K-means")
    main('Fase 1 - Direto.txt', 'Agglomerative')
    main('Fase 2 - Cadeia de pensamento.txt', 'K-means')
    main('Fase 2 - Cadeia de pensamento.txt', 'Agglomerative')
    main('Fase 3 - Descrição.txt', 'K-means')
    main('Fase 3 - Descrição.txt', 'Agglomerative')
    main('Fase 4 - Com modelo.txt', 'K-means')
    main('Fase 4 - Com modelo.txt', 'Agglomerative')
        