<!-- MOTIVATION -->

- sometimes you want to add a little bit of functionality to a function that already exists

- an exmple that I like to give is: you want to time how long a function takes
- it's the same function, you just want to decorate it with a little extra functionality
- and python gives you a handy way to decorate functions with extra stuff like this, using something called a decorator
- which looks like this

_show typing out a decorator_

- the key thing to take away from this video, is that when you see something like this
- it means that python is wrapping some extra code around the function
- and now when you call that function, it's going to behave a little differently, because it has been decorated
- I say it wraps extra functionality around the function because decorators can put some code before the code in the function
- and they can put some code after the function
- wrapping around it
- in the case of a timing decorator, it would need to start the clock before the function which it decorates, and stop the clock and calculate the time elapsed after the function it decorates

# running on events

- decorators can also be used to run code on certain events
- a useful one, is the `register` decorator from the `atexit` module
- it runs the code when the file terminates
<!-- TODO explain more deeply because this may be confusing as it's not obviosu what code is wrapping the function being decorated -->

# common decorators

- the most common use case of decorators is in decorating methods of classes
- the staticmethod decorators allows you to define methods which don't take in the instance of the class, self, as the first parameter
- the classmethod decorator means that methods can be called as a method of the class itself, rather than as a method of an INSTANCE of the class
- although, when you use a classmethod, they can be used in either way

- you will find decorators in other places too
- and it's great that you're watching this, because in my experience, many developers actually do not know what a decorator is when they encounter one
- so when you see that `@` sign, you'll know what it is

- to make sure you leave understanding the minimum you need to about how they work, i'll take a few minutes to quickly go through the process of implementing the timing decorator

- so how would I go about timing my function if i didn't know about decorators?

- I could fisrtly define a function that calls my function inside
- but now it only works for that one function
- and i'd like to be able to time other functions too
- so i could pass the function in as an argument
- now this function times whatever function I pass to it
<!-- DEFINE FUNCTION WHICH WRAPS AROUND ANOTHER -->

- and I also personally think that this looks very confusing, because it's calling a function, but it doesn't look like it is
- but the bigger problem is now that I can't pass arguments to

- what would be better is if this function returned a new function that wraps our original function with extra functionality
- because of that, we typically call this function the wrapper
<!-- SHOW DECORATOR SYNTAX -->
- it gets returned

- And now I can reuse this timer on many different functions
- but python provides what is known as the pie syntax to do this more compactly

- it can be confusing to start, but here are the key things to remember
- decorators wrap functions with extra functionality
- you can define your own decorator by defining a function
- that decorator must take in a function as an argument
- and return a function
- you define the function you want to
- when you put the pie syntax on the line above a function definintion, the function with that name is overwritten by the wrapped version of that function returned from the decorator

- that's all

<!-- EXPLAIN HOW TO HANDLE ISSUE OF PASSING PARAMETERS -->

- if the function that you want to decorate takes in arguments, and you want the decorated function to take in the same arguments, then you will need to define them in the wrapper function arguments
- a really common mistake is trying to define them in the decorator arguments
- but the decorator only takes in one thing
- that is function which you want to decorate

# outro

- these can get a lot more complicated
- you can look into chaining multiple decorators together
- you can go on to write classes which can be used as decorators
