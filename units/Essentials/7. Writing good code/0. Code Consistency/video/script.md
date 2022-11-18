- consistency is the key to writing good code

- many people will argue about what is best practice, but whichever conventions you choose, everyone will agree that you need to stick to them and be consistent

- here's a few examples of things that should be consistent

- firstly, the case you use should be consistent within a single variable name

_Switch to screen capture_

- this is awful
- don't have some spaces removed, some replaced by underscores, and some removed and capitalised

_Correct variable name_

- variable case
- don't use snake case somewhere and pascalcase in other places

_Show snake case and pascal case_

<!-- - the style of your comments -->

- variable name choice
- if you've got a variable called users, and another variable that counts the number of users, don't call it playercount, call it usercount
- in that case I'm being consistent with the word "users"

_show both variables and replace `playercount` with `usercount`_

- if you put some code in a function, then code of similar size and functionality should also be put in a function

_Show moving standalone code into a function_

- this should all be in a function, like the similar code that calculates the min

- be consistent with the libraries you use
- if you need bar charts and scatter charts, then use a library that can handle both
- this makes it easy for anyone looking at your code to find anything related to graphing by looking for one library

- if you have to perform a similar operation in several places, use a similar implementation

- I could give many more examples
- all of this keeps your code simple and makes it easy to navigate not only for yourself, but for others too
- when things are consistent, you can take shortcuts by assuming that similar things will be implemented similarly

<!-- OUTRO -->

- in summary, be consistent everywhere that you can be
