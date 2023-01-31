import requests
import base64
import json
import numpy as np

payload = np.random.rand(
    1, 4
)  # example features to make prediction on (1 example, 4 features)

r = requests.post(
    "https://u0zhb9rcdd.execute-api.eu-west-2.amazonaws.com/prod/classify",
    data=json.dumps({"payload": payload}),
)

print(json.loads(r.content))
