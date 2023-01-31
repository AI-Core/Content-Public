import uvicorn
from fastapi import FastAPI

api_instance = FastAPI()


@api_instance.get("/")
def example_handler():
    return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run(api_instance)
