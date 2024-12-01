from APIWebUI import APIWebUI

class IAGenModel:

    def __init__(self, temperature=1):
        self.api_client = APIWebUI()
        self.temperature = temperature

    def create_model(self, message):
        """
        Faz uma requisição para a API do WebUI para gerar uma resposta baseada no prompt.
        """
        response = self.api_client.make_api_request(message)
        return response
