- simply put, encapsulation is capturing related functionality under the same umbrella
- because everything related is encapsulated in the same place, it makes code easier to develop and maintain both for you and others

- one way that you should do this is by grouping together related functions as methods of a class

- let's get a feel for what that might look like in practice

_Switch to screen capture_

_Group `get_data` and `insert_data` methods under class called `Database`_

_Group `remove_duplicate` and `remove_missing` functions under class called `DataCleaner`_

- this makes is so much clearer what relates to what

- another way you can encapsulate things together is by putting them within the same file
- this is especially useful if your file is getting big enough to be confusing
- or it can be useful in this case, where the functions don't depend on any internal state

_move functions out of one file_

_import module into another file and then call module.function_

- you can even encapsulate separate variables, functions, and classes together under the same file

- to take things even further, I could put the class in its own file
- and if I had related classes I could encapsulate them both in the same file too

- at the end of the day there are many ways to implement the same functionality
- but your code might be small enough that it's already really easy to understand what's going on, and breaking it up would just confuse things
- overall you can pretty much always follow the heuristic of doing whatever makes your code easier to read and use
- in my case, the file was so small that it might have been easiest to just keep everything together how it started
- that might lead you to _a combination_ of encapsulating related things within classes and files
- it depends on your style, just be consistent

<!-- TODO SPLIT PROTECTED AND PRIVATE METHODS OUT INTO ANOTHER LESSON -->

- another thing encapsulation can be useful for is preventing the code being used in a way that it shouldn't be

- python allows us to indicate that methods or attributes should not be accessed outside of a class
- we call these protected methods or attributes
- and we incidate to any developer or user that they are not supposed to be accessed from outside the class definition by prefixing their name with an underscore

_highlight the private method_

- it's important to note that these methods are only "protected by convention"
- they _can_ still be accessed by including the underscore when referring to the name

- So they should not be used here

_Access protected attribute outside of class definition_

- we're relying on the fact that developers know that the signle underscore prefix means that they should not be used outside

- because they _can_ be accessed, it means that these protected methods can still be accessed by any subclass which inherits from this class

_Define subclass with method which prints protected attribute_

_Create instance of subclass_

_Call method_

- if you really want to ensure a method or attribute cannot be accessed outside the class it is defined in, even by a subclass, then you can prefix its name with a double underscore
- we call this a private attribute
- when you define this class, python mangles the name and replaces it with something
- so even if you try to access the attribute, then

- this can be used to prevent variable name clashes between subclasses and parent classes
- you wouldn't want to inherit from one class and overwrite an attribute which you didn't know is used in an important method of the parent
- so the attribute in the parent should be implemented as a private attributes

- you may hear that in Python, private methods are not really private
- that's true
- if you look under the hood at the name of the attributes of a class with private attributes
- you can see the name of the attribute
- it's been turned into a combination of the name of the class and the attribute
- if you really wanted to, you could access the attribute using this name

_Switch to webcam_

- the attitude in python is "if you have looked into it and you understand it, then you are free to do what you want"

- so in summary, you should use encapsulation to group related things together

<!-- TODO highlight difference between private and protected attributes -->
