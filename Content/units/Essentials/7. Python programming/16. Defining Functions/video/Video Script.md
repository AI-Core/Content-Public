# Functions

## Setup

### What do i need open?
- VSCode open on the home page
    - `.functions.ipynb` notebook
- Open Browser for googling how to use function with variable number of arguments
- OBS
    

### What recording scenes do I need open?

- Screencapture of vscode with your webcam capture in the corner
- Webcam capture in full screen
- Safari (or any browser) with Google open

## Script

- __`[START SCENE] webcam in full screen`__
    - Here you're going to learn about one of the building blocks in programming: functions
    - A function is a block of code which only runs when it is called.
    - This means that we can define a function, and everything we include inside it won't be executed until we use the function.
    - Functions can take data as inputs, known as parameters
    - And, commonly, it also returns data as result.

- __`[CHANGE SCENE] Open VSCODE - .functions.py`__
- Let's see how this is implemented in Python:
- __`[FIRST CELL] def test_function(param_1, param_2):`__
    - Here we can see the basic syntax of a function
    - The first thing we need to include is the `def` keyword
        - This tells Python that we are about to <font size=+1> _define_ </font> a function
    - Then, we add the name of the function, in this case, we are naming it `test_function`
    - Right next to the function name, we add parentheses, in which we can include the arguments that the function will take. 
        - It is important to remark that functions don't necessarily take arguments
        - Thus, we can leave the parentheses empty
        - However, when defining a function, it must have parentheses after the name
    - And to finish the first line, don't forget about the colon!
    - Inside the function, to define that what we are coding belongs to the function, we add an indentation
    - And we start coding everything we want our function to do
    - Optionally, we can add the return keyword
    - In this case, we are returning the variable `output`
        - If we don't add a return statement, the function will return None. This is called void function, but we will come back to this shortly
    - First, let's see some examples to get a better understanding of functions

<br>

- __`[NEXT CELL] def say_hi():`__
    - In this cell, we have an example on how to define a function
    - Notice that we are not passing any argument to the function, but as mentioned, parentheses are mandatory, so we just leave it empty
    - Now, __`[Press 'Run Cell']`__ when I run this cell, nothing happens, there is no output at all
    - This is because, as mentioned, the code inside the function doesn't run until we ask it to

<br>

- __`[NEXT CELL] say_hi()`__
    - Executing a function is quite straightforward. 
    - Simply type the name of the function and add parentheses.
    - We call this __calling__ the function
    - Observe that the output now reflects the content of the function
        - It prints Hello
        - It prints World
        - It returns 'Good Bye'
    - One common mistake when using functions is not adding the parentheses.
    - Parentheses is the way we have to tell Python that we are calling a function
    - So, if we don't add them, Python will simply give us information about the function

<br>

- __`[NEXT CELL] say_hi`__
    - If we run this, the output shows something rather strange
    - It basically tells that say_hi is a function, but it doesn't give much more information.
    - Thus, when handling functions, don't forget to include the parentheses!

- It's really important to notice the difference between a function, and a function call.
- say_hi is a function
- say_hi followed by parentheses is a function call
- a function call becomes equal to whatever it returns
- another way to say that is that a function resolves to it's return value
- so if you assign a variable to a function call, it will take on the value returned by the function
- in the next cell you can see that, where I'm assigning this variable length equal to what is returned by python's builtin len function

<br>

- The examples we have seen so far don't accept any arguments
- One of the beauties of functions is that they can be used with different arguments and return a different output
- So let's define a function that accepts arguments

- __`[NEXT CELL] get_length():`__
    - This function calculates the length of a string and it will return the number of characters in the sentence
    - Observe that for each sentence, the function returns a different value, 40 and 27
    - That means that, indeed, the function changes its output based on the arguments you pass to it

- Let's use a similar example to explain a couple of things about the `return` keyword
- Now, we are going to define a function that only returns the length of the sentence if the number of characters if lower than 30
- Otherwise, it prints that the sentence is too long

<br>

- __`[NEXT CELL] get_short():`__
    - Take a look at this function:
        - The return keyword is in the if statement
        - In case the condition is not met, it will print that the sentence is too long
        - But if the condition is True, the code in the if statement should run before running the print statement that says that the sentece is too long
    - However, this doesn't happen because once the function hits the return keyword, it exits the function, and doesn't run anything included below that return keyword
    - This can be seen if I run this cell `[RUN the cell]`
    - We are calling the function with a sentence whose length is lower than 30.
    - The output doesn't print anything related to the sentence being too long, meaning that, as soon as the function reaches the return statement, the code exits the function

<br>

- Let's see what happens when the sentence is longer than 30 characters
- __`[NEXT CELL] len_1 = get_short(sent_1)`__
    - In this case, the return statement is never reached
    - The print statement, on the other hand, will print that the sentence is too long
    - However, what happened to len_1?
    - Let's take a look at its value

<br>

- __`[NEXT CELL] print(len_1)`__
    - The value is None
    - This is because, if we call a function that doesn't have a return keyword, it will return None 
    - When a function doesn't return a value, we call it void
    - So, functions stop running as they find the return keyword, and not all functions have to include a return statement

<br>

## Variable scope

