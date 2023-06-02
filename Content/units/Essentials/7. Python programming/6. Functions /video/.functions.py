# %%
# Basic Syntax of a function in Python
'''
def test_function(param_1, param_2):
    Code to be executed when we call for the function
    return output

'''




#%%

def say_hi():
    print('Hello')
    print('World')
    return 'Good Bye'




# %%
say_hi()






# %%
say_hi






# %%
def get_length(sentence):
    length = len(sentence)
    return length

sent_1 = 'Learning Python is increasingly demanded'
sent_2 = 'Python was released on 1991'

len_1 = get_length(sent_1)
len_2 = get_length(sent_2)

print(f'"{sent_1}" contains {len_1} characters')
print(f'"{sent_2}" contains {len_2} characters')





# %%
def get_short(sentence):
    length = len(sentence)
    if length <= 30:
        return length   # Once the return statement is reached, the code exits the function
    print('The sentence is too long')

len_2 = get_short(sent_2)




# %%
len_1 = get_short(sent_1)





# %%
print(len_1)




# %%
x = 'I am in the global scope'

def scope_test():
    print('Printing inside the function')
    print(x)

    y = 'I am in the local scope'

    print('Printing inside the function')
    print(y)

scope_test()
print()
print('Printing outside the function')
print(x)
print('Printing outside the function')
print(y)




# %%
x = 10

def test_function():
    x = 20
    print(f'Inside the function, and after assigning a new value, x is equal to {x}')

print(f'Before calling the function x is equal to {x}')
test_function()
print(f'After calling the function x is equal to {x}')







# %%
def test_args(*args):
    print(args)
    print(type(args))
test_args(1, 2, 3, 4, 5, 6, 7)





# %%
def get_mean(*args):
    total = sum(args)
    return total / len(args) # Divide the addition of all the numbers by the amount of numbers

print(get_mean(3, 6, 9, 12))







# %%
def test_kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))
test_kwargs(a=1, b=2, c=3)







# %%
def calculate_price(*args, **kwargs):
    fee = args[0]
    total = 0
    for item, price in kwargs.items():
        print(f'Adding {item} to the list')
        total += price
    
    return fee * total

cost = calculate_price(1.1, tomatoes=1.2, potatoes=0.75, chocolate=3.2)
print(round(cost, 2))
