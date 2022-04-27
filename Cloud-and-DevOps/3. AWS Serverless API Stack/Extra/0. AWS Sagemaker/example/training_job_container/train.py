from sklearn import datasets, linear_model
import joblib
import boto3

X, y = datasets.load_boston(return_X_y=True)

model = linear_model.LinearRegression()
model.fit(X, y)
joblib.dump(model, "saved_model.joblib")

# upload to s3
s3 = boto3.client("s3")
fn = "saved_model.joblib"
s3.upload_file(fn, "demo-ml-models", fn)
