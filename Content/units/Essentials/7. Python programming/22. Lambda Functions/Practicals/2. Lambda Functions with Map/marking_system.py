from typing import Callable

def check_step_1(
    square: Callable[[int], int],
    numbers_old: list,
    numbers_new: list
) -> None:
    
    square_test = lambda x : x ** 2
    numbers_test = list(map(square_test, numbers_old))


    assert isinstance(square, type(lambda x:x)), "The function 'square' should be a lambda function"
    assert square(-2)==4, "The function 'square' should square any number it is given"
    assert type(numbers_new)!=map, "You need to cast the map object to a list"
    assert numbers_new == numbers_test, "The function 'square' needs to square each individual number in the list"

    print("\033[92m\N{heavy check mark} Well done!")
    
def check_step_2(
    cube: Callable[[int], int],
    numbers_old: list,
    numbers_new: list
) -> None:
    
    cube_test = lambda x : x ** 3
    numbers_test = list(map(cube_test, numbers_old))


    assert isinstance(cube, type(lambda x:x)), "The function 'cube' should be a lambda function"
    assert cube(-2)==-8, "The function 'cube' should cube any number it is given"
    assert type(numbers_new)!=map, "You need to cast the map object to a list"
    assert numbers_new == numbers_test, "The function 'cube' needs to cube each individual number in the list"

    print("\033[92m\N{heavy check mark} Well done!")

def check_step_3(
    func: Callable[[int], int],
    numbers_old: list,
    numbers_new: list
) -> None:
    
    func_test = lambda x : x ** 2 if x % 2 == 0 else x ** 3
    numbers_test = list(map(func_test, numbers_old))


    assert isinstance(func, type(lambda x:x)), "The function 'func' should be a lambda function"
    assert func(-2)==4, "The function 'func' should square any even number it is given"
    assert func(-3)==-27, "The function 'func' should cube any odd number it is given"
    assert type(numbers_new)!=map, "You need to cast the map object to a list"
    assert numbers_new == numbers_test, "The function 'func' needs to square each even number and cube each odd number in the list"

    print("\033[92m\N{heavy check mark} Well done!")