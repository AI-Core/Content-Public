import requests
import base64
import json

with open("angry-dog.jpg", "rb") as f:
    payload = f.read()
    payload = base64.b64encode(payload)
    payload = payload.decode("utf-8")

r = requests.post(
    "https://u0zhb9rcdd.execute-api.eu-west-2.amazonaws.com/prod/classify",
    data=json.dumps({"payload": payload}),
)

print(json.loads(r.content))
