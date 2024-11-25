import requests
import json

class IALlamaModel:
    def __init__(self, temperature=1, max_tokens=8192):
       
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.api_url = "http://localhost:11434/api/generate" 

    def create_model(self, initial_instruction='', model_type="llama2-uncensored"): #Mudar o modelo aqui
    
        self.model_type = model_type
        self.initial_instruction = initial_instruction

    def send_message(self, prompt):
        payload = {
            "model": self.model_type,
            "prompt": prompt,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
        }
        try:
            response = requests.post(self.api_url, json=payload)
            response.raise_for_status()
            return response.json().get("text", "Nenhuma resposta gerada.")
        except requests.exceptions.RequestException as e:
            return f"Erro na API: {e}"
