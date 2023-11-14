import json
import requests
import os


HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
    "OpenAI-Beta": "assistants=v1"
}


def send_post_request(url: str, headers: dict, data: dict):
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(response.text)


def send_get_request(url: str, headers: dict):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(response.text)


def send_delete_request(url: str, headers: dict or None = None):
    response = requests.delete(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(response.text)


class Functions:
    def __init__(self):
        self.functions: dict = dict()

    def __repr__(self):
        return f"<Functions {list(self.functions.keys())}>"

    def __str__(self):
        return f"<Functions {list(self.functions.keys())}>"

    def add_function(self, function: any, description: dict) -> bool:
        self.functions[function.__name__] = function
        self.functions[function.__name__].description = description
        return True

    def remove_function(self, function_name: str) -> bool:
        del self.functions[function_name]
        return True

    def list_functions(self) -> list:
        return list(self.functions.keys())
