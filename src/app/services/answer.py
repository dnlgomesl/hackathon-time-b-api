import requests
import json
import time
import os

key = os.environ["OPENAI_KEY"]
headers = {
      'Authorization': f'Bearer {key}',
      'OpenAI-Beta': 'assistants=v1',
      'Content-Type': 'application/json'
}

ASSISTANT_ID = os.environ["ASSISTANT_ID"]

def create_thread(assistant_id=ASSISTANT_ID, headers=headers):
    url = f'https://api.openai.com/v1/threads'
    response = requests.post(url, headers=headers)
    return response.json().get("id")


def create_message(thread_id, question,  headers=headers):
    url = f'https://api.openai.com/v1/threads/{thread_id}/messages'
    payload = {
        "role": "user",
        "content": question
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json().get("id")


def create_run(thread_id, assistant_id=ASSISTANT_ID, headers=headers):
    url = f'https://api.openai.com/v1/threads/{thread_id}/runs'
    payload = {
        "assistant_id": assistant_id
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json().get("id")


def run_retrive(thread_id, run_id, headers=headers):
    url = f'https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}'
    response = requests.get(url, headers=headers)
    return response.json().get("id")


def get_completion_assistant(thread_id, headers=headers):
    url = f'https://api.openai.com/v1/threads/{thread_id}/messages'
    response = requests.get(url, headers=headers)
    return response.json().get("data")[0].get("content")[0].get("text").get("value")


def answer_question(question, headers=headers, time_sleep=60):
    thread_id = create_thread()
    create_message(thread_id, question)
    run_id = create_run(thread_id)
    run_retrive(thread_id, run_id)
    time.sleep(time_sleep)
    answer = get_completion_assistant(thread_id)

    response = {"answer": answer}

    return response
