from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

api = FastAPI()

product_data = [
    {"name": "headphones", "price": 100.00, "category": "audio", "id": 361},
    {"name": "GPU", "price": 1000.00, "category": "computing", "id": 406},
    {"name": "drone", "price": 300.00, "category": "cameras", "id": 522},
    {"name": "gopro", "price": 400.00, "category": "cameras", "id": 452}
]


# @api.get("/products")
# def get_products():
#     """Gets all products"""
#     # get products
#     return product_data


# @api.get("/products")
# def get_products(category):
#     """Gets all products within a certain category specified in the query string"""
#     print(category)
#     products = [p for p in product_data if p["category"] == category]
#     # get products
#     return product_data


@api.get("/products")
def get_products(category=None):
    """Gets all products within a certain category specified in the query string"""
    print(category)
    if category:
        products = [p for p in product_data if p["category"] == category]
        return products
    else:
        return product_data


@api.get("/products/{product_id}")
def get_product_by_id(category, product_id):
    """Gets a product by its id"""
    print(category)
    print("product id:", product_id)
    for product in product_data:
        if product["id"] == product_id:
            return product


class User(BaseModel):
    preferred_name: str
    address: str


@api.put("/user")
def put_user(user: User):
    print(user)
    # insert user object into database


if __name__ == '__main__':
    uvicorn.run(api)
