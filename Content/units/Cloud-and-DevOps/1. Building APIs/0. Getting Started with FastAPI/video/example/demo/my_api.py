import uvicorn
from fastapi import FastAPI

api = FastAPI()


@api.post("/")
def example_handler():
    return {"message": "Hello w"}


@api.post("/")
def get_user():
    # get user attributes
    return {"name": "Harry"}


@api.put("/user/basket")
def put_item_in_basket():
    # put item in basket
    return "Success!"


# if __name__ == '__main__':
#     uvicorn.run(api)
