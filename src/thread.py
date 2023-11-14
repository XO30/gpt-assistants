from .utils import send_post_request, send_get_request, send_delete_request
from .utils import HEADERS
from .message import create_message, retrieve_message, list_messages, delete_message, modify_message
from .run import create_run, retrieve_run, list_runs, modify_run, submit_tool_output, cancel_run


def create_thread():
    url = "https://api.openai.com/v1/threads"
    response = send_post_request(url, HEADERS, {})
    return Thread(**response)


def retrieve_thread(thread_id: str):
    url = f"https://api.openai.com/v1/threads/{thread_id}"
    response = send_get_request(url, HEADERS)
    return Thread(**response)


def delete_thread(thread_id: str):
    url = f"https://api.openai.com/v1/threads/{thread_id}"
    send_delete_request(url, HEADERS)
    return True


def list_threads():
    url = "https://api.openai.com/v1/threads?order=desc&limit=20"
    response = send_get_request(url, HEADERS)
    return [Thread(**thread) for thread in response["data"]]


def modify_thread(thread_id: str, metadata: dict):
    url = f"https://api.openai.com/v1/threads/{thread_id}"
    data = {
        "metadata": metadata
    }
    response = send_post_request(url, HEADERS, data)
    return Thread(**response)


class Thread:
    def __init__(self, id: str, object: str, created_at: int, metadata: dict):
        self.id = id
        self.object = object
        self.created_at = created_at
        self.metadata = metadata

    def __repr__(self):
        return f"<Thread {self.id}>"

    def __str__(self):
        return f"<Thread {self.id}>"

    def info(self):
        print(f"ID: {self.id}")
        print(f"Object: {self.object}")
        print(f"Created at: {self.created_at}")
        print(f"Metadata: {self.metadata}")

    def retrieve(self):
        thread = retrieve_thread(self.id)
        self.__dict__.update(**thread.__dict__)
        return thread

    def delete(self):
        delete_thread(self.id)
        self.__dict__.clear()
        del self
        return True

    def update(self, metadata: dict):
        thread = modify_thread(self.id, metadata)
        self.__dict__.update(**thread.__dict__)
        return thread

    def create_message(self, role: str, content: str):
        message = create_message(self.id, role, content)
        return message

    def retrieve_message(self, message_id: str):
        message = retrieve_message(self.id, message_id)
        return message

    def list_messages(self):
        messages = list_messages(self.id)
        return messages

    def delete_message(self, message_id: str):
        delete_message(self.id, message_id)
        return True

    def modify_message(self, message_id: str, metadata: dict):
        message = modify_message(self.id, message_id, metadata)
        return message

    def create_run(
            self,
            assistant_id: str,
            model: str or None = None,
            instructions: str or None = None,
            tools: list or None = None,
            metadata: dict or None = None
    ):
        run = create_run(self.id, assistant_id, model, instructions, tools, metadata)
        return run

    def retrieve_run(self, run_id: str):
        run = retrieve_run(self.id, run_id)
        return run

    def list_runs(self):
        runs = list_runs(self.id)
        return runs

    def modify_run(self, run_id: str, metadata: dict):
        run = modify_run(self.id, run_id, metadata)
        return run

    def submit_tool_output(self, run_id: str, tool_call_id: str, output: str):
        run = submit_tool_output(self.id, run_id, tool_call_id, output)
        return run

    def cancel_run(self, run_id: str):
        run = cancel_run(self.id, run_id)
        return run