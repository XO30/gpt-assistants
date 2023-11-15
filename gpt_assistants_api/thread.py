from .utils import send_post_request, send_get_request, send_delete_request
from .constants import HEADERS
from .tools import Tools
from .message import create_message, retrieve_message, list_messages, delete_message, modify_message
from .run import create_run, retrieve_run, list_runs, modify_run, cancel_run


def create_thread() -> object:
    """
    create a new thread
    :return: object: thread object
    """

    url = "https://api.openai.com/v1/threads"
    response = send_post_request(url, HEADERS, {})
    return Thread(**response)


def retrieve_thread(thread_id: str) -> object:
    """
    retrieve a thread
    :param thread_id: str: id of the thread
    :return: object: thread object
    """

    url = f"https://api.openai.com/v1/threads/{thread_id}"
    response = send_get_request(url, HEADERS)
    return Thread(**response)


def delete_thread(thread_id: str) -> bool:
    """
    delete a thread
    :param thread_id: id of the thread
    :return: bool: True if deleted
    """

    url = f"https://api.openai.com/v1/threads/{thread_id}"
    send_delete_request(url, HEADERS)
    return True


def _list_threads() -> list:
    """
    list all threads (currently not working)
    :return: list: list of thread objects
    """

    url = "https://api.openai.com/v1/threads?order=desc&limit=20"
    response = send_get_request(url, HEADERS)
    return [Thread(**thread) for thread in response["data"]]


def modify_thread(thread_id: str, metadata: dict) -> object:
    """
    modify a thread
    :param thread_id: str: id of the thread
    :param metadata: dict: metadata to update
    :return: object: thread object
    """

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

    def info(self) -> None:
        """
        print thread info
        :return: None
        """

        print(f"ID: {self.id}")
        print(f"Object: {self.object}")
        print(f"Created at: {self.created_at}")
        print(f"Metadata: {self.metadata}")
        return None

    def retrieve(self) -> object:
        """
        retrieve thread
        :return: object: thread object
        """

        thread = retrieve_thread(self.id)
        self.__dict__.update(**thread.__dict__)
        return thread

    def delete(self) -> bool:
        """
        delete thread
        :return: bool: True if deleted
        """

        delete_thread(self.id)
        self.__dict__.clear()
        del self
        return True

    def update(self, metadata: dict) -> object:
        """
        update thread
        :param metadata: dict: metadata to update
        :return: object: thread object
        """

        thread = modify_thread(self.id, metadata)
        self.__dict__.update(**thread.__dict__)
        return thread

    def create_message(self, content: str, role: str = "user", files: list or None = None, metadata: dict or None = None) -> object:
        """
        create a new message
        :param content: str: content of the message
        :param role: str: role of the message (user or assistant)
        :param files: list or None: list of file ids
        :param metadata: dict or None: metadata for the message
        :return: object: message object
        """

        return create_message(self.id, content, role, files, metadata)

    def retrieve_message(self, message_id: str) -> object:
        """
        retrieve a message
        :param message_id: str: id of the message
        :return: object: message object
        """

        return retrieve_message(self.id, message_id)

    def list_messages(self) -> list:
        """
        list all messages
        :return: list: list of message objects
        """

        return list_messages(self.id)

    def delete_message(self, message_id: str) -> bool:
        """
        delete a message
        :param message_id: str: id of the message
        :return: bool: True if deleted
        """

        delete_message(self.id, message_id)
        return True

    def modify_message(self, message_id: str, metadata: dict) -> object:
        """
        modify a message
        :param message_id: str: id of the message
        :param metadata: dict: metadata to update
        :return: object: message object
        """

        return modify_message(self.id, message_id, metadata)

    def create_run(
            self,
            assistant_id: str,
            model: str or None = None,
            instructions: str or None = None,
            tools: Tools or None = None,
            metadata: dict or None = None
    ) -> object:
        """
        create a new run
        :param assistant_id: str: id of the assistant
        :param model: str or None: id of the model
        :param instructions: str or None: instructions for the run
        :param tools: Tools or None: tools for the run
        :param metadata: str or None: metadata for the run
        :return: object: run object
        """

        return create_run(self.id, assistant_id, model, instructions, tools, metadata)

    def retrieve_run(self, run_id: str) -> object:
        """
        retrieve a run
        :param run_id: str: id of the run
        :return: object: run object
        """

        return retrieve_run(self.id, run_id)

    def list_runs(self) -> list:
        """
        list all runs
        :return: list: list of run objects
        """

        return list_runs(self.id)

    def modify_run(self, run_id: str, metadata: dict) -> object:
        """
        modify a run
        :param run_id: str: id of the run
        :param metadata: dict: metadata to update
        :return: object: run object
        """

        return modify_run(self.id, run_id, metadata)

    def submit_tool_output(self, run_id: str, tool_outputs: list) -> object:
        """
        submit tool output
        :param run_id: str: id of the run
        :param tool_outputs: list: list of dictionaries of tool outputs
        :return: object: run object
        """

        return submit_tool_output(self.id, run_id, tool_outputs)

    def cancel_run(self, run_id: str) -> object:
        """
        cancel a run
        :param run_id: str: id of the run
        :return: object: run object
        """

        return cancel_run(self.id, run_id)
