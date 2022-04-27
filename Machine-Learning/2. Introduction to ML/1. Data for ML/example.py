#%%
import joblib
from sklearn import datasets

data = datasets.load_boston()

print(data.keys())

X = data['data']
y = data['target']

print('X')
print(type(X))
print(X.shape)
print(X)

print('y')
print(type(y))
print(y.shape)
print(y)
# %%

from sklearn import linear_model

model = linear_model.LinearRegression()

model.fit(X, y)
# %%
model.predict(X[:10])
# %%
model.score(X, y)
# %%
import joblib
joblib.dump(model, 'saved_model.joblib')
# %%
loaded_model = joblib.load('saved_model.joblib')

loaded_model.predict(X)
# %%
