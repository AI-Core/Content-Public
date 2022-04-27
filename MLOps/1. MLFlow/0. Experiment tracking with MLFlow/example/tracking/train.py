from sklearn import datasets, linear_model
import mlflow
import joblib
import argparse
import json

# THIS IS HOW YOU PARSE ARGUMENTS FROM THE COMMAND LINE
def get_flags_passed_in_from_terminal():
	parser = argparse.ArgumentParser()
	parser.add_argument('-r')
	args = parser.parse_args()
	return args
args = get_flags_passed_in_from_terminal()
print(args)

data = datasets.load_boston()
X = data['data']
y = data['target']
feature_names = data['feature_names']

# SET EXPERIMENT
# mlflow.set_experiment('new') # current bug in mlflow

# START RUN
with mlflow.start_run():

	# LOG ARTIFACT
	filename = "features.txt"
	with open(filename, 'w') as f:
		json.dump(list(feature_names), f)
	mlflow.log_artifact(filename)

	# FIT MODEL
	model = linear_model.LinearRegression()
	model.fit(X, y)

	# LOG MODEL
	joblib.dump(model, 'saved_model.joblib')
	# mlflow.sklearn.log_model(
	# 	sk_model=model,
	# 	artifact_path="sklearn-model",
    #     registered_model_name="sklearn-linear-regression"
	# )

	# LOG METRIC
	score = model.score(X, y)
	mlflow.log_metric('R-Squared', score)