- __`[CHANGE SCENE] webcam in full screen`__

    - One important thing with functions is that the variables inside it might be affected by variables defined outside the function
    - But it doesn't happen the other way around
    - We call this Scope
    - The scope refers to which parts of a program will have access to a specific variable
    - In this lesson we will focus on two kind of scope: Local and Global
    - A variable defined <i><font size=+1> inside </font></i> a function, has a local scope, and it can't be reference outside it
    - On the other hand, a variable defined <i><font size=+1> outside </font></i> the function, in the general script, has a global scope, and you can reference that variable inside a function

- __`[CHANGE SCENE] Open VSCODE`__
- __`[NEXT CELL] x = 'I am in the global scope'`__
    - We define two variables, `x` in the global scope, and `y` in the local scope
    - We can see that, when running the cell, first we define and call the function
        - The output shows that inside the function, Python didn't have any issue finding `x`, which is in the global scope
        - And the same goes for `y`, inside the function we have no problem referencing local variables
    - On the other hand, when we print our variables outside the function, the global variable is printed with no issue
    - But when referencing the local variable, it will throw an error because Python won't find it
    - This is because `y` is stored inside the function, and once the function finishes running, `y` is not stored anymore

<br>

- When you have two variables with the same name in different scopes, the local variable will overwrite the global variable, but only inside the function
- Let's observe one example using x in both scopes
- __`[NEXT CELL] x = 10`__
    - As we can see in the code, in the global scope, x is equal to 10, so before calling the function, this value remains unchanged
    - Then, we call the function, and we are changing the local value of `x` to 20
    - So when printing it, its value is 20
    - However, going back to the global scope outside the function, we can see that the value of x is the same as in the global scope
    - Thus, the local scope won't make changes to global scope

## Functions with variable number of parameters

- __`[CHANGE SCENE] webcam in full screen`__
    - So, by now you know that functions can accept a number of parameters
    - However, in some ocassions, you might need to use functions where the number of arguments is unknown
    - Say for example, that you want to create a function that accepts an undefined amount of numbers and returns the mean value
    - Creating a flow control for ALL possibilities would be incredibly inefficient
    - Can we do something to solve it in an efficient manner?
    - As always, I am sure Google has the answer!

- __`[CHANGE SCENE] open the browser`__
- __`[GOOGLE] python functions with variable number of arguments`__
    - Nice, the first answer is from StackOverflow
    - Let's take a look at the answers
- __`[OPEN LINK] StackOverflow "Can a variable number of arguments..."`__
- __`[SCROLL DOWN] go to the first answer`__
    - The first answer says that you can use *args to pass a variable number of input
    - As we can see in the answer, this input will behave as a tuple
    - And the way to pass them to the function is by simply add the value
- __`[SCROLL DOWN] go to the second answer`__
    - It might be worthy check the second answer as well
    - Nice, it looks like it adds information to the first answer
    - We can also use the **kwargs which stands for keyword arguments
    - As we can see in the answer, these inputs will behave as a dictionary
    - And the way to pass them to the function is by passing a key and its corresponding value

- Alright, so let's see an example on VScode
- __`[CHANGE SCENE] open VSCode`__
- __`[NEXT CELL] def test_args(*args):`__
    - In this small example, we can see that we just added *args to the parameters
    - But we can pass as many arguments as we want
    - When calling this function, it prints out the arguments between parentheses, which indicates we are dealing with a tuple
    - Just to check that, we also printed the type of the variable, and indeed, we can see that it is a tuple

<br>

- This might be helpful for example if we want to calculate the mean value of a sequence of numbers
- __`[NEXT CELL] def get_mean(*args):`__
    - In this example, we also use args to get a variable number of inputs
    - We add all the values in the tuple
    - And we divide it by the number of items in the tuple
    - So, returning the mean value of all the values passed to the function

<br>

- The second way to add a variable number of inputs to a function is using the kwargs argument
- The difference is that appart from the value, we have to pass a key
- In the following example we can see that it acts as a dictionary
- __`[NEXT CELL] def test_kwargs(**kwargs):`__
    - So, when we print the value of kwargs, it will print out what it seems to be a dictionary
    - And we can check using the type function

<br>

- __`[NEXT CELL] test_kwargs(1, 2, 3)`__
    - If we try to pass arguments without any keyword, this function will throw an error, saying that the function doesn't accept positional arguments
    - Positional arguments would correspond to those arguments that don't require a key
    - These are expected when we write *args

<br>

- The following example calculates the price of some groceries, and add it a 10% fee
- __`[NEXT CELL] calculate_price(*args, **kwargs)`__
    - We can see that the function accepts both positional and keyword arguments
    - Since args will act as a tuple, we can index it and get the fee
    - and since kwargs act as a dictionary, we can iterate through its items
    - With that we can calculate the total and multiply by 1.1 to calculate the total

## Summary

- __`[CHANGE SCENE] webcam in full screen`__
    - Let's summarize what we learnt in this lesson:
        - You saw how to define functions
        - You learnt how to call functions
        - You learnt how to use the return keyword:
            - Once the function reaches the return keyword, the function finished
            - If a function doesn't have a return statement, it will return None
        - You now know the difference between local and global scope
        - You saw how to use parameters in a function
        - You learnt how to define functions with a variable number of parameters:
            - Using args
            - And using kwargs
    - Now you are ready to start using functions in your code
