## Sets

- The second type of object we will see are sets
- **`[FIRST CELL] s = {0, 1, 2, 3, 4, 5}`**:
  - Sets are also used to store a series of elements. However, sets only store unique values, meaning that they will not have repeated values
  - We can define a set using curly brackets

<br>

- **`[NEXT CELL] s = set([0, 1, 2, 3, 4, 5])`**:
  - Or we can define it using the set function

<br>

- **`[NEXT CELL] s = set([0, 1, 2, 3, 4, 5, 1, 1, 1 , 1])`**:
  - If we convert a list with repeated values into a set, it will automatically remove repeated values
  - We saw that lists are ordered, so you could index a list to get a specific item in it.

<br>

- **`[NEXT CELL] s[0] show error indexing set`**
  - On the other hand, sets are unordered, so they don't have a specific order, and therefore they can't be indexed

<br>

- **`[OPEN] Venn.png`**:
  - You can apply mathematical sets operations to the set structures
  - Some common set operations are union, intersection, difference, and symmetric difference

<br>

- **`[NEXT CELL] set1 = {"apple", "cherry"}`**:
  - To see how to use these methods in Python, let's define two examples set1 and set2, which contain fruit names
- **`[NEXT CELL] set1.union(set2)`**:
  - The union() method returns a new set with all items from both sets:
  - Notice that the repeated elements don't appear twice because we are dealing with sets

<br>

- **`[NEXT CELL] set1.intersection(set2)`**:
  - The intersection method returns a set that only contains the items that are present in both sets.

<br>

- **`[NEXT CELL] set1.difference(set2)`**:
  - The difference method returns a set that contains the items that only exist in set_1, and not in set_2

<br>

- **`[NEXT CELL] set1.symmetric_difference(set2)`**:

  - And finally, the symmetric_difference method returns a set that contains all items from both sets, except items that are present in both sets

- To finish off this video, let's see how to add and remove elements in a set
- **`[NEXT CELL] set1.add("fig")`**
  - We can add elements using the add method
  - Notice that the add method is an in-place operation, meaning that it will change the original content of the set

<br>

- **`[NEXT CELL] set1.add("apple")`**
  - If we try to add an already existing element, this will not affect the set

<br>

- **`[NEXT CELL] set1.remove("fig")`**
  - We can remove elements using the remove or the discard methods
  - They both remove a certain element from the set

<br>

- **`[ASK]`**
  - So, you might be wondering what's the difference between remove and discard
  - We can ask google!

<br>

- **`[OPEN BROWSER] Google "python difference between remove and discard sets"`** :
  - Here, we can see one of the web pages that you will find multiple times when looking for answers online: Stackoverflow

<br>

- **`[OPEN LINK] What is difference between Discard() and Remove() function ...`**
- **`[SCROLL DOWN TO THE FIRST ANSWER]` <font size=+1> Read the answer out loud </font>**
  - So, as we can see, the difference between them is that remove throws an error if the element is not present
  - let's be empirical and try it on our script

<br>

- **`[NEXT CELL] set1.remove("orange")`**
  - When running this cell, Python is complaining that 'orange' is not in the set

<br>

- **`[NEXT CELL] set1.discard("orange")`**
  - But when using discard, it doesn't throw any error

## Summary

- **`[SHOW] Webcam capture in full screen`**
- Let's review what we learnt today
- So, in this video, we covered lists and sets

- Lists are collections of items
- They are ordered and mutable
- You learnt how to create a list
- You learnt how to access elements in a list
- You learnt how to add elements to a list
- You learnt how to remove elements in a list

- Sets are collections of unique items
- They are ordered and mutable
- You learnt how to create a set from scratch and from a list
- You learnt how to perform mathematical set operations to a list in Python
- You learnt how to add elements to a set
- You learnt how to remove elements in a set
