import os
import time
from APIWebUI import APIWebUI

class LoadFile:

    def __init__(self):
        self.api_client = APIWebUI()  

    def upload_file_to_webui(self, file_path):
        try:
            
            file_info = self.api_client.upload_file(file_path) 
            print(f"Arquivo {file_path} enviado com sucesso!")
            return file_info
        except Exception as e:
            print(f"Erro ao dar upload no arquivo {file_path}: {e}")
            return None

    @staticmethod
    def wait_for_files_active(file_info):
        file_id = file_info.get('file_id')
        print(f"Aguardando ativação do arquivo {file_id}")
        
        while True:
            status = file_info.get('status', 'inactive')
            if status == 'active':
                break
            time.sleep(5)
        print("Arquivo ativado.")
