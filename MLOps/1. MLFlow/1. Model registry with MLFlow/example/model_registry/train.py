import mlflow
import joblib
from sklearn import datasets, linear_model

data = datasets.load_boston()
X = data["data"]
y = data["target"]

# START RUN
with mlflow.start_run():

    # FIT MODEL
    model = linear_model.LinearRegression()
    model.fit(X, y)

    # LOG MODEL TO MODEL REGISTRY
    # joblib.dump(model, 'saved_model.joblib')
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="sklearn-model",
        registered_model_name="sklearn-linear-regression",
    )
