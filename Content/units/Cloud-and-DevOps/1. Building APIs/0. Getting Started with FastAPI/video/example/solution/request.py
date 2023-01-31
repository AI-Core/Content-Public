import requests

response = requests.get('https://127.0.0.1:8000')
print(response.json())
