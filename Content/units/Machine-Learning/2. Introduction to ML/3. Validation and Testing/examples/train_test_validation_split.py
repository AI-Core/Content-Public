# %%
from sklearn import datasets, model_selection, linear_model, tree
import numpy as np

X, y = datasets.load_boston(return_X_y=True)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, train_size=0.8)
X_train, X_val, y_train, y_val = model_selection.train_test_split(X_train, y_train, train_size=0.8)

model = linear_model.LinearRegression()

model.fit(X_train, y_train)
model.score(X_test, y_test)


# DECISION TREE

linear_regression_model = linear_model.LinearRegression()
decision_tree = tree.DecisionTreeRegressor()

# TRAIN
linear_regression_model.fit(X_train, y_train)
decision_tree.fit(X_train, y_train)

# COMPARE TO FIND BEST
print(linear_regression_model.score(X_val, y_val))
print(decision_tree.score(X_val, y_val))

# REPORT HOW WELL I THINK THE MODEL IS GOING TO DO
print(linear_regression_model.score(X_test, y_test))
print(decision_tree.score(X_test, y_test))


# %%
