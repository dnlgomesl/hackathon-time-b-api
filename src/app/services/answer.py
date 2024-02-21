import requests
import json
import time
import os

ASSISTANT_ID = os.environ["ASSISTANT_ID"]

FILES = {
    "file_id": {"title": "TITULO", "link": "url.com.br"}
}

key = os.environ["OPENAI_KEY"]

headers = {
      'Authorization': f'Bearer {key}',
      'OpenAI-Beta': 'assistants=v1',
      'Content-Type': 'application/json'
}

def _create_thread(headers=headers):
    url = f'https://api.openai.com/v1/threads'
    response = requests.post(url, headers=headers)
    return response.json().get("id")


def _create_message(thread_id, question,  headers=headers):
    url = f'https://api.openai.com/v1/threads/{thread_id}/messages'
    payload = {
        "role": "user",
        "content": question
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json().get("id")


def _create_run(thread_id, assistant_id=ASSISTANT_ID, headers=headers):
    url = f'https://api.openai.com/v1/threads/{thread_id}/runs'
    payload = {
        "assistant_id": assistant_id
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json().get("id")


def _run_retrive(thread_id, run_id, headers=headers):
    url = f'https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}'
    requests.get(url, headers=headers)


def _get_completion_assistant(thread_id, headers=headers):
    url = f'https://api.openai.com/v1/threads/{thread_id}/messages'
    response = requests.get(url, headers=headers)
    return response.json().get("data")[0].get("content")[0].get("text").get("value")


def answer_question(question, time_sleep=60):
    thread_id = _create_thread()
    _create_message(thread_id, question)
    run_id = _create_run(thread_id)
    _run_retrive(thread_id, run_id)
    time.sleep(time_sleep)
    answer = _get_completion_assistant(thread_id)

    response = {"answer": answer}

    return response
