# Motivation

- A very typical type of problem is one where you want to predict one of many possible classifications
- for example, predicting the species of plant shown in an image
- we call this multiclass classification

# Model format

- here, I've got three logistic regression models
- the naive way to perform multiclass classification would be to havea binary model predicting each class and take the one that's most confident
- but in just a few steps, they can be combined and adapted to perform multiclass classification
- to get multiple outputs, we use a weight matrix instead of a weight vector
- the matrix has size in by out
- the number of outputs is the number of classes which we want to classify from
- typically, this number is denoted as `k`
- `k` different classes
- so y = XW + b is a k-vector
- note that in this case, `b` is also a vector because we have a bias for each output

- if we were to simply take a logistic regression model and change the number of outputs, applying the sigmoid function element-wise to the output, then that would be a multilabel classifier, not a multiclass classifier
- a multilabel classifier outputs a number of independent binary predictions which can all be true, essentially predicting different labels at the same time
- a multiclass classifier outpus a single distribution over multiple labels, predicting one label out of many
- for the output of a multiclass classifier to represent a probability distribution, all of it's calues need to between zero and one, and sum up to one
- to achieve that, we need to apply a softmax function instead of an element-wise sigmoid function
- the softmax function takes a vector of real numbers and turns it into a probability distribution

- so the overall multiclass logistic regression model looks like this

_show model equation_

- it takes in numerical features, and outputs a vector probability distribution over k different classes
- it's still fully differentiable, so it can be trained with gradient descent

- and this is one of the most common models in production today
