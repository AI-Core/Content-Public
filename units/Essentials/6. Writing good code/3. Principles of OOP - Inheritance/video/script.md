- inheritance allows you to compose functionality of different classes together without repeating code
- that means that if several classes have similar functionality, then they could both inherit methods and attributes from a class which has the methods common to both of them

_Switch to screen capture_

- in python we do this by putting the name of the parent class which all the methods and attributes will be inherited from in parentheses after the subclass' name definition
- then we can access any of those methods or attributes in the subclass

<!-- DEFINITIONS -->

- the class which inherits from another is referred to as a subclass, or a child class
- the class which is inherited from is referred to as a parent class

<!-- OVERWRITING METHODS -->

- methods or attributes defined in a class can be overwritten by defining them in the subclass

<!-- SUPER -->

- in most cases, we need to initialise the parent class during the initialisation of the child class
- so access the methods and attributes of the parent, we can call python's builtin function
- it returns you an object which has those methods and attributes

- so to initialise the parent class we can access it's init method from the super call, and call it

- note that we could use the super method to call _any_ method of the parent class in the same way we've done with the super method here

<!-- NESTED INHERITANCE -->

- you can also have nested inheritance where a parent class also inherits from another and so on
- this

<!-- MULTIPLE INHERITANCE -->

- although it is not too common, it is possible for a python class to inherit from multiple other classes
- this is called multiple inheritance
- to do that, you simply separate the different parent class names by a comma
- because multiple inheritance is pretty uncommon, I will leave you to play around with what overwrites what there

<!-- OUTRO -->

- in summary, use inheritance to better model your code by separating out the different components into their own classes and to minimize repeated code
