# Motivation

- if you know that event A is 3 more times likely than event B, and twice as likely as option C, how can you turn that into a probability distribution that shows the chance of each of those outcomes?

- you can use a mathematical function called the softmax

- most commonly, it's applied to the output of a multiclass classification model to turn real numbers into a distribution over different classes

- it transforms a vector of numbers into a vector of numbers between zero and one, which sum to one
- that is, a probability distribution
- the input logits represent an unnormalised probability distribution
- the softmax normalises it, making it a valid probability distribution
- this is the key characteristic of the softmax function

# How it works

- it does that in 2 steps
- firstly, for each element, the sofmax raises e to the power of that number, which makes it positive, as any real number to any power is positive
- this ensures that we don't end up with negative probabilities
- then the softmax divides the result by the sum of those values, to get it as a fraction of the whole
- this ensures that the output adds up to one

# Why the name?

- because of the fact that the output sums to one, increasing one input element pushes down the outputs of all the others
- when the difference between the largest input and the others is significant, the winner takes all
- the largest element is pushed up to 1
- whilst the others are pushed to zero

- in that case, it approximates a binary output with max input equal to one and the others as zero
- this is where the max in the name softmax comes from

- unlike the max function which is discontinuous, the softmax is smooth and differentiable
- when this happens to the input of a softmax, the change is... soft

- so the softmax is soft because it's differentiable and behaves like the max when theres a significant difference in the inputs

# Outro

- the softmax is important to understand becuase it can be really handy when you need to represent or predict a probability distribution over multiple variables
