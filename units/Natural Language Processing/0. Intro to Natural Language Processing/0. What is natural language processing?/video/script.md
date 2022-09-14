- natural language processing is the field of processing text with computers
- it has been used to tackle problems like...
- sentiment analysis, where text is classified by the tone which it describes something (positively or negatively)
- question answering, where the system generates answers to questions
- machine translation, where the system generates the translation of some text in another language
- named entity recognition, where the system identifies
- and many more different tasks
  <!-- TODO why is NLP hard? -->
  <!-- OVERVIEW OF THE PROCESS -->
- to process text, we need to represent it numerically
- that consists of a few steps, which we will go into a lot more detail on
- firstly we need to split up the text into discrete atomic units, typically words
- we call this tokenisation
- then we assign every word in the corpus an integer, building a map between each word and its index in the dataset
- but these indices are totally arbitrary
- we would like similar words to have similar mathematical representations
- so we assign each word to a vector, which we call a word embedding
- we can either learn these word embeddings from scratch or bring pretrained embeddings from elsewhere
- once we have the embeddings, we can process them
- and there are a number of models which we could use depending on the task and other constraints
- they include 1-d convolutional networks
- recurrent networks
- sequence to sequence models
- transformers
- and others
<!-- OUTRO -->
- so let's get into the details
