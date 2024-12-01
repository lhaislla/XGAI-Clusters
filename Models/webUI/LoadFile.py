from APIWebUI import APIWebUI

class LoadFile:

    def __init__(self):
        self.api_client = APIWebUI()

    def upload_file_to_webui(self, file_path):
        """
        Faz o upload de um arquivo para o WebUI.
        """
        try:
            response = self.api_client.upload_file(file_path)
            print(f"Arquivo '{file_path}' carregado com sucesso: {response['file_id']}")
            return response
        except Exception as e:
            print(f"Erro ao carregar o arquivo {file_path}: {e}")
            return None

    def add_file_to_knowledge(self, knowledge_id, file_id):
        """
        Adiciona um arquivo ao conhecimento no WebUI.
        """
        try:
            response = self.api_client.add_file_to_knowledge(knowledge_id, file_id)
            print(f"Arquivo {file_id} adicionado ao conhecimento {knowledge_id}: {response}")
            return response
        except Exception as e:
            print(f"Erro ao adicionar o arquivo ao conhecimento: {e}")
            return None
