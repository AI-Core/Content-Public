import mlflow
import numpy as np

model_name = 'sklearn-linear-regression'

model = mlflow.pyfunc.load_model(
	model_uri=f"models:/{model_name}/1"
)

prediction = model.predict(np.random.rand(1, 13))
print('predicted:', prediction)