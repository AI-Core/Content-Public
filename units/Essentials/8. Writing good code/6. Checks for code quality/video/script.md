- so here's a brief checklist of what you might want to run through to check your code
- number 1. check consistency
- be consistent with your variable naming
- be consistent with the different variable names you've used to refer to the same thing
- be consistent with the kinds of things you've put into functions
- number 2. make sure your variables are named clearly
- no variables called X or Y
- no acronyms
- don't sacrifice readability for variable name length
- number 3
- check that you've used abstraction to show the user the right level of detail
- but don't abstract away too much that useful functionality is hidden
- number 4
- check that you've used inheritance where appropriate
- number 5
- check that you've encapsulated together any related functionality under an unbrella class or file
- number 6
- use polymorphism if appropriate, although the chance for this to appear is less common
- to do that, check that you've made any methods that do the same thing for similar classes have the same name
- familiarity with one of them then allows a user to easily use the other, without having to think about it
<!-- TODO implement lesson for # 7 -->
- number 7
- take the time to think about where you might be doing things inefficiently
- profile your code if you need to
- number 8
- make sure you haven't had to repeat code. keep it D-R-Y. Don't repeat yourself.
- number 9
- make sure you're following the conventional python style guidelines outlined in PEP8
- use snakecase for variable and function names
- use pascalcase for class names
- whitespace on either side of any equal sign, except for defining keyword arguments or their defaults
- follow all commas with whitespaces
- and so on

<!-- OUTRO -->

- if you do all those 9 things, then you can be confident that your code is better than most
