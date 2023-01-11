# Dictionaries

<!-- MOTIVATION -->

- i'm sure you know how to use a dictionary
- you have a word in mind that you want to know the detils of
- so you look it up in the dictionary to find the details
- the dictionary maps frm the word to its definition

_pause_

- we call the word you look up a key
- and we call the definition a value

- so Dictionaries are collections of data that are presented in key-value pairs.

- and this type of data structure is really useful for other things, and really common

- you might have barcodes that map to product prices
- you might have a english word which you want to map to a french word
- you might have a user id which you want to map to their attributes
- or a team name which you map to a list of their user ids

- in python, there's a data type which does exactly that, it maps from a key to a value

- funnily enough, the data type is called a dictionary

- and it looks like this

_show dictionary_

- Dictionaries are represented using curly brackets like in this image

- each key is mapped to its value by a comma

- and each key value pair is separated by a comma

- so this dictionary contains n key value pairs

_webcam_

- so whenever I say dictionary from now on, I'm not referring to the book

_screen capture_

- you can get the value of a particular key in a dictionary by indexing it
- and you know when I say indexing, i mean using square brackets like this

_index key from dictionary and assign to variable_

- like lists, dictionaries are ordered and mutable
- they became ordered from Python version 3.6, and it means that the dictionary keeps the order in which keys were added to it
- The mutability of a dictionary means that you can add, remove and change the value of different keys

- this is how you add a new key

_show adding key_

- The keys in a dictionary are unique
- you change the value of a key by overwriting it

_overwrite key_

- the rule is that Keys can't be mutable data types
- most commonly strings

- On the other hand, values can take any type of data and be the same for different keys

- so I could have a dictionary of lists or even a dictionary of dictionaries, however nested I want
- because of that, they can be very flexible and easy to work with
- if you don't know what data type to make something and you're worried about how easy it will be to change later, make it a dictionary

## Accessing Items

- just a note on nested dictionaries
- if you index the top dictionary, that will return you the inner dictionary, so you can index that simply by indexing the result, like so

_show indexing nested dictionary_

- you'll raise a keyerror if the key doesn't exist

- The second way for adding items is using the update method, which accepts another dictionary as an argument.
- Observe in this example that `Colour` didn't exist, so it has been added.
  - On the other hand, `Year` already existed, so its value has been modified

## Remove Items

- Let's see how to do the opposite of adding items: removing items.
- I don't expect myself to remember how to do this
- But I expect myself to be able to find out, so I'm going to search for it
- **`[OPEN BROWSER] Google "python dictionary remove items"`**
- **`[OPEN FIRST LINK] Delete an element from a dictionary - Stack Overflow`**
- **`[SCROLL DOWN TO THE FIRST AND SECOND ANSWERS]` Read the answers out loud**

- Thus, we can see that we can use the `del` Python function with the key to be removed
- Or we can also use the .pop method

- The printed dictionary doesn't have the key that we deleted

## Dictionary methods

- there are loads of cases

- **`[NEXT CELL] car.keys()`**
- The first method is the keys method, which will return a list containing all the keys in the dictionary

_show values method_

_show items method_
