from pickle import GET
from flask import Flask, request
import json

from werkzeug.exceptions import GatewayTimeout

APP_NAME = "my_api"
APP_HOST = "0.0.0.0"
APP_PORT = 5000

app = Flask(APP_NAME)

# API
#     - /admin
#         -POST
#         - metrics
#             - GET
#         - student
#             - GET
#             - attendance
#                 - GatewayTimeout
#                 - post
#     - /user 2
#         - GET
#         - POST


@app.route(
    "/"
)  # defines the function which is the response is returned from at / route
def home():
    return "hello world"


@app.route(
    "/hello"
)  # defines the function which is the response is returned from at /home route
def hello():
    return "<html><h1>yo</h1><p>hi</p></html>"


@app.route("/predict", methods=["POST"])  # GET, POST, POUT, PATCH, DELETE
def predict():
    data = request.get_json()
    print(data)
    data = data["input"]
    prediction = data * 2  # replace with crazy computer vision model
    return json.dumps(prediction)


# @app.route('/with_status_code') # requests to localhost:5000/with_status_code call this function
# def root():
#     return json.dumps({
#         'statusCode': 200,
#         'body': 'yo'
#     })

if __name__ == "__main__":
    app.run(host=APP_HOST, port=APP_PORT)
