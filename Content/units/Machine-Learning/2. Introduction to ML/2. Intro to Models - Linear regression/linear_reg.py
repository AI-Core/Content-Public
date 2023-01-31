# %%
from sklearn import datasets
import numpy as np

X, y = datasets.load_boston(return_X_y=True)

print(X.shape)
print(y.shape)
# %%

class LinearRegression:
    def __init__(self, n_features) -> None:
        self.w = np.random.randn(n_features)
        self.b = np.random.randn()

    def fit(self, X, y):
        pass # compute analytical solution
            # batch our examples
            # for batch in batches
            # pred = self.predict(X) # make predictions
            # loss = self._get_mean_squared_error_loss(pred, y) # compute loss and print    
            # print('Loss:', loss)

    def predict(self, X):
        return np.matmul(X, self.w) + self.b

    def _get_mean_squared_error_loss(self, y_hat, y):
        return np.mean((y_hat - y)**2)

    
# %%
linear_model = LinearRegression(n_features=X.shape[1])
linear_model.fit(X, y)
linear_model.predict(X)
        
# %%
