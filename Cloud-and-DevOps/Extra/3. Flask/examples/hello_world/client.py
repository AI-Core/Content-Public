import requests


# r = requests.get(
#     "http://127.0.0.1:5000/predict"
# )  # make a get request to the local host (look in your hosts file)
# print(r.content)

r = requests.post(
    "http://127.0.0.1:5000/predict", json={"input": 3}
)  # make a get request to the local host (look in your hosts file)
print(r.content)
