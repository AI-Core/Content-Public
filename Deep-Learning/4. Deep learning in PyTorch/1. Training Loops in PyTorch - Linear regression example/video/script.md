- here I've got a model that's been initialised with random parameters
- now we need to train it using gradient descent
- in pytorch, we need to implement the steps of gradient descent ourself
- this means we can be much more flexible in defining our model
- but it also means that there are a few more things to remember
- once you've done it a few times, you'll start to find it simple

- typically, you might have a function which does all of the model training

_Define a function called train which takes in a model and call `train(model)` below_

- in here what we will do is loop through the dataset a number of times, that is, a number of epochs

_Add for loop_

- and sample different batches of the dataset

_Add for loop through batch_

- for each batch, we will make a prediction

_Make prediction_

- compare that prediction to the labels to compute a loss

_Compute loss_

- then perform backpropagation to compute the gradients

_loss.backward_

- then take an optimisation step using those gradients

_Add comment_

- The optimisation is a little more involved, so I'll leave that out for now

- but this is the skeleton for the training loops you'll be creating to train neural networks in pytorch
