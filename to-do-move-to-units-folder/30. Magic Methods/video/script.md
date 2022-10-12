- you might have noticed that some class methods, like the initialiser, in python have funny names which start AND end in double underscores
- you might have seen others like `__len__`, `__getitem__`, or `__repr__`
- this isn't just for fun
- it means something special

- but I find that people have a hard time explaining what it means
- really, it's as simple as this:
- methods starting and ending with double underscores define the behaviouro some particular syntax
- for example, the `__init__` method defines the behaviour for putting parentheses after a class name
- that is, it defines the behaviour for initialisation

- we call these methods magic methods
- again, the key explanation you need to remember is:
- magic methods define the behaviour for a particular syntax

- python recognises several different magic methods

## len

- the `__len__` method defined the behaviour for what is returned when you call python's builtin len method on it

## str

- the `__str__` method returns what the string representation of the object should be
- and by default that's what's shown when you print the object

_print(book)_

## getitem

- the getitem method defines how an object is indexed with square brackets

# motivation

- before you implement these methods, that syntax will either do the default behaviour, which probably isn't useful in you case
- or it will throw an error
- what's important to notice is that you can implement these methods _however_ you want
- so whatever behaviour makes sense in the case of the object that you are trying to model
- and this is one of the key points of object oriented programming
- it let's you totally customise the behaviour of your custom datatypes

# exploring other magic methods

- and there are many others
- you can see a full list of the magic methods online

_go [here](https://docs.python.org/3/reference/datamodel.html#basic-customization)_

- there are methods for defining how mathematical operators should be applied to the object
- there are methods for defining how to represent the daa in bytes
- or apply string formatting
- or whatever other syntax python has

# outro

- if you're still with me, then you understand python better than i think most people do
- and if you understand these magic methods, you'll be able to take your code to the next level and model the entities that appear in your use case in a way that's much more useful
