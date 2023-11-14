<a name="readme-top"></a>

<div align="center">
  
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<h3 align="center">GPT Assistants Python API</h3>

  <p align="center">
    This is a Python API for the new GPT Assistants API from OpenAI.
    It is designed to help you get started with the API and simplify the process of building your own GPT Assistant.
    <br />
    <a href="https://github.com/XO30/gtp-assistants"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/XO30/gtp-assistants/issues">Report Bug</a>
    <a href="https://github.com/XO30/gtp-assistants/issues">Request Feature</a>
  </p>
</div>


<!-- ABOUT THE PROJECT -->
# About The Project
GPT Assistants Python API is a Python wrapper for the new GPT Assistants API from OpenAI.
It is designed to help you get started with bulding your own GPT Assistant and.
Assistants can be simply created and modified with the help of the API.
Furthermore, the API provides a simple way to create threads, messages and runs.


# Usage
the following examples show the basic usage of the API.
There are way more functions available. For more information see the code.
in the near I will update the documentation and add more examples.

## API Key

To use the API you need an API key from OpenAI. You can get one [here](https://beta.openai.com/).
Furthermore, you need to install set your API key as an environment variable.

```python
API_KEY = 'api-key'
import os
os.environ['OPENAI_API_KEY'] = API_KEY
```

First you need to import some functions from the api

```python
from src.assistant import list_assistants, retrieve_assistant, delete_assistant, modify_assistant, create_assistant
from src.thread import create_thread, retrieve_thread, delete_thread, modify_thread
from src.utils import Tools
```

## Assistant

With the api you can easily create new assistants and modify them.

Let's create a new assistant. The only required parameter is the model. The other parameters are optional.
See the documentation to see what parameters are available.

```python
assistant = create_assistant(
    model="gpt-4",
    name="my-assistant",
    description="my first assistant",
    instructions="be a friendly assistant"
)

assistant.info()

list_assistants()
```

## Thread

Let's now create a new thread.

```python
thread = create_thread()

thread.info()
```

## Message

Now we can create messages in the thread.

```python
thread.create_message("tell me a joke")

thread.list_messages()
```


## Run

after we added some messages we can create a run.

```python
thread.create_run(assistant.id)

thread.list_runs()

thread.list_messages()

thread.list_messages()[0].info()
```

As you can see the run has generated a response to our message.

# Roadmap
there are a lot of things that need to be done. a roadmap will be added soon.


# Contact

Stefan Siegler: dev@siegler.one

Project Link: [https://github.com/XO30/gtp-assistants](https://github.com/XO30/gtp-assistants)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/XO30/gtp-assistants.svg?style=for-the-badge
[contributors-url]: https://github.com/XO30/gtp-assistants/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/XO30/gtp-assistants.svg?style=for-the-badge
[forks-url]: https://github.com/XO30/gtp-assistants/network/members
[stars-shield]: https://img.shields.io/github/stars/XO30/gtp-assistants.svg?style=for-the-badge
[stars-url]: https://github.com/XO30/gtp-assistants/stargazers
[issues-shield]: https://img.shields.io/github/issues/XO30/gtp-assistants.svg?style=for-the-badge
[issues-url]: https://github.com/XO30/gtp-assistants/issues
[license-shield]: https://img.shields.io/github/license/XO30/gtp-assistants.svg?style=for-the-badge
[license-url]: https://github.com/XO30/gtp-assistants/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/stefan-siegler-04b116205