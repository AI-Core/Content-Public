- There are many different types of operators that return boolean values:
  - Comparison Operators
  - Logical Operators
  - Identity Operators
  - Membership Operators

### Comparison

- Comparison operators compare two values
- **`[FIRST CELL] x = 6`**
  - `==` compares if two values are equal
  - `!=` compares if two values are different
  - `>` compares if the first value is greater than the second
  - `<` compares if the first value is lower than the second
  - `>` compares if the first value is greater or equal than the second
  - `<` compares if the first value is lower or equal than the second

### Logical

- Logical Operators are used to combining conditional statements

<br>

- **`[NEXT CELL] Three print statements with comparisons`**
  - `and` Returns True if both statements are true

<br>

- **`[NEXT CELL] print(x > z or y == x)`**
  - `or` returns True if ONE of the statements is true

<br>

- **`[NEXT CELL] not(x > y)`**
  - `not` reverses the result.

### Identity

- Identity Operators are used to comparing objects, not if they are equal.
- To understand this, you have to know that each variable has a space in memory

<br>

- **`[NEXT CELL] x = 1`**

  - Usually, the same integers share the same space in memory. For example, there is a space in memory reserved for number 1
  - Identity operators will see if two variables point to the same space in memory
    - `is` returns true if both variables point to the same space
    - `is not` returns true if both variables DON'T point to the same space
  - Thus, the following operator returns True because they are pointing to the space reserved for number 1

<br>

- **`[NEXT CELL] list_1 = [1, 2, 3]`**

  - However, it works differently for lists. Python allocates a unique space in memory for each list, even if they share the same content
  - This means that when assigning a list to a variable, Python allocates that variable to a new space in memory
  - However, if we assign an existing list to a variable, we are telling Python to make the new variable to the same space in memory
  - Thus, this statement returns False:

<br>

- **`[NEXT CELL] list_3 = ['a', 'b', 'c']`**
  - In this case, we are telling list_4 to point to the same memory space as list_3
  - Thus, this statement `is` returns True

### Membership

- Membership operators are used to check if an item is present in a container, such as a list, set, tuple, or dictionary keys

<br>

- **`[NEXT CELL] 1 in my_list`**
  - `in` returns true if the item is in the container

<br>

- **`[NEXT CELL] 1 not in my_list`**

  - `not in` returns true if the item is not in the container

- With this in mind, you will be able to run specific parts of your code or use loops based on defined conditions. But for now, let's wrap up this lesson

## Summary (TODO replace with key takeaways)

- We created dictionaries
- We learnt how to add, read, and remove elements in a dictionary
- We introduced tuples, which as opposed to lists, are immutable
- This immutability prevents us from modifying the content of the tuple
- We saw that you can unpack iterables into individual variables
- Then we saw boolean type and the operations that return boolean values
- and We learnt how to use comparison , Logical ,Identity, Membership operators
- So make sure you can explain the difference in each of those data types and know when to use each of them
