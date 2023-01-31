from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

api = FastAPI()

product_data = [
    {"name": "headphones", "price": 100.00, "category": "audio", "id": 361},
    {"name": "GPU", "price": 1000.00, "category": "computing", "id": 406},
    {"name": "drone", "price": 300.00, "category": "cameras", "id": 522},
    {"name": "gopro", "price": 400.00, "category": "cameras", "id": 452}
]


@api.get("/products")
def get_products(category: Union[str, None] = None, min_price: float = 0.00):
    print(min_price)
    print(category)
    if category:
        return [p for p in product_data if p["category"] == category]
    else:
        return product_data


@api.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    print(product_id)
    return


class User(BaseModel):
    preferred_name: str


@api.post("/user")
def insert_user_data(user: User):
    print(user)
    # insert into user database
    return
