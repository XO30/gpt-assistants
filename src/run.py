from .utils import send_post_request, send_get_request, send_delete_request
from .utils import HEADERS


def create_run(
        thread_id: str,
        assistant_id: str,
        model: str or None = None,
        instructions: str or None = None,
        tools: list or None = None,
        metadata: dict or None = None
):
    data = dict()
    data["assistant_id"] = assistant_id
    if model is not None:
        data["model"] = model
    if instructions is not None:
        data["instructions"] = instructions
    if tools is not None:
        data["tools"] = tools
    if metadata is not None:
        data["metadata"] = metadata

    url = f"https://api.openai.com/v1/threads/{thread_id}/runs"
    response = send_post_request(url, data=data, headers=HEADERS)
    return Run(**response)


def retrieve_run(thread_id: str, run_id: str):
    url = f"https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}"
    response = send_get_request(url, headers=HEADERS)
    return Run(**response)


def modify_run(thread_id: str, run_id: str, metadata: dict):
    data = dict()
    data["metadata"] = metadata

    url = f"https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}"
    response = send_post_request(url, data=data, headers=HEADERS)
    return Run(**response)


def list_runs(thread_id: str):
    url = f"https://api.openai.com/v1/threads/{thread_id}/runs"
    response = send_get_request(url, headers=HEADERS)
    return [Run(**run) for run in response["data"]] if "data" in response else []


def cancel_run(thread_id: str, run_id: str):
    url = f"https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}/cancel"
    response = send_post_request(url, data={}, headers=HEADERS)
    return Run(**response)


def submit_tool_output(thread_id: str, run_id: str, tool_call_id: str, output: str):
    data = dict()
    data["tool_call_id"] = tool_call_id
    data["output"] = output
    url = f"https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}/submit_tool_outputs"
    response = send_post_request(url, data=data, headers=HEADERS)
    return Run(**response)


class Run:
    def __init__(
            self,
            id: str,
            object: str,
            created_at: int,
            thread_id: str,
            assistant_id: str,
            status: str,
            expires_at: int,
            model: str,
            instructions: str,
            tools: list,
            file_ids: list,
            metadata: dict,
            started_at: int or None = None,
            cancelled_at: int or None = None,
            failed_at: int or None = None,
            completed_at: int or None = None,
            required_actions: object or None = None,
            last_error: str or None = None,
    ):
        self.id = id
        self.object = object
        self.created_at = created_at
        self.thread_id = thread_id
        self.assistant_id = assistant_id
        self.status = status
        self.required_actions = required_actions
        self.last_error = last_error
        self.expires_at = expires_at
        self.started_at = started_at
        self.cancelled_at = cancelled_at
        self.failed_at = failed_at
        self.completed_at = completed_at
        self.model = model
        self.instructions = instructions
        self.tools = tools
        self.file_ids = file_ids
        self.metadata = metadata

    def __str__(self):
        return f"Run: {self.id} ({self.status})"

    def __repr__(self):
        return f"Run: {self.id} ({self.status})"

    def info(self):
        print(f"ID: {self.id}")
        print(f"Object: {self.object}")
        print(f"Created at: {self.created_at}")
        print(f"Thread ID: {self.thread_id}")
        print(f"Assistant ID: {self.assistant_id}")
        print(f"Status: {self.status}")
        print(f"Required actions: {self.required_actions}")
        print(f"Last error: {self.last_error}")
        print(f"Expires at: {self.expires_at}")
        print(f"Started at: {self.started_at}")
        print(f"Cancelled at: {self.cancelled_at}")
        print(f"Failed at: {self.failed_at}")
        print(f"Completed at: {self.completed_at}")
        print(f"Model: {self.model}")
        print(f"Instructions: {self.instructions}")
        print(f"Tool: {self.tools}")
        print(f"File IDs: {self.file_ids}")
        print(f"Metadata: {self.metadata}")

    def retrieve(self):
        run = retrieve_run(self.thread_id, self.id)
        self.__dict__.update(**run.__dict__)
        return run

    def modify(self, metadata: dict):
        run = modify_run(self.thread_id, self.id, metadata)
        self.__dict__.update(**run.__dict__)
        return run

    def cancel(self):
        run = cancel_run(self.thread_id, self.id)
        self.__dict__.update(**run.__dict__)
        return run

    def submit_tool_output(self, tool_call_id: str, output: str):
        run = submit_tool_output(self.thread_id, self.id, tool_call_id, output)
        self.__dict__.update(**run.__dict__)
        return run
    