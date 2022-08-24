- so we can get a binary classification model by simply applying a _sigmoid_ function to a linear model

_Show sigmoid applied to linear model_

- we call this machine learning model _logistic regression_

- it's important to notice, that even though the curve of the hypothesis is not straight
- this is still a linear model
- that's because the input to the sigmoid is a linear function

- that is, the output changes proportionally to the change in the value of a feature
- we call the output of the linear function, the logit
- it's represents an unnormalised probability value
- when the logit is exactly zero, the classification is 50/50

_Show sigma(0) = 0.5_

_Show dotted line above from where input = 0_

- we call this the decision boundary
- on one side of the decision boundary examples are classified as positive, and on the other side, negative

## How does the hypothesis look when predicting from multiple features

- what happens when I have multiple features, and I'm processing multiple examples in parallel?
- the two features are weighted and summed up, then shifted by the bias to produce a scalar for each example

_Point to the logit size_

- multiple features come in, one comes out
- that's exactly the same as in linear regression

- then I apply a sigmoid
- which turns that output into a probability for each example

\_Scroll to empty x-y grid

- here I've got a 2d feature space
- and the vertical axis represents the classification probability
- so what does this surface look like?
- well we know that the output of the sigmoid is going to be
  near 1 when the input is very positive, and near zero when the input is very negative
- and it's going to be 0.5 whenever the input is zero

_Write xw + b = 0_

- And for each example the weighted sum looks like this

_Write $x_1w_1 + x_2w_2$_

- so let's find out where the input is going to be zero

_Assign the linear combination to zero_

- let's consider where it intercepts each axis
- when the second feature is zero, we can rearrange it like this to get the value of x1

_Rearrange to get value of x1 where x2 = 0_

_Write @x_2 = 0, x_1 = -b / w_1_

_Mark that on the graph_

- when the second feature is zero, we can rearrange it like this to get the value of x1

_Rearrange to get value of x2 where x1 = 0_

_Write @x_1 = 0, x_2 = -b / w_2_

_Mark that on the graph_

- and we can see that the equation can be arranged to give a straight line relationship between the two features

\_Write x_1 = - (w_2 / w_1) x_2 - (b / w_1)

- that means that these two points are connected by a line like this

_Draw line on grid_

- that's the decision boundary
- any number on one side of it will be classified as the positive class

_Draw + on RHS_

- any number on the other side of it will be classified as the negative class

_Draw - on RHS_

- so if we take a slice of the hypothesis surface along where x2=0
- it will look like this

_Draw sigmoid above x1 axis_

- and the same for the other axis
- and interpolating between these two linearly gives you the surface you would see if you actually computed the hypothesis for each one

- this visualisation better helps to understand the limitations of logistic regression as a linear model
- the decision boundary is always a straight line

_Switch to webcam_

- if examples from the different classes can't be separated by a straight line, we say that they are not linearly separable

_Switch to screen capture_

_Show examples that cannot be linearly separated_

_Switch to webcam_

- Many problems of practical interest cannot be well separated by a straight line
- however, many problems _can_ be solved by logistic regression
- and although more complex nonlinear models are becoming more widely used, it seems that most models deployed in the real world right now, are binary classifiers like this
- linear classifiers aren't likely to be able to solve image classification problems, but given the right features, they can probably predict if you are likely to stop using a product, or upgrade your plan,

_Switch to screen capture_

_Show graph with x-axis label "Number of times visited upgrade page" and y-axis label "probability of upgrading"_

- at least well enough to be useful

_Draw another datapoint which makes it linearly inseparable_

## Another visualisation

- really, a better way to think about visualising a classifier is as a grid of possible feature combinations covered in numbers which represent the classification probability

_Show such a grid_

- essentially every point in space is mapped to a number
- this visualisation extends more easily into higher dimensions too

_Draw 3d grid with large grid cells for clarity_

- Here again, it's easy to imagine that each position in this 3d space, which represents an example with features equal to those particular values, would be mapped to that probability

- another useful visualisation is to imagine that the feature space is filled with color. and it's darker where the numbers are larger

_Switch to webcam_

- Notice that...
- in a 2d feature space, the decision boundary was a 1d line
- in a 3d feature space, the decision boundary was a 2d plane
- in higher dimensionsional n-d space, the decision boundary is what we call a hyperplane
- it still has n-1 dimensions
- but it's hard to visualise

- Regardless of the dimensionality of the feature space, the maths behind the model is the same
- just like it was for linear regression
