## Tuples

<!-- MOTIVATION -->

- tuples are very similar to lists, they are ordered collections of objects
- the difference is that they are immutable
- that is, their contents cant be changed
- because they don't need this functionality, they take up less memory than lists, and can be indexed faster

- if you know that a sequence doesn't need to be changed, then make it a tuple instead of a list

- to define a tuple, use parentheses instead of square brackets

- or you can cast a list into a tuple

_Show `tuple([1, 2, 3])`_

- Tuples are ordered, so we can index them

- if you try to mutate a tuple, you'll get an error

- so tuples can also be useful for raising your attention when you code tries to change something that shouldnt change

- We can actually create tuples without using the parentheses, but it makes it harder to tell what's going on just by looking at the code

_Show `my_tuple = 1, 2, 3`_

_Webcam_

- so don't do that

- one particularly hard to find bugs can be caused by a rogue comma at the end of an assignment

_`my_int = 1,`_

- python interprets this as a tuple with one element, when in reality I wanted it to be an integer

- because brackets are usually used to denote order of mathematical operations, writing something like this actually results in an integer
- if you want it to be a one element tuple, then you need the comma

_add comma and print type_

- tuples aren't super common, but it's usefult o know that you can get some memory and time efficiency gains by using them over lists in situations that makes sense
- and i'd certainly rather you not be surprised or confused when you see something like this down the line
