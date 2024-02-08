import requests

headers = {
    "Content-Type": "application/json",
}

data = {
    'inputs': 'What is Deep Learning?',
    'parameters': {
        'max_new_tokens': 20,
    },
}

# call potassium server, which calls TGI
response = requests.post('http://127.0.0.1:8000/generate', headers=headers, json=data)
print(response.json())