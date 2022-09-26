- For multiclass classification, we typically use a loss function known as the cross entropy
- I won't get into the exact details why just here, because it's very mathematical
- but I'll show you what it looks like and point out some of the important properties

- when we make predictions for multiclass classification problems, we're going to be predicting a probability distribution over all of those classes
- we want to push up the probability predicted for the correct class, the label
- and by doing that, push down the probabilities for the incorrect classes

- and we're gonna attempt to achieve that by minimising a loss function
- so the loss function should be zero when we have perfect predictions, and huge when we're way off

- in a perfect prediction, the probability of the correct class is one, and all others are zero

_mark loss=0 at p(y_hat=y) = 1_

- in the worst case, our loss should be as large as possible

_draw curve asymptotic to p(y_hat=y)=0_

- we can get this curve by taking the -log probability predicted for the true label
- and this is the cross entropy loss function

- it can also be derived mathematically, but I won't go into it here

- you should notice a few important things
- it's smooth and differentiable
- secondly, the probability which you take from the output distribution and put into this function depends on the label for the specific example
- we want to minimise the negative log likelihood for
- we don
- pushing up the correct label


_implement in python_

- this is a really important loss function to understand if you want to be able to build models from scratch or optimise existing ones, because a huge number of problems, can be framed as multiclass classification problems, and are trained by minimising this loss function