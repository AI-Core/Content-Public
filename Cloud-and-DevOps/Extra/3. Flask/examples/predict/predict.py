from flask import Flask, request
import json

APP_NAME = 'my_api'
APP_HOST = '0.0.0.0'
APP_PORT = 5000

app = Flask(APP_NAME)

@app.route('/predict', methods=['POST'])
def predict():
	x = request.get_json()['input']
	model = MachineLearningModel()

	try:
		return json.dumps({
			'statusCode': 200,
			'body': model.predict(x)
		})
	except:
		return json.dumps({
			'statusCode': 500,
			'message': 'Internal server error'
		})

class MachineLearningModel:
    def __init__(self):
        pass

    def predict(self, x):
        return 2*x # this is a very simple model

if __name__ == '__main__':
    app.run(host=APP_HOST, port=APP_PORT)