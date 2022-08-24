# Classification

- classification is the task of assigning something to a categorical label
- for example
- predicting whether a piece of fruit is ripe or not from an image
- predicting whether a user is going to stop using your product
- or predicting which of your friends appear in a photo

- in both of those cases, the labels are discrete, you can't be somewhere in between

<!-- TODO  -->

## Compare to regression

_Show regression graph then classification graph with one feature_

_Show regression graph then classification graph with 2 features_

- the aim of classification is to draw a line that splits the different classes as best as possible

- we call this line the decision boundary

## Binary classification

- binary classification is the simplest case, where we only have two classes
- true or false
- we call these the positive or negative class
- class 0 or class 1

## Getting a probability

- the way that we typically do classification is by creating models which output the probabilities of each different class

- in this case, we can output a single number
- a probability of the input being a member of the positive class

## True labels

- the true label for mmbers of the negative class is 0
- that's because as members of the negative class, we should have zero confidence in them being a member of the positive class
- the true label for members of the positive class is 1
- that's because, as members of the positive class, we should ideally have total confidence in them being a member of the positive class

- a common mistake is to think that we need to output 2 numbers, one for each class
- but we don't, because the probability of the negative class is always going to be equal to 1 minus the positive class

## multiclass classification

_draw multiclass classification graph_
