- popeline function
- several pre-build pipelines
  - sentiment-analysis
  - zero-shot classification
  - text generation
  - fill-mask
  - question answering
  - summarisation
  - translation
- you can specify the model in the pipeline
- when initialising or calling different pipelines you can specify kwarg arguments to change their behaviour
  - specify model in text generation
  - specify top_k in ner
  - grouped-entities
- create and instance of it

- types of transformer models
- auto-regressive models like GPT
- auto-encoding models like BERT
- sequence-to-sequence models like

# transformers

_show transformer diagram_

- encoder on the left
- decoder on the right
- encoder creates embeddings using bidirectional self-attention
- the decoder also takes in text
- it is unidirectional and typically autoregressive
- it uses masked self-attention
- combining them gives a encoder-decoder architecture
- also known as seq-to-sqe
- the encoder gives a high-level output which it shares with the encoder
- the encoder then produces a prediction which it stores and uses to make the next predictions

# encoders

- BERT is the most popular encoder model
- encoder generates an embedding of each word
- 768 for bert by default
- the representations are not just isolated embeddings, but are contextualised based on the surrounding words
- all of the context contribute to the value of the embedding
- so they represent the meaning of the word within the text
- encoders are extremely powerful for generating these embeddings
- encoders can be used for many tasks
  - sequence classification
  - masked language modelling
    - one of the ways that BERT was trained
    - bidirectionality is important for providing context

# decoders

- similar to encoders but typically little worse performance
- GPT(2/3?) is a decoder
- they generate an embedding for each word
- decoder uses masked self-attention
- this is because it is not bidirectional
- they are autoregressive
- the mask hides the context in one direction
- hence the representation of each word does not contain information from the hidden context
- we typically call the hidden context the right or left context
- they are powerful for problems where the right-context is hidden such as causal language modelling

# encoder-decoder architectures

- T5 is an example
- the encoder encodes the prompt and passes it to the encoder
- decoder receives output of encoder as well as the start word
- ENC-DEC can handle sequence to sequence tasks including tasks where num inputs number of inputs and outs can be differetns
- such as translation or summarization
- dec does not have to share weights with enc
- you can pull different combinations of enc-decs off the shelf

# What happens in the pipeline?

- tokenisation
- model
- post processing

## tokenisation

- source text is split into tokens
- special tokens are added
- special tokens are mapped to word index

## automodel

- `from transformers import AutoModel`
- can load weights from a checkpoint
- creates model without finetuned head layer
- takes tokenised input
- last_hidden_state.shape = [B x seq_len x hidden_size]
- there are also more specific models used for tasks called AutoModelForX where X is a common NLP task
- `from transformers import AutoModelForSequenceClassification`
- every model outputs logits, not predictions
- this clssifier model is binary
- `model.config.id2label`
- every part of the pipeline can be adapted to your specific task

### autotokeniser

- autotokeniser can take weights from a pretrained model checkpoint
- sentences can be padded so that they're all the same length
- truncation=True trims off the ends of sentences that are too long
- tokeniser returns dictionary of token ids and attention mask which shows which words have been masked

# Models

- AutoModel infers the architecture from the pretrained weights you ask it to take on
- automodel gets the model config from a file, including which class should be used, meanwhile, it gets the model weights from a model file

- you can get the config for any model in the HF library too by importing things like BertConfig for example
- you can get pretrained weights by calling this class's from_pretrained classmethod
- then you cn load this into a BertModel

## saving a model

- model.save_pretrained(saved_model_name)
- model.from_pretrained is the opposite of save_pretrained (it loads in instead of saves weights)

# tokenisation

## word based tokenisation

- splits on spaces and punctuation
- some punctuation is removed
- limitation: plurals being represented differently
- limitation: vocab becoming very large
- we can limit the number of words in our text, typically taking the top n most common words
- limitation: multiple words are represented as the UNKNOWN token
- this results in a loss of information as different unknown words are represented as the same token
- you don't want your tokeniser to be producing inputs where many of the characters are special characters, like [UNK]

## cahracter based vocabularies

- languages all have less characters than words so vocabularies stay small
- limitation: but characters typically hold less information than words
- limitation: sequences can become very long, as most words contain multiple characters
- solves some of the limitations of word based tokenisation

## subword-based tokenisers

- a middle ground between word and character based tokenisers
- frequently used words are not split
- rare words are broken down into different parts of words which are tokenised individually

- words are split into
- subword tokenisation algorithms typically have ways to indicate completions e.g. BERT ##ization
- many algorithms for sub-word tokenisation algorithms
  - BERT, DistilBERT uses the word-piece alrogithm
  - XLNet, ALBERT use unigram
  - GPT-2, RoBERTa use byte-pair encoding
-

- tokeniser.tokenise() takes in a string of text and returns a sequence of tokens
- when you get a tokeniser tokeniser.from_pretrained
- tokenizer.decodde takes in ids and returns a string of decoded ids to show the words they represent

# Batch processing text

- tokenizer.pad_token_id gives the id of the token that should be used to make all sequences the same length
- but you don't want the transformers to contextualise the other words in the context of the padding tokens
- so we give the model what is known as an attention mask
- it's a binary tensor with the same shape as the batch of tensors, it has zeros where padding tokens have been inserted, and ones everywhere else
- it tells the model whether to pay attention to the token in each of those positions or not

<!-- TODO find where best to put this in -->

- most transformers have a limitation to the number of words that you're allowed to pass in as input because of the way that the self-attention mechanism scales quadratically with the sequence length

# TODO what is self-supervised data?

# TODO what are zero shot predictions?

# TODO what is NER?

<!--
TODO remove below in place of huggingface replacing as standard
 # What is Torchtext?

- NLP datasets
- text processing pipelines
- NLP operators

## Datasets

#

# Typical workflow

- preprocessing
  - define in fields
- file loading
  - use tabularDataset
- bucket iterator for batching and padding
- numericalisation
- embedding lookup

# creating a dataset

- be careful of the deprecated docs which still show up in search

- build vocab from training dataset which was created from fields
  - sets a .vocab attribute of each field
- compare situations when you might build from iterator vs from tabular

  - iterator: many large files too big to open and store in RAM

- create iterators from BucketIterator
- why? so you can ierate through them and pad them

- using pretrained GloVE in build_vocab -->

# TODO what is spacy?

# TODO insert glove embeddings into model building a model

# TODO other tokenizers from spacy and what they do

# TODO JIT

# TODO torchscript

# TODO distributed training
