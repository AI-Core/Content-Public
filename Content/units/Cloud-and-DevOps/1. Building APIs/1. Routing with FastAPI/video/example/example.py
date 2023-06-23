from fastapi import FastAPI

api = FastAPI()

product_data = [
    {"name": "headphones", "price": 100.00, "category": "audio"},
    {"name": "GPU", "price": 1000.00, "category": "computing"},
    {"name": "drone", "price": 300.00, "category": "cameras"},
    {"name": "gopro", "price": 400.00, "category": "cameras"}
]


@api.get("/products")
def get_products(category: str):
    # get products
    category.
    return product_data
