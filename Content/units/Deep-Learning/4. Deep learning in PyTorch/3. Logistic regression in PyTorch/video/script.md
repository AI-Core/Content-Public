- changing a linear regression model into a logistic regression model for binary classification only requires a few alterations
- here i've got a binary classification dataset and a model, which currently has the linear regression forward pass implemented
- we need to pass the unbounded prediction through a sigmoid function to turn it into a probability
- we can find the sigmoid in torch.nn.functional, here imported as F

_Wrap return from forward in F.sigmoid()_

- we then need to change the loss function
- the binary cross entropy loss function can be found in torch.nn.functional too

_Replace mse_loss with `binary_cross_entropy`_

- and that's it
- the rest of the implementation is exactly the same
- the optimiser and the training loop stay as they were
- just be careful about replacing things like loss functions or network layers without checking the docs
- always make sure you know every line of your code works, like i do
