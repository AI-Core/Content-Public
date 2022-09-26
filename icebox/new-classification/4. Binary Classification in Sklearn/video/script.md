## Sklearn demo

- it's a great exercise to implement this from scratch, but in practice you don't need to
- libraries like sklearn perform all of that under the hood

_Switch to screen capture_

- We can implement logistic regression using the **`sklearn.linear_model.LogisticRegression`** class
- Let's use it on the breast cancer dataset that we can also download from the **`sklearn.datasets`** module
- After training the model, we can see that the model predicts the class of the sample as the one with the highest probability
- Notice that the model can return the prediction using the predict method
- Or the probability that the sample belongs to each class using the predict_proba method
