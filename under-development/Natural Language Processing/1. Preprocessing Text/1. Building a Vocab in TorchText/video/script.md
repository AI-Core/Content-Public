- the first step in converting text data into numerical data, which can be processed by mathematical machine learning models, is to create a mapping between the tokens of the text (typically the words), and an integer
- we call this mapping between token and index a "vocab" or vocabulary
- really, the index is arbitrary - it doesn't tell you anything about which words are similar
- typically, the next steps involve learning or downloading richer vector representations of each word, known as embeddings
- stacking those vector representations for every word in the corpus gives a matrix
- and the vocab is useful because it allows you to map the word to an index, and then you can index that row of the embedding matrix to get the word embedding

<!-- example in pytorch -->

- you can create a vocab from an iterator using torchtext's `build_vocab_from_iterator` method

_Code `from torchtext.vocab import build_vocab_from_iterator`_

- the method takes in an iterable which gives lists of tokens as you go through it

- here i've got an iterable list of sentences, which i could have generated from a dataset
- in practice, you would probably load these sentences in on the fly in the generator rather than having them all in a variable in advance, as many text datasets will be far too big to fit in memory

- when you call this method, it basically iterates through all of the examples of text and builds a set of unique tokens and assigns an integer to each to produce a mapping between them

- the vocab generated has dictionary-like functionality
- so you can index it to get the index for any word in the vocabulary

_index vocab with word_

- it also has a bunch of other useful functionality including a lookup the ability to go the other way and look up word from index, which will probably be useful when evaluating results
- on top of that it has things like a state dictionary, so you can save this mapping just like the parameters of another torch layer
- it has methods to move the mapping to GPU or CPU
- and more

- a mistake here would be just iterating through the sentences, without first having tokenised them

<!-- OUTRO -->

- so to recap...
- a vocab is a mapping between each token and an index
- the vocab is going to be useful because we will use the word index to index the row of an embedding matrix to get the representation of the word as a vector
