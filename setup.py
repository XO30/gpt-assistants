# import
from setuptools import setup

# setup
setup(
    name='gpt-assistants-api',
    version='0.9.1',
    url='https://github.com/XO30/gtp-assistants',
    author='Stefan Siegler',
    author_email='dev@siegler.one',
    py_modules=['gpt_assistants_api'],
    classifiers=[
        'Intended Audience :: ML Engineers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
        'Programming Language :: Python :: 3.11'
    ],
    install_requires=[
        'requests',
    ],
    python_requires='>3.5, <4',
)
