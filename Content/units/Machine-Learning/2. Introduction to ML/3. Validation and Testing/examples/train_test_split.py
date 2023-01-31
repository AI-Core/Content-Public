
from sklearn import datasets, model_selection, linear_model
import numpy as np

X, y = datasets.load_boston(return_X_y=True)

X_train, y_train, X_test, y_test = model_selection.train_test_split(X, y, test_size=0.2)

model = linear_model.LinearRegression()

model.fit(X_train, y_train)
model.score(X_test, y_test)