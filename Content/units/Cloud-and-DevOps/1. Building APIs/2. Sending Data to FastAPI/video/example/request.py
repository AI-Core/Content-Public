# %%
import requests
import json

# %%
response = requests.get('http://127.0.0.1:8000/products')
print(response.json())

# %%
response = requests.get('http://127.0.0.1:8000/products?category=cameras')
print(response.json())

# %%
response = requests.get('http://127.0.0.1:8000/products')
print(response.json())

# %%
response = requests.get('http://127.0.0.1:8000/products/452?category=cameras')
print(response.json())

# %%
response = requests.put(
    'http://127.0.0.1:8000/user',
    # data=json.dumps({
    #     "preferred_name": `"Harry",
    #     "address": "1 Melgrove Lane"
    # })
)
print(response.json())

# %%
