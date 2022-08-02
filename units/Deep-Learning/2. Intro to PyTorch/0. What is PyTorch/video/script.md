- pytorch is a python library for creating and training deep learning models
- it's called pytorch because it is a version of a library called torch which existed in a language called lua, that was ported over to python
- when we say torch though, you can assume we're talking about pytorch
<!-- KEY FEATURE -->
- the key feature is that by keeping track of how each variable in each part of any calculation relates to each other, it can use those relationships to calculate the rate of change of any one of those variables with respect to any other
- this is known as automatic differentiation
- and the reason why that's important is because the rate of change of the loss with respect to each model parameter is used to update that parameter whilst the model is being optimised with gradient descent
- to use this automatic differentiation we will need to store our numerical values in a datatype called the pytorch tensor
<!-- OTHER FEATURES -->
- building on top of the torch tensors, pytorch provides different python classes for initialising layers of neural networks, and tying them together
- it also provides many functions for common mathematical operations used in deep learning such as the sigmoid

<!-- INSTALLING -->

- before we start using pytorch we need to install it

_Show running `pip install torch`_

- then we can import it into our python scripts as torch

_Show `import torch` at the top of a python script_

<!-- OUTRO -->

- so that's enough of an overview
- let's get into the details
