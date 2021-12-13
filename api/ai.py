from dotenv import dotenv_values
from iot.light import BulbControl
import openai

light = BulbControl()


def complete(query):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"You: {query}, Friend:",
        temperature=0.4,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0,
        stop=["You:"]
    )
    return response


def classify(query, examples):
    classification = openai.Classification.create(
        search_model="ada",
        model="curie",
        examples=examples,
        query=query,
        labels=["Positive", "Negative", "Neutral"]
    )
    return classification


def analyze(query, examples_classify: dict) -> str:
    classified = classify(query, examples_classify)
    completed = complete(query)
    light.emote(classified['label'])
    if classified['label'] == 'Neutral':
        return completed
    else:
        return classified['label']
