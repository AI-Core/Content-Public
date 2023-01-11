- so here, I've got a pytorch model, a dataloader for the diabetes regression dataset, and most of the skeleton for a training loop
- the problem is, that this training loop doesn't actually train the model
- if we run this code, you can see that the loss doesn't go down over time
- that's because we haven't implemented the optimisation step
- the optimiser is an algorithm such as gradient descent, which has a certain rule for updating the parameters based on their gradients
- pytorch contains a bunch of optimisers which all work in the same way
- you can access them through torch's `optim` module
- and I'll define that just inside our train method

_define `optimiser = torch.optim.` just inside the train method_

- here you can see all of the available optimisers including common ones like SGD and Adam
- let's stick with SGD for now

_`torch.optim.SGD`_

- every optimiser requires a learning rate

_pass lr = 0.001_

- every optimiser requires a set of parameters which it will optimise

- you can get all of the parameters of a model by calling `.parameters()` on it
- that method is another thing inherited form `torch.nn.Module`

<!-- STEP -->

- now that we've defined an optimiser, we actually need to use it to optimise the parameters
- we do that by calling it's `.step()` method
- when we do this, the optimiser is going to look through these parameters, and update them using their grad attribute, which should have been populated by an earlier `.backward()` call
- the rule that it uses to update the parameters depends on which optimiser you use
- for example, gradient descent is simply going to move each parameter in the opposite direction to it's gradient proportional to the learning rate

<!-- ZERO GRAD -->

- one thing that you need to be really careful of is that calling `.backward()` doesn't _overwrite_ the value stored in any tensor's `.grad` attribute
- instead, it adds to what is already there
- there are some advanced use cases which I won't get into right now
- but the important thing is that you need to manually reset the grad attributes to zero
- you can do that by calling the `.zero_grad()` method of your optimiser
- if you don't do this, your gradients will just be added to the previous gradients
- those old gradients are no longer relevant, as there were computed when the model had different weights
