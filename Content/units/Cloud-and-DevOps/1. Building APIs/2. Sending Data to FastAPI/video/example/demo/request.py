import json
import requests

response = requests.post(
    'http://127.0.0.1:8000/user',
    # data=json.dumps({"preferred_name": "Harry"})
)
print(response.json())
