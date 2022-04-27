import fastapi
import uvicorn

from api import dob_api
from views import home

app = fastapi.FastAPI()


def configure_routing():
    app.include_router(home.router)
    app.include_router(dob_api.router)


if __name__ == '__main__':
    configure_routing()
    uvicorn.run(app, port=8000, host='127.0.0.1')
else:
    configure_routing()