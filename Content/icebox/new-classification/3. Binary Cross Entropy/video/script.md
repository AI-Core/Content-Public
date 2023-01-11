## Optimisation

- so far we've only talked about the model, but we still need to train it
- the parameters to start with are going to be random
- as with linear regression, the way to do that is with gradient descent

- but should we use the same loss function?
- we _could_ use the mean squared error
- but if we look at the gradient of the MSE loss function with respect to the prediction...

_Show equation for dL/dw = 2\* (y_hat - y)_

- in the regression problem, it's unbounded, because this error can be any size
- for classification the worst possible error is 1
- so in that case, the MSE gradient doesnt provide a very strong signal, even when the prediction is totally off

_Show the gradient for err = 0.5 and err = 1_

- the gradient when we are as wrong as possible is only twice as big as when we are unsure
- when we are as wrong as possible, we should feel a really strong gradient pushing us away from the current parameterisation

_Switch to webcam_

- so for classification, we should use a different loss function
- we want it to have a high gradient when the predictions are wrong, and have zero loss when the predictions are correct

_Switch to ipad_

- let's do a quick mathematical recap to cover the log function, which is going to be useful here
- as a quick reminder, log base n of x is the power of n which gives x
- so log_2(8) = 3 because 3 is the power of 2 that gives 8

_show log_2(8) = 3 and 2^3 = 8_

- if we leave out the base, we assume that the base is e
- and that is also known as _ln_

- the log graph looks like this

_Show log graph_

- it intersects the x axis at x = 1
- and it's asymptotic at x = 0

- you might notice that it's the inverse of e^x
- ok, we're back from the mathematical recap

- the log function has the properties we want for computing how bad a prediction for a positive example is
- a positive example would have the label one
- so if our prediction is one, and we pass it through a log function, then the function gives us zero indicating that the prediction is perfect
- if our prediction for a positive example is near zero, and we pass it through a log function, then the function gives us a very large number indicating that the prediction is bad

- what about in the case of negative examples, where the label is zero?
- in that case we want the opposite: inputs near zero give us zero output, and inputs near one give us a very large value
- we can again achieve that with a log function by applying a simple transformation
- firstly reflecting the function in the y-axis by negating the input variable
- then by shifting it in the positive direction by adding 1

- we could do a check for every prediction, and have some control flow to determine which of these loss functions is used, but that's inefficient
- instead, we can actually combine them into a single equation which works in both cases

_Show the equation_

- this equation contains both terms
- but the term for the positive label is multiplied by the label
- so in the case where the label is 0, this term will become nothing, and the other one will be used
- when the label is 1, this term will be the same

- because the labels are only ever going to be 0 or 1, they essentially act like a switch, turning on and off the relevant terms

- we call this the binary cross entropy loss function

- it looks complicated, but it's really not when you break it down

## So

- so now we understand

  - the data
  - the model
  - and the loss function

- the final thing we need to cover is the optimisation
- like linear regression, we can optimise the logistic regression model parameters using gradient descent

- but now the model is a little more complicated

_Show the computational graph_

- it's often useful to use these computational graphs to understand how the different variables relate
<!-- TODO move this intro to computational models to the linear regression video ^ -->

- we can use the chain rule to compute the gradient of the loss with respect to the model parameters
- and the computational graph helps to understand the chain of gradients that need to be multiplied

_Show 2 comp graph with backward arrows labelled with gradients for both dLdw and dLdb with equation of multiplied gradients below_

- and with a little calculus we can calculate all of the values we need

_Show a grid of each part of the function and it's derivative_

- then we simply use those values in the gradient descent algorithm
