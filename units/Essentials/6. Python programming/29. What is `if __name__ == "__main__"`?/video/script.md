# Motivation

- i'm going to explain why you should include this in almost all of your python files

- often, you're going to see this
- people respond in one of two ways
- either they panic because it looks complicated
- or they totally ignore it

# Intuitive explanation

- before I get into what each of these things is, let me explain it intuitively

- that's the key takeaway

# Under the hood

- now let's look a little deeper

`__name__` is the name of the current module

- that is, a reference to the name of the file that contains the code being run
- `__main__` is the name of the module which was run from the teminal

# **name** in main file

# Name in another file

Add `print('Another file __name__:', __name__)` to `another_file.py`
