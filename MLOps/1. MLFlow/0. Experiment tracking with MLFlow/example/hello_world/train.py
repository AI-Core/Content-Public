from sklearn import datasets, linear_model

data = datasets.load_boston()
X = data["data"]
y = data["target"]
print(X.shape)

model = linear_model.LinearRegression()
model.fit(X, y)
