import requests

response = requests.get(
    "http://127.0.0.1:8000/products?category=cameras&min_price=hello")
print(response.json())
