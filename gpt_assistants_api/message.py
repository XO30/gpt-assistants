from .utils import send_get_request, send_delete_request, send_post_request
from .constants import HEADERS
from .file import list_message_files, upload_file


def create_message(thread_id: str, content: str, role: str = 'user', files: list or None = None, metadata: dict or None = None) -> object:
    """
    create a new message
    :param thread_id: str: id of the thread
    :param content: str: content of the message
    :param role: str: role of the message (user or assistant)
    :param files: list: list of files to upload
    :param metadata: dict: metadata to add
    :return: object: message object
    """

    url = f"https://api.openai.com/v1/threads/{thread_id}/messages"
    data = {}
    data["role"] = role
    data["content"] = content
    file_ids = []
    if files:
        for file in files:
            f = upload_file(file)
            file_ids.append(f.id)
    data["file_ids"] = file_ids
    if metadata:
        data["metadata"] = metadata

    response = send_post_request(url, HEADERS, data)
    return Message(**response)


def retrieve_message(thread_id: str, message_id: str) -> object:
    """
    retrieve a message
    :param thread_id: str: id of the thread
    :param message_id: str: id of the message
    :return: object: message object
    """

    url = f"https://api.openai.com/v1/threads/{thread_id}/messages/{message_id}"
    response = send_get_request(url, HEADERS)
    return Message(**response)


def list_messages(thread_id: str) -> list:
    """
    list all messages in a thread
    :param thread_id: str: id of the thread
    :return: list: list of message objects
    """

    url = f"https://api.openai.com/v1/threads/{thread_id}/messages"
    response = send_get_request(url, HEADERS)
    return [Message(**message) for message in response["data"]]


def delete_message(thread_id: str, message_id: str) -> bool:
    """
    delete a message
    :param thread_id: str: id of the thread
    :param message_id: str: id of the message
    :return: bool: True if deleted
    """

    url = f"https://api.openai.com/v1/threads/{thread_id}/messages/{message_id}"
    send_delete_request(url, HEADERS)
    return True


def modify_message(thread_id: str, message_id: str, metadata: dict) -> object:
    """
    modify a message
    :param thread_id: str: id of the thread
    :param message_id: str: id of the message
    :param metadata: dict: metadata to update
    :return: object: message object
    """

    url = f"https://api.openai.com/v1/threads/{thread_id}/messages/{message_id}"
    data = {
        "metadata": metadata
    }
    response = send_post_request(url, HEADERS, data)
    return Message(**response)


class Message:
    def __init__(
            self,
            id: str,
            object: str,
            created_at: int,
            thread_id: str,
            role: str,
            content: str,
            assistant_id: str,
            run_id: str,
            file_ids: list,
            metadata: map
    ):
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

    def info(self) -> None:
        """
        print message info
        :return: None
        """
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
        return None

    def retrieve(self) -> object:
        """
        retrieve message
        :return: object: message object
        """

        message = retrieve_message(self.thread_id, self.id)
        self.__dict__.update(**message.__dict__)
        return message

    def delete(self) -> bool:
        """
        delete message
        :return: True if deleted
        """

        delete_message(self.thread_id, self.id)
        self.__dict__.clear()
        del self
        return True

    def update(self, metadata: dict) -> object:
        """
        update message
        :param metadata: dict: metadata to update
        :return: object: message object
        """

        message = modify_message(self.thread_id, self.id, metadata)
        self.__dict__.update(**message.__dict__)
        return message

    def list_files(self) -> list:
        """
        list all files in a message
        :return: list: list of file objects
        """

        return list_message_files(self.thread_id, self.id)


