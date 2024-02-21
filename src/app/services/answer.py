import requests
import json
import time
import os
import re

ASSISTANT_ID = os.environ["ASSISTANT_ID"]

FILES = {
    'file-vY8A41vQ0vJf5MPjxsM2ytg7': 
        {'title': 'Como iniciar uma conversa',
        'link': 'https://suporte.ubots.com.br/support/solutions/articles/36000476340-como-iniciar-uma-conversa'},
    'file-JOsygLBh16FlTK8LdY7YDVnl':
        {'title': 'Como um atendente opera no Ubots Desk?',
        'link': 'https://suporte.ubots.com.br/support/solutions/articles/36000380595-como-um-atendente-opera-no-ubots-desk'},
    'file-TzgcJlLSXERlhZSPjmjGdV1f':
        {'title': 'Falha ao enviar mensagem no WhatsApp',
        'link':'https://suporte.ubots.com.br/support/solutions/articles/36000404028-falha-ao-enviar-mensagem-no-whatsapp'},
    'file-xmaDtqkBiLUZ39Qcy7Y7GR1A':
        {'title': 'Impressão de Histórico de Conversas',
         'link': 'https://suporte.ubots.com.br/support/solutions/articles/36000381865-impress%C3%A3o-de-hist%C3%B3rico-de-conversas'},
    'file-W0D2lyxwCS9lGsHvNsaqkqbX':
        {'title': 'Formatação de texto: Markdown',
        'link': 'https://suporte.ubots.com.br/support/solutions/articles/36000453738-formatac%C3%A3o-de-texto-markdown'}}

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

    while True:
        response = requests.get(url, headers=headers)
        if len(response.json().get("data")) > 0:
            if response.json().get("data")[0].get("role") == "assistant":
                if len(response.json().get("data")[0].get("content")) > 0:
                    annotations = response.json().get("data")[0].get("content")[0].get("text").get("annotations")
                    answer = response.json().get("data")[0].get("content")[0].get("text").get("value")
                    
                    formattedAnswer = re.sub(r'【.*?】', '', answer)

                    fileIds = _get_files_from_annotations(annotations)
                    references = _get_references(fileIds)
                    
                    return {
                        "content": formattedAnswer,
                        "references": references
                    }
                
        time.sleep(3)

def _get_references(fileIds):
    references = []
    for file_id in fileIds:
        file = FILES.get(file_id)
        references.append(file)
    
    return references

def _get_files_from_annotations(annotations):
    fileIds = []
    for annotation in annotations:
        fileIds.append(annotation["file_citation"]["file_id"])
    return fileIds

def answer_question(question):
    thread_id = _create_thread()
    _create_message(thread_id, question)
    run_id = _create_run(thread_id)
    _run_retrive(thread_id, run_id)
    answer = _get_completion_assistant(thread_id)

    response = {
        "answers": [
            {
                "content": {
                    "data": answer["content"],
                },
                "references": answer["references"]
            }
        ]
    }
    
    return response
