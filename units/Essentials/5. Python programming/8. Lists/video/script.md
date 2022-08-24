# List and Sets

_Webcam capture in full screen_

## Lists

- Lists are used to store multiple items in a single variable.
- Lists are represented with square brackets, and each element is separated from each other using a comma
- **`[NEXT CELL] my_list = ["apple", 2, 3.14]`** :

  - For example, this is a list that contains three elements: a string, an integer, and a floating-point number
  - This means that the elements inside the List don't necessarily have the same type

- **`[NEXT CELL] my_list[0]`**
  - The items inside the List are indexed, and the first item corresponds to index 0
  - Thus, index 1 is number two, and index 2 corresponds to 3.14
- **`[NEXT CELL] my_list[-1]`**
  - We can use negative indices, where index -1 corresponds to the last element.
  - So [-1] will return 3.14
- **`[NEXT CELL] my_list[8]`**
  - If you try to index something out of range, it will throw an error

<br>

- **`[NEXT CELL] longer_list = ["a", "b", "c"...**`:
  - Lists allow slicing, which is the operation of getting a range of items

<br>

- **`[NEXT CELL] longer_list[ 5:8 ]`**:
  - One case where newlines and indentation are not treated is between square brackets
  - this is because it often makes the indexing easier to read

<br>

- **`[NEXT CELL] longer_list[0:3]**`:

  - For example, in this List, we can get the first three elements writing longer_list[0:3]
  - Notice that 3 is not inclusive

<br>

- **`[NEXT CELL] longer_list[-1000:1000]`**:
  - you might expect Python to throw an error if the slice indices are out of range
  - but, if your slice indices are out of range, Python will go as far as it can

<br>

- **`[NEXT CELL] longer_list[6:]`**:
  - If we don't specify upper or lower bound, it will assume the lower bound will be 0, and -1 respectively
  - And longer_list[6:] returns 10, 11, 42

<br>

- **`[NEXT CELL] longer_list[:4]`**:
  - Thus longer_list[:4] returns 'a', 'b', and 'c'

<br>

- **`[NEXT CELL] longer_list[3:8:2]`**:
  - You can add a third number to the range separated by another colon
  - This third number corresponds to the step size of the range
  - For example longer_list[3:8:2] returns [1, 3, 11]

<br>

- Lists have two main characteristics, they are mutable and ordered
- Ordered means that the items have a defined order, and this order will not change
  - So, if you add an item to the List, the rest of the items won't change their order

<br>

- Mutable means that items in the List are changeable, so we can replace, add, and remove items in the List
- **`[NEXT CELL] longer_list[0] = "hello"`** :
  - For example, you can say longer_list[0] = "hello", and the new List will replace "a" for "hello" without any issue

## List methods

- We know how to define a list and access certain data in it.
- What else can we do with a list?
- Let's take a look at the most common functions and methods

<br>

- **`[NEXT CELL] len(longer_list)`** :

  - One of the most common things you will do is get the number of items on a list. You can do that using the `len` function
  - So, `len(my_list)` in this List returns 9

<br>

- remember, methods are a function that can be called on some python variable
- lists have lots of practical methods, and you'll mostly learn them as you need them - but for now, I'll show you some of the most common and useful

<br>

- **`[NEXT CELL] longer_list.append("new final item")`** :
  - You can add data to your List using append
  - For example, you can add a new string

<br>

- **`[NEXT CELL] longer_list.append([1, 2, 3])`** :
  - Another way to add elements to a list is using the extend method
  - The difference between append and extend is that append will add the new item as a single element, whereas extend will add them item-wise.
  - Thus, both methods return something similar, but as we can see in this example, `append` adds the elements as a whole.

<br>

- **`[ASK]`** :
  - We know how to add items, but how do we remove them?
  - As with many other problems in programming, you can find the answer quickly by googling the correct terms
  - Let's look for an answer on Google:

<br>

- **`[OPEN BROWSER] Google "python remove items from list"`** :
  - A good option for basic queries is going to w3schools

<br>

- **`[OPEN LINK] Python - Remove List Items - W3Schools`**
  - As we can see, we can remove specific items using the remove method
  - Another way to remove an element is using the pop method, which will remove an element in a specific index.
  - If we don't specify the index, it will remove the last item
  - The delete keyword from Python can achieve the same result if we know the index of the element we want to remove
  - Finally, the `clear` method simply empties the List in case you want to start over

<br>

- Finally, we can sort the list using the sort method
- **`[NEXT CELL] my_list = ['p', 'y', 't', 'h', 'o', 'n']`**:
  - To do so, we can use the sort method my_list.sort()

<br>

- **`[NEXT CELL] my_list.reverse()`**

  - We can also sort it in a reverse order using the reverse method

- notice that these two perform what we call an "in-place" operation

  - that is, they overwrite the existing value of that variable with a sorted or reversed list
  - other methods are not in place, and instead, they return us a new value which something can be assigned to

- **`[NEXT CELL] sorted(my_list)`**
  - e.g. the built-in method sorted does the same thing as doing .sort on a list, but instead of changing the List in place, it returns you a variable

<br>

- **`[NEXT CELL] sorted_list = sorted(my_list)`**
  - to use that variable, we need to assign something equal to the returned value

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
