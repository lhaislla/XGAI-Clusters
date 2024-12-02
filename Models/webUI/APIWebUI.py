import requests
from dotenv import load_dotenv
import os

load_dotenv()

class APIWebUI:
    def __init__(self):
        self.api_url = os.getenv("URL")
        self.api_key = os.getenv("TOKEN_JWT")
        
    def make_api_request(self, message):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        #print(headers)
        data = {
            "model": "llama3.2:latest",
            #"model": "qwen2.5:latest",
            #"model": "mistral:latest",
            #"model": "deepseek-v2:latest",
            "messages": [{"role": "user", "content": message}]
        }

        
        response = requests.post(f'{self.api_url}/api/chat/completions', headers=headers, json=data)
        #response.raise_for_status()
        return response.json()
        

    def upload_file(self, file_path):
        url = f'{self.api_url}/api/v1/files/'
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Accept': 'application/json'
        }
        
        with open(file_path, 'rb') as file:
            files = {'file': file}
            response = requests.post(url, headers=headers, files=files)
            response.raise_for_status()
            return response.json()
    

    def add_file_to_knowledge(self, knowledge_id, file_id):
        url = f'{self.api_url}/api/v1/knowledge/{knowledge_id}/file/add'
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        data = {'file_id': file_id}
        
        response = requests.post(url, headers=headers, json=data)
        return response.json()
        

if __name__ == "__main__":
    client = APIWebUI()

    response = client.make_api_request("Por que o ceu é azul?")
    if response:
        print(response)
