<!-- words are the atomic unit of text -->

- just like every image is made up of pixels, every body of text is made up of smaller constituents
- you could let those constituents be words, or characters
- we typically use words as the meaningful unit, rather than characters
- that's because characters don't really have much meaning outside of the word that they make up
- for most problems of interest, the same letter doesn't mean the same thing when represented in a different word
- so to
<!--  define tokenisation -->
- so the first step in processing text is to break down the text into discrete tokens, which are typically words
- we call this tokenisation
- so tokenisation is the process of breaking up text into it's constituent parts, which each have a semantic meaning
<!-- different tokenisers -->
- to perform the tokenisation, you would want to do things like split the text on spaces, normalise all of your capitalisation so that a capitalised word is treated the same as its lowercase counterpart, remove spelling mistakes, remove special characters like semicolons, and more
<!-- off the shelf tokenisers -->
- i'm sure you could implement that in python pretty easily
- but to save yourself time, you can also just use one of the many standard tokenisers, which someone else has written and put online
- there are many different publicly available tokenisers
- as an example, the most basic is called the basic english tokeniser
- it lowercases the text
- then it adds space before and after commas, single quotes, periods, parentheses, exclamation marks and question marks so that they will eventually be their own tokens
- then it replaces semicolons or colons with a whitespace, so that they wont be included as tokens
- it removes double quotes
- and then it splits everything on a whitespace
- the result of that is that a body of text is converted to the set of lowercase words and meaningful punctuation which it contains
- like I said, and as the name implies, this tokeniser is very basic, so i'm sure you can think of cases where these rules break down
- one example would be where the letters of an acronym like AI are separated by periods
- the basic english tokeniser would treat the A, the dot, and the I would be treated as different tokens
- because of that, there are much more advanced tokenisers out there too, which for the moment I'll leave you to look into
<!-- example in code -->
- many libraries have built in functionality to get these tokenisers
- in torchtext, you can simply import the `get_tokenizer` method from `torchtext.data.utils`
- then you can create a tokeniser by calling that function with the name of the tokeniser you want to use
- i'll use the basic english tokeniser, which unlike others, you won't need to go and install from elsewhere

_Instantiate basic english tokeniser_

- once you've created the tokeniser, you can call it on a body of text to get the tokens as a list

_Tokenise a sentence_

- and it's as simple as that really: tokenisers convert text into individual tokens which represent the meaningful constituents of your text
  o
