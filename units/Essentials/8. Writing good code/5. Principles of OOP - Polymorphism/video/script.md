- polymorphism is a complicated sounding word used to describe the very simple ability for the same code to behave differently in different situations
- What do I mean by that?

_Switch to screen capture_

- here's an example
- the plus operator can be used to add strings together, as well as add integers together
- but in each case it does something different
- the plus operator behaves differently based on the type of its inputs
- we call this operator polymorphism

_Switch to webcam_

- polymorphism comes from the greek words poly which means many, and morph which means form
<!-- TODO TYPEWRITE DEFINITION poly + morph = polymorphism -->

- that makes sense, right, because polymorphism means that the same code can take many forms of behaviour, depending on the situation

- a physical analogy of polymorphism would be how the behaviour of a person changes whether they are at work or at home
- same person, different situation, different behaviour

<!-- - polymorphism is one of the 4 principles of object oriented programming along with abstraction, encapsulation, and inheritance -->

_Switch to screen capture_

- and this case that we've seen here is one of the benefits of python being a dynamically typed language - you don't need to specify that the type of the input can be any one of the potentially many classes

_Switch to webcam_

- we can also have function polymorphism, where a function behaves differently based on the type of its inputs

_Switch to screen capture_

- the same len function is used to calculate the length of several different data types
- here, a function behaves differently based on the type of its inputs

_Switch to webcam_

- the final type of polymorphism I'll talk about is class polymorphism
- this is where different classes have a method of the same name, and so you can treat the instances of those different classes in the same way

_Switch to screen capture_

- for example, here I have two different machine learning models, which both have a method called predict

_Show classes representing two different machine learning models_

- the canonical demonstration of class polymorphism is where you iterate through a list of items which are instances of different classes, but you call the method of the same name for each of them
- so here, I can make predictions for each of them

- another similar example is the different behaviour exhibited by the a method in one class and the same method in a class which inherits from the other one

_Switch to webcam_

- overall, just remember that polymorphism is a principle that means that the same code (operators, functions, methods, classes etc) can behave differently in different situations
