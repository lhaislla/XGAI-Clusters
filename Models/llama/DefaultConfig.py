import os
import pandas as pd
from LoadFile import LoadFile

class DefaultConfig:
    def __init__(self):
       
        self.data_directory = os.getenv("ROOT_PATH_PROJECT") + "\\data"
        self.api_url = "http://localhost:11434/api/generate"  # Endpoint para o Llama 3.2

    def load_data_file(self, filename):
       
        file_path = os.path.join(self.data_directory, filename)
        return pd.read_excel(file_path)

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
