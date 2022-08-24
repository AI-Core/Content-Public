- by their very nature, words are discrete
- words with very similar meanings might look very different in terms of the characters they contain
- if we treat them as totally discrete, by doing something like 1-hot encoding them, then we lose all of that information about words might be similar or different
- we would like to have a representation for each of the words in our text which makes similar words appear similar
- one way we can do that is by representing different words as different points in space, where similar words are closer together
- these points in space are vectors, whose elements are their coordinates
- we call those vectors "word embeddings"

_Show 3D word embeddings graph_

- and graphically, they might look something like this

- with this representation we can meaningfully represent words and compare and contrast different words against each other by comparing their embeddings

- numerically, the word embeddings are a number of vectors, aka a matrix, which we call an "embedding matrix"
- if i had a tiny corpus of just 8 words, with 3 dimensional embeddings, the embedding matrix might look like this

_Show 8 x 3 torch matrix_

- much like the activations of a neural network layer, the values in each position of the vector can represent something meaningful, but it's hard to describe exactly what

- here I am showing 3D word embeddings
- in practice, the embeddings are typically on the order of hundreds
- most typical are 128, 526, and 1024 dimensional embeddings
- as usual, a power of 2 is used to increase cache utilisation and speed things up, as well as narrowing down your options

<!--  OUTRO -->

- so what I've explained here is what a word embedding is
- what I haven't told you yet, is how we get them
