- Let's focus now on the last element in this video: Generators
- Generators are a special functions that act like an iterator
- We can define them as if we were defining a function but they have a special keyword called `yield`
- Let's see some examples on how to create generators

<br>

- **`[CHANGE SCENE] Open VSCode`**
- **`[NEXT CELL] def my_gen()`**
  - As I mentioned earlier, we can define a generator as if I defined a regular function
  - But just by adding the keyword `yield`, this function becomes a generator
  - In a regular function, when you call it, the function will reach the return keyword and next time you call the function, it will start over
  - In the case of a generator, the Python will execute the generator until it reaches the yield keyword
    - And next time it is called, it will start from the yield statement
  - So, let's run this cell to create a generator and assign it to the variable called `s` **`[RUN CELL]`**
  - We can see that `s` is a generator now
  - We can run the content of the generator using the function `next`, or iterating through it using a `for` loop
  - Let's take a look at the `next` function

<br>

- **`[NEXT CELL] next(s)`**
  - The next function applied to a generator will execute its content and it will PAUSE as soon as it hits a `yield` clause
  - So, when running this **`[RUN CELL]`**
    - The output only shows the first print statement and the output in the `yield` clause: 1

<br>

- **`[NEXT CELL] next(s)`**
  - If we run the next function again on the same generator, Python will start from the last reached yield statement **`[RUN CELL]`**
  - So it prints the second print statement
    - And the output of the second yield statement

<br>

- **`[NEXT CELL] next(s)`**
  - And the same goes if we run it a third time

<br>

- **`[NEXT CELL] next(s)`**

  - Notice that there are no more yield statements
  - So if we try to run it again, Python won't find any additional yield statement
  - And it will throw an error
  - Thus, the generator will return values until it runs out of elements

- The second way we have to get the content of a generator is by looping through it in a for loop

<br>

- **`[NEXT CELL] assigning s again and using for loop`** - One of the benefits of using a for loop in a generator is that it will iterate through all the elements until it exhausts it **`[RUN CELL]`** - But once it runs out of elements, it will stop without throwing any error
  <br>

- **`[NEXT CELL] def inf_gen()`**

  - We can add anything we want to the body of the generator.
  - For example, if we add an infinite loop inside the generator, we can obtain a generator that never runs out of elements
  - In this case, we have an infinite loop that will return values from 0 to infinite
  - And, even though we can obtain infinite numbers, it doesn't take an infinite amount of memory
  - And that is one of the beauties of generators
  - We can have huge iterables that don't take large amounts of memory
  - So, when I run this cell **`[RUN CELL]`**
    - The loop won't stop!
    - But the printed value increases by one **`[STOP THE CELL]`**
  - This happens because it hits the yield statement, and pauses
  - But the generator is called again, so it will increase x by one, and it hits the yield statement again, with a higher value of x
  - This is repeated indefinitely

- This is it for generators. They are a great way to save memory when you want to deal with large lists
- If a list is so large that it barely fits in memory, iterating through it will consume a lot of resources
- But creating a generator will take almost no memory
