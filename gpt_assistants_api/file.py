from .utils import send_post_request, send_get_request, send_delete_request, send_file
from .constants import HEADERS, HEADERS_OLD


def list_files() -> list:
    """
    list files
    :return: list: list of file objects
    """

    response = send_get_request("https://api.openai.com/v1/files", HEADERS_OLD)
    return [File(**file) for file in response["data"]]


def upload_file(file: str, purpose: str = 'assistants') -> object:
    """
    upload a file
    :param file: str: file to upload
    :param purpose: str: purpose of file
    :return: object: file object
    """
    data = {
        "purpose": purpose,
    }
    file = {
        "file": file
    }
    response = send_file("https://api.openai.com/v1/files", HEADERS_OLD, data, file)
    return File(**response)


def delete_file(file_id: str) -> bool:
    """
    delete a file
    :param file_id: str: id of file to delete
    :return: bool: True if successful
    """

    response = send_delete_request(f"https://api.openai.com/v1/files/{file_id}", HEADERS_OLD)
    return True


def retrieve_file(file_id: str) -> object:
    """
    retrieve a file
    :param file_id: str: id of file to retrieve
    :return: object: file object
    """

    response = send_get_request(f"https://api.openai.com/v1/files/{file_id}", HEADERS_OLD)
    return File(**response)


def retrieve_file_contents(file_id: str) -> any:
    """
    retrieve a file's contents
    :param file_id: str: id of file to retrieve
    :return: any(): file contents
    """

    response = send_get_request(f"https://api.openai.com/v1/files/{file_id}/content", HEADERS_OLD)
    return response


def create_assistant_file(assistant_id: str, file_id: str) -> object:
    """
    create an assistant file
    :param assistant_id: str: id of assistant to create file for
    :param file_id: str: id of file to create
    :return: object: assistant file object
    """

    response = send_post_request(f"https://api.openai.com/v1/assistants/{assistant_id}/files", HEADERS, {
        "file_id": file_id
    })
    return AssistantFile(**response)


def retrieve_assistant_file(assistant_id: str, file_id: str) -> object:
    """
    retrieve an assistant file
    :param assistant_id: str: id of assistant to retrieve file for
    :param file_id: str: id of file to retrieve
    :return: object: assistant file object
    """

    response = send_get_request(f"https://api.openai.com/v1/assistants/{assistant_id}/files/{file_id}", HEADERS)
    return AssistantFile(**response)


def delete_assistant_file(assistant_id: str, file_id: str) -> bool:
    """
    delete an assistant file
    :param assistant_id: str: id of assistant to delete file for
    :param file_id: str: id of file to delete
    :return: bool: True if successful
    """

    response = send_delete_request(f"https://api.openai.com/v1/assistants/{assistant_id}/files/{file_id}", HEADERS)
    return True


def list_assistant_files(assistant_id: str) -> list:
    """
    list assistant files
    :param assistant_id: str: id of assistant to list files for
    :return: list: list of assistant files
    """

    response = send_get_request(f"https://api.openai.com/v1/assistants/{assistant_id}/files", HEADERS)
    return [AssistantFile(**file) for file in response["data"]]


def retrieve_message_file(thread_id:str, message_id: str, file_id: str) -> object:
    """
    retrieve a message file
    :param thread_id: str: id of thread to retrieve file for
    :param message_id: str: id of message to retrieve file for
    :param file_id: str: id of file to retrieve
    :return: object: message file object
    """

    response = send_get_request(f"https://api.openai.com/v1/threads/{thread_id}/messages/{message_id}/files/{file_id}", HEADERS)
    return MessageFile(**response)


def list_message_files(thread_id: str, message_id: str) -> list:
    """
    list message files
    :param thread_id: str: id of thread to list files for
    :param message_id: str: id of message to list files for
    :return: list: list of message file objects
    """

    response = send_get_request(f"https://api.openai.com/v1/threads/{thread_id}/messages/{message_id}/files", HEADERS)
    return [MessageFile(**file) for file in response]


class File:
    def __init__(self, id: str, bytes: str, filename: str, object: str, created_at: int, purpose: str, status: str or None = None, status_details: str or None = None):
        self.id = id
        self.bytes = bytes
        self.filename = filename
        self.object = object
        self.created_at = created_at
        self.purpose = purpose
        self.status = status
        self.status_details = status_details


    def __repr__(self):
        return f"<File {self.id}>"

    def __str__(self):
        return f"<File {self.id}>"

    def info(self):
        """
        print info about file
        :return: None
        """
        print(f"File ID: {self.id}")
        print(f"Filename: {self.filename}")
        print(f"Created At: {self.created_at}")
        print(f"Purpose: {self.purpose}")
        print(f"Object: {self.object}")
        print(f"Bytes: {self.bytes}")
        print(f"Status: {self.status}")
        print(f"Status Details: {self.status_details}")
        return None

    def delete(self):
        """
        delete file
        :return: bool: True if successful
        """
        delete_file(self.id)
        self.__dict__.clear()
        del self
        return True

    def retrieve(self):
        """
        retrieve file
        :return: object: file object
        """
        file = retrieve_file(self.id)
        self.__dict__.update(**file.__dict__)
        return file

    def retrieve_contents(self):
        """
        retrieve file contents
        :return: any(): file contents
        """
        return retrieve_file_contents(self.id)


class AssistantFile:
    def __init__(self, id: str, object: str, created_at: int, assistant_id: str):
        self.id = id
        self.object = object
        self.created_at = created_at
        self.assistant_id = assistant_id

    def __repr__(self):
        return f"<AssistantFile {self.id}>"

    def __str__(self):
        return f"<AssistantFile {self.id}>"

    def info(self):
        """
        print info about assistant file
        :return: None
        """
        print(f"File ID: {self.id}")
        print(f"Created At: {self.created_at}")
        print(f"Object: {self.object}")
        print(f"Assistant ID: {self.assistant_id}")
        return None

    def delete(self):
        """
        delete assistant file
        :return: bool: True if successful
        """
        delete_assistant_file(self.assistant_id, self.id)
        self.__dict__.clear()
        del self
        return True

    def retrieve(self):
        """
        retrieve assistant file
        :return: object: assistant file object
        """
        assistant_file = retrieve_assistant_file(self.assistant_id, self.id)
        self.__dict__.update(**assistant_file.__dict__)
        return assistant_file

    def retrieve_contents(self):
        """
        retrieve assistant file contents
        :return: any(): assistant file contents
        """
        return retrieve_file_contents(self.id)


class MessageFile:
    def __init__(self, id: str, object: str, created_at: int, message_id: str):
        self.id = id
        self.object = object
        self.created_at = created_at
        self.message_id = message_id

    def __repr__(self):
        return f"<MessageFile {self.id}>"

    def __str__(self):
        return f"<MessageFile {self.id}>"

    def info(self):
        """
        print info about message file
        :return: None
        """
        print(f"File ID: {self.id}")
        print(f"Created At: {self.created_at}")
        print(f"Object: {self.object}")
        print(f"Message ID: {self.message_id}")
        return None

    def retrieve(self, thread_id: str):
        """
        retrieve message file
        :return: object: message file object
        """
        message_file = retrieve_message_file(thread_id, self.message_id, self.id)
        self.__dict__.update(**message_file.__dict__)
        return message_file

    def retrieve_content(self):
        """
        retrieve message file contents
        :return: any(): message file contents
        """
        return retrieve_file_contents(self.id)
