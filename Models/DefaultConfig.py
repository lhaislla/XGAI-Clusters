import os
from dotenv import load_dotenv, find_dotenv
import google.generativeai as gemini
import pandas as pd
from LoadFile import LoadFile

class DefaultConfig:

    def __init__(self):
        self.GEMINI_KEY = self.load_key()
        self.data_directory = os.getenv("ROOT_PATH_PROJECT") + "\\data"

    def load_key(self):
        load_dotenv(find_dotenv())
        chave = os.getenv("GOOGLE_API_KEY")
        gemini.configure(api_key=chave)
        print("Chave reconhecida com sucesso!")
        return chave

    def load_data_file(self, filename):
        file_path = os.path.join(self.data_directory, filename)
        return pd.read_excel(file_path)
    
    def load_image_to_gemini(self, path):
        """Função para dar upload dos dados no gemini"""
        file_gemini = LoadFile.upload_file_to_gemini(path)

        return file_gemini

    def create_column_reference_dataframe(self, dataframe, new_column):
        dataframe[new_column] = None

    def update_value_reference_dataframe(self, dataframe, index, column, value):
        dataframe.loc[index, column] = value

    def add_item_to_dataframe(self, dataframe, values):
        dataframe.loc[len(dataframe)] = values

    def result_to_dataframe(self, string_result):
        rows = string_result.strip().split("\n")
        columns = rows[0].split(";")
        rows_csv = [row.split(";") for row in rows[1:]]
        return pd.DataFrame(rows_csv, columns=columns)

