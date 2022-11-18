# MOtivation

- what does the word self refer to in python?

_show self in class_

- this is one of those things which in general, i find is really badly explained
- but it's so simple

- firstly, let's just remind ourselves where we find self
- it is passed as the first argument to every method of a class
- but you don't have to pass it in yourself
- python does it for you
- and then it can be used within those methods
- like this

_highlight self being accessed in the class_

- so what is that self?

- if you take away one thing from this video, it should be this
- every time you see the word self, just say "this instance of the class"

- the reason for that is that you can have many different instances of the same class

_create many instances of the player class_

- but when one of them is accessed, python needs to know which instance you are talking about, so that it can apply the function to the right instance

- let's try that out, and I think it will give you an idea of what self is

_explain how every `self` is used in the code_

- when we use the variable self inside an instance of a class, it's talking about itself, that is, this instance of the class

- self is just a conventional name, you could call it whatever you want

_change to `this_instance_of_the_class`_

- but stick with self

_undo the name of self back to self_

- again, overall it's really simple: when you see the word self, just say "this instance of the class"
