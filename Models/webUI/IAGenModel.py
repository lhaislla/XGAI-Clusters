import requests
from APIWebUI import APIWebUI

class IAGenModel:

    def __init__(self, temperature=1):
        self.temperature = temperature
        self.api_client = APIWebUI()
        
    def create_model(self, message):
        try:
            response = self.api_client.make_api_request(message)
            return response
        except Exception as e:
            print(f"Erro ao criar o modelo: {str(e)}")
            return None
