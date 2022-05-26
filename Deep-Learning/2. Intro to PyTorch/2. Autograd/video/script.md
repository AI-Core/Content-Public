- so here i've got a simple equation for a linear regression model, and i'm computing the loss using the mean squared error
- the result is a tensor

_Do that computation_

- the most important feature of torch tensors is that they keep track of what mathematical operation they were created from
- this is stored as the tensor's grad_fn attribute

_Print the grad fn for the loss_

- under the hood, pytorch knows the mathematical function, and the corresponding function of it's gradient
- and that gradient tells you how one value will change as the values it was created from change
- the reason why this is important for machine learning is that we need to how the loss will change as the parameters of our model change

- when we differentiate our loss, we want to know by how much chaging each parameter is going to effect it
- the grad function is the function called that gets you that number
- when the grad function is called, it stores the gradient of a tensor in it's .grad attribute

- but right now, its grad is empty because we haven't differentiated anything with respect to this tensor

_print x.grad_

- to get the gradient of something with respect to all the variables that lead to it, we simply call .backward on it

_.backward()_

- what this does, is recursively looks at the variables which contributed to this value, calls their grad function on the values which it was created from, and stores that value in its .grad attribute
- but we don't require gradients for every variable, and we dont need to waste time or compute calculating them
- for example, we can't change the values of the features, so we don't really care about by how much changing them will affect our loss
- so by default, torch only calculates the grads of tensors which have an attribute called requires_grad equal to true
- by default, any initialised values will have requires_grad = false
- which is why i've explicitly set requires grad=true for the weights and bias
- but if any value used to create some variable has requires grad=true, then that variable will also require grad

- tensors that were initialised randomly or just loaded in won't have a grad_function, as they weren't created from any other tensors

_Print feature grad fn_

- so to recap, when i call .backward on a variable, it looks at which tensors created it, and through what operation, and calls the corresponding grad function on those tensors
- then it stores the grad in the attribute of a variable
- then for each of those tensors, if their requires_grad attribute is true, it does the same thing
- and this continues recursively until all of the values that contributed to the variable you differentiated have a .grad attribute assigned, if they require one

- what this means is that we can calculate the gradient of any variable without having to explicity write out the equation to do so each time
- our neural networks can easily have millions of parameters, so we definitely don't want to be writing out the functions to compute their gradients
- and that is the main function of pytorch, to act as a library for automatic differentiation
- we call the system that does this automatic differentiation "autograd"
- and you can use it for differentiation in any context, not just machine learning

<!-- OUTRO -->

- now you know about autograd you're almost ready to start using it for AI
