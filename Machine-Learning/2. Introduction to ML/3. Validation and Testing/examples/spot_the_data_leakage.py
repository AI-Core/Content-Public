from sklearn import datasets, model_selection, linear_model
import numpy as np

X, y = datasets.load_boston(return_X_y=True)

X_mean = np.mean(X, axis=0)
X_standard_deviation = np.std(X, axis=0)
X = (X - X_mean) / X_standard_deviation # normalise all values in the dataset

X_train, y_train, X_test, y_test = model_selection.train_test_split(X, y)

model = linear_model.LinearRegression()

model.fit(X_train, y_train)
model.score(X_test, y_test)