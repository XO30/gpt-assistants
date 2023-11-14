from .utils import send_get_request, send_post_request, send_delete_request
from .utils import HEADERS
from .utils import Functions


def list_assistants():
    url = "https://api.openai.com/v1/assistants?order=desc&limit=20"
    response = send_get_request(url, HEADERS)
    return [Assistant(**assistant) for assistant in response["data"]]


def retrieve_assistant(assistant_id: str):
    url = f"https://api.openai.com/v1/assistants/{assistant_id}"
    response = send_get_request(url, HEADERS)
    return Assistant(**response)


def delete_assistant(assistant_id: str):
    url = f"https://api.openai.com/v1/assistants/{assistant_id}"
    send_delete_request(url, HEADERS)
    return True


def create_assistant(
        model: str,
        name: str or None = None,
        description: str or None = None,
        instructions: str or None = None,
        code_interpreter: bool = False,
        retrieval: bool = False,
        functions: Functions or None = None,
        file_ids: list or None = None,
        metadata: dict or None = None
):
    if not name:
        name = str()
    if not description:
        description = str()
    if not instructions:
        instructions = str()
    if not file_ids:
        file_ids = list()
    if not metadata:
        metadata = dict()
    if not functions:
        functions = list()

    tools = []
    if code_interpreter:
        tools.append({"type": "code_interpreter"})
    if retrieval:
        tools.append({"type": "retrieval"})
    if functions and isinstance(functions, Functions):
        for func in functions.functions.values():
            tools.append(func.description)

    url = "https://api.openai.com/v1/assistants"

    data = {
        "instructions": instructions,
        "name": name,
        "description": description,
        "tools": tools,
        "model": model,
        "file_ids": file_ids,
        "metadata": metadata
    }

    response = send_post_request(url, HEADERS, data)
    return Assistant(**response)


def update_assistant(
        assistant_id: str,
        model: str or None = None,
        name: str or None = None,
        description: str or None = None,
        instructions: str or None = None,
        code_interpreter: bool or None = None,
        retrieval: bool or None = None,
        functions: Functions or None = None,
        file_ids: list or None = None,
        metadata: dict or None = None
):
    assistant = retrieve_assistant(assistant_id)

    if not name:
        name = assistant.name
    if not description:
        description = assistant.description
    if not instructions:
        instructions = assistant.instructions
    if not file_ids:
        file_ids = assistant.file_ids
    if not metadata:
        metadata = assistant.metadata
    if not functions:
        functions = [tool for tool in assistant.tools if tool["type"] == "function"]
    else:
        functions = [func.description for func in functions.functions.values()]
    if not model:
        model = assistant.model
    if code_interpreter is None:
        code_interpreter = True if {"type": "code_interpreter"} in assistant.tools else False
    if retrieval is None:
        retrieval = True if {"type": "retrieval"} in assistant.tools else False

    tools = []
    if code_interpreter:
        tools.append({"type": "code_interpreter"})
    if retrieval:
        tools.append({"type": "retrieval"})
    if functions:
        for func in functions:
            tools.append(func)

    url = f"https://api.openai.com/v1/assistants/{assistant_id}"

    data = {
        "instructions": instructions,
        "name": name,
        "description": description,
        "tools": tools,
        "model": model,
        "file_ids": file_ids,
        "metadata": metadata
    }

    response = send_post_request(url, HEADERS, data)
    return Assistant(**response)


class Assistant:
    def __init__(self,
                 id: str,
                 object: str,
                 created_at: int,
                 name: str,
                 description: str,
                 model: str,
                 instructions: str,
                 tools: list,
                 file_ids: list,
                 metadata: dict,
                 ):
        self.id = id
        self.object = object
        self.created_at = created_at
        self.name = name
        self.description = description
        self.model = model
        self.instructions = instructions
        self.tools = tools
        self.file_ids = file_ids
        self.metadata = metadata

    def __repr__(self):
        return f"<Assistant {self.name}, id: {self.id}>"

    def __str__(self):
        return f"<Assistant {self.name}, id: {self.id}>"

    def info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Object: {self.object}")
        print(f"Created at: {self.created_at}")
        print(f"Description: {self.description}")
        print(f"Model: {self.model}")
        print(f"Instructions: {self.instructions}")
        print(f"Tools: {self.tools}")
        print(f"File IDs: {self.file_ids}")
        print(f"Metadata: {self.metadata}")

    def retrieve(self):
        assistant = retrieve_assistant(self.id)
        self.__dict__.update(**assistant.__dict__)
        return assistant

    def delete(self):
        delete_assistant(self.id)
        self.__dict__.clear()
        del self
        return True

    def update(
            self,
            model: str or None = None,
            name: str or None = None,
            description: str or None = None,
            instructions: str or None = None,
            code_interpreter: bool or None = None,
            retrieval: bool or None = None,
            functions: Functions or None = None,
            file_ids: list or None = None,
            metadata: dict or None = None
    ):
        assistant = update_assistant(
            self.id,
            model,
            name,
            description,
            instructions,
            code_interpreter,
            retrieval,
            functions,
            file_ids,
            metadata
        )
        self.__dict__.update(**assistant.__dict__)
        return assistant
