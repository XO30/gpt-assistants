import json
import requests


def send_post_request(url: str, headers: dict, data: dict) -> dict:
    """
    send a post request
    :param url: str: url to send request to
    :param headers: dict: headers to send
    :param data: dict: data to send
    :return: dict: response
    """

    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(response.text)


def send_get_request(url: str, headers: dict) -> dict:
    """
    send a get request
    :param url: str: url to send request to
    :param headers: dict: headers to send
    :return: dict: response
    """

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(response.text)


def send_delete_request(url: str, headers: dict or None = None) -> dict:
    """
    send a delete request
    :param url: str: url to send request to
    :param headers: dict: headers to send
    :return: dict: response
    """

    response = requests.delete(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(response.text)


def send_file(url: str, headers: dict, data: dict, file: dict) -> dict:
    """
    send a file
    :param url: str: url to send request to
    :param headers: dict: headers to send
    :param data: dict: data to send
    :param file: dict: file to send
    :return: dict: response
    """

    response = requests.post(url, headers=headers, data=data, files=file)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(response.text)
