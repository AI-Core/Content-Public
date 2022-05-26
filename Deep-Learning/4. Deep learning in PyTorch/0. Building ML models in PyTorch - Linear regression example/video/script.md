- now i'm going to create a linear regression model in pytorch

- to help with that, I've already made a dataloader from a dataset, and got the first batch

- the way we create a model in pytorch is by defining a class

_create NN class with empty init_

- and eventually, we want to be able to use an instance of that class like this

- we want to be able to initialise it to get a model

_Create instance of model_

- and then we want to call that model on some featues to return a prediction

_prediciton = model(features)_

- that's nice because it looks the same as it would mathematically, where we call a function on some variable

- so now we need to define those two behavious

- the initialiser defines what happens when the model is created

_Define init method with commend "define layers"_

- and the magic method "call" defines what happens when we call an instance of this class on some data
- you can implement any custom functionality that you want in here

_Define `__call__` method with comment "use layers to process data"_

- let's define the layers first
- pytorch contains classes that represent all kinds of common layers
- for linear regression, we want to use the linear layer to perform a linear combination of the features
- that's the whole model for linear regression
- initialising the linear layer initialises a number of weights and biases
- you have to tell pytorch how many inputs and outputs you expect for each example
- in this case, the number of inputs is goign to be the number of features
- and the number of outputs is going to e how many targets we have for each example
- once initialised, it can be called on a batch of features to compute a linear combination of them by multiplying each of them by a weight and adding a bias
  it simply performs

_define `self.linear_layer` attribute_

- now let's define how this model makes precitions in the call method

- right now, this would work

_Run the script and get a prediction_

# TORCH.NN.MODULE

- but to make things easier later, we can access a bunch of pytorch functionality by inheriting from a class called `torch.nn.Module`

_inherit from torch.nn.Module_

- it gives our model few useful methods and attributes
- it also allows you to define what happens when you call the model with a method called forward, rather than the ugly double underscore call method
  -as well as making things prettier, this makes it clearer that this method performs the forward pass on the data when it is pushed through the model whilst still letting us just call the model on the data
- of course, we should initialise the parent module too

- and there you've got your first pytorch model
