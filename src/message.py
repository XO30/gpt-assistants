from .utils import send_get_request, send_delete_request, send_post_request
from .utils import HEADERS


def create_message(thread_id: str, role: str, content: str):
    url = f"https://api.openai.com/v1/threads/{thread_id}/messages"
    data = {
        "role": role,
        "content": content
    }
    response = send_post_request(url, HEADERS, data)
    return Message(**response)


def retrieve_message(thread_id: str, message_id: str):
    url = f"https://api.openai.com/v1/threads/{thread_id}/messages/{message_id}"
    response = send_get_request(url, HEADERS)
    return Message(**response)


def list_messages(thread_id: str):
    url = f"https://api.openai.com/v1/threads/{thread_id}/messages"
    response = send_get_request(url, HEADERS)
    return [Message(**message) for message in response["data"]]


def delete_message(thread_id: str, message_id: str):
    url = f"https://api.openai.com/v1/threads/{thread_id}/messages/{message_id}"
    send_delete_request(url, HEADERS)
    return True


def modify_message(thread_id: str, message_id: str, metadata: dict):
    url = f"https://api.openai.com/v1/threads/{thread_id}/messages/{message_id}"
    data = {
        "metadata": metadata
    }
    response = send_post_request(url, HEADERS, data)
    return Message(**response)


class Message:
    def __init__(self, id: str, object: str, created_at: int, thread_id: str, role: str, content: str,
                 assistant_id: str, run_id: str, file_ids: list, metadata: map):
        self.id = id
        self.object = object
        self.created_at = created_at
        self.thread_id = thread_id
        self.role = role
        self.content = content
        self.assistant_id = assistant_id
        self.run_id = run_id
        self.file_ids = file_ids
        self.metadata = metadata

    def __repr__(self):
        return f"<Message {self.id}>"

    def __str__(self):
        return f"<Message {self.id}>"

    def info(self):
        print(f"ID: {self.id}")
        print(f"Object: {self.object}")
        print(f"Created at: {self.created_at}")
        print(f"Thread ID: {self.thread_id}")
        print(f"Role: {self.role}")
        print(f"Content: {self.content}")
        print(f"Assistant ID: {self.assistant_id}")
        print(f"Run ID: {self.run_id}")
        print(f"File IDs: {self.file_ids}")
        print(f"Metadata: {self.metadata}")

    def retrieve(self):
        message = retrieve_message(self.thread_id, self.id)
        self.__dict__.update(**message.__dict__)
        return message

    def delete(self):
        delete_message(self.thread_id, self.id)
        self.__dict__.clear()
        del self
        return True

    def update(self, metadata: dict):
        message = modify_message(self.thread_id, self.id, metadata)
        self.__dict__.update(**message.__dict__)
        return message
