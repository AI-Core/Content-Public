<!-- MOTIVATION -->

- sometimes you want to add a little bit of functionality to a function that already exists

<!-- DEFINE FUNCTION WHICH WRAPS AROUND ANOTHER -->

<!-- SHOW DECORATOR SYNTAX -->

<!-- EXPLAIN HOW TO HANDLE ISSUE OF PASSING PARAMETERS -->

- **`[NEXT CELL] def timer`**
  - An interesting thing we can do with decorators is measuring the time it took to run a function
  - To do so, we can create a timestamp before calling the function
  - Call the function
  - And finally create another timestamp after running the function
  - The difference between both timestamps will be the time needed to run the function
  - And that difference is printed out whenever we run the decorated function **`[RUN CELL]`**

<br>

- ...
- And now I can use this timer on many different functions

- **`[NEXT CELL] def timer`**

- the problem with this arrangement is that it can get pretty convoluted if our function requires arguments or returns a value we need
- if our function takes in arguments, we would need to pass them in as another argument to this function which adds the decoration
- it would also be convoluted if our function returned something we needed
- we would have to assign it's return to a value and then return that later

- the way around this is to have our function return another function, which the decoration is wrapped around
- inside this function, we'll wrap our original function with the extra functionality
- because of that, we typically call this function the wrapper
- we should then be able to call that returned function in near enough the same way that we used the original function
- so if we call this decorator I've made on our original function, it will overwrite the original function with the wrapper, which calls the original function, but might also add some extra decorating functionality before and after

- **`[NEXT CELL] def timer`**

  - Now that it takes in a function, and returns a function, it's a decorator
  - And when in this format, Python let's use decorate functions in a much more convenient way, often named as pie syntax
  - This syntax consists on add an @ symbol and the name of our decorator right before defining our function
  - And next time we use the decorated function, it will use the extended functionality we defined in the decorator
  - So, for example, if we use this syntax on a function called `wave_hand`
  - If we simply call `wave_hand` it will executed the same as if it were decorated **`[CELL RUN]`**
    - Because in fact, thanks to this syntax, IT IS decorated

- **`[NEXT CELL] wrapper with arguments`**

  - note that if your decorated function takes in arguments, you'll need to define them in the wrapper definition, not in the decorator definition
  - the decorator only takes in one argument - the function which it will redefine
  - this can

- **`[CHANGE SCENE] open webcam in full screen`**
  - Decorators are an extensions of the functions we create
  - Its syntax go beyond what we saw in this video
  - But the most important thing to remember is what they do behind the scenes
  - You will see that Python has many useful decorators that can use
    - Including some decorators that can be used on classes and their methods
    - But we are not going to see those yet
