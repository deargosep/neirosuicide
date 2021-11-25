import json
from api.ai import analyze
from dotenv import dotenv_values
import openai

# returns an array from json


def read(which: str) -> dict:
    if (which == 'bad'):
        with open('data/bad.json') as strings:
            stringsArr = json.load(strings)
        return stringsArr

    if (which == 'good'):
        with open('data/good.json') as strings:
            stringsArr = json.load(strings)
        return stringsArr
    if (which == 'ai-classify'):
        with open('data/examples_classify.json') as strings:
            stringsArr = json.load(strings)
            return stringsArr

# checks if string is a substring of input


def check(inp: str) -> str:
    if dotenv_values().__getitem__("USE_AI") == 'True':
        openai.api_key = dotenv_values().__getitem__("OPENAI_API_KEY")
        return analyze(inp, read('ai-classify'))
    else:
        for string in read('bad'):
            if string in inp:
                return 'bad'
        for string in read('good'):
            if string in inp:
                return 'good'
