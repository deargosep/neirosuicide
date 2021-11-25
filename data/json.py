import json

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

# checks if string is a substring of input


def check(inp: str) -> str:
    for string in read('bad'):
        if string in inp:
            return 'bad'
    for string in read('good'):
        if string in inp:
            return 'good'
