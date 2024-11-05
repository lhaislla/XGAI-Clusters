import os
from dotenv import load_dotenv, find_dotenv
import google.generativeai as gemini
import pandas as pd

class DefaultConfig:

    def __init__(self):
        self.data_directory = "./data"
        self.result_dataframe = self.load_data_file("dado.xlsx") #Substituir o nome do arquivo dado.xlsx pelo nome do arquivo que deseja carregar
        self.GEMINI_KEY = self.load_key()

    def load_key(self):
        load_dotenv(find_dotenv())
        chave = os.getenv("GOOGLE_API_KEY")
        gemini.configure(api_key=chave)
        print("Chave reconhecida com sucesso!")
        return chave

    def load_data_file(self, filename):
        file_path = os.path.join(self.data_directory, filename)
        return pd.read_excel(file_path)

    def create_column_reference_dataframe(self, new_column):
        self.result_dataframe[new_column] = None

    def update_value_reference_dataframe(self, index, column, value):
        self.result_dataframe.loc[index, column] = value

    def add_item_to_dataframe(self, values):
        self.result_dataframe = self.result_dataframe.append(values, ignore_index=True)

    def result_to_dataframe(self, string_result):
        rows = string_result.strip().split("\n")
        columns = rows[0].split(";")
        rows_csv = [row.split(";") for row in rows[1:]]
        return pd.DataFrame(rows_csv, columns=columns)

