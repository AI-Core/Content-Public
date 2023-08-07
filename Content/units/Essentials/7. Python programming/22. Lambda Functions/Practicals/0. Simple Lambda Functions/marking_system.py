from typing import Callable

def check_step_1(
    square: Callable[[int], int]
) -> None:
    assert isinstance(square, type(lambda x:x)), "The function should utilise a lambda function"
    valid = True
    for num in range(-2,5):
        if not square(num) == num**2:
            raise ValueError(f"Failed to square {num}. Expected {num**2} but got {square(num)}")
            valid = False
    if valid:
        print("\033[92m\N{heavy check mark} Well done!")

def check_step_2(
    cube: Callable[[int], int]
) -> None:
    assert isinstance(cube, type(lambda x:x)), "The function should utilise a lambda function"
    valid = True
    for num in range(-2,5):
        if not cube(num) == num**3:
            raise ValueError(f"Failed to cube {num}. Expected {num**3} but got {cube(num)}")
            valid = False
    if valid:
        print("\033[92m\N{heavy check mark} Well done!")

def check_step_3(
    add: Callable[[int, int], int]
) -> None:
    assert isinstance(add, type(lambda x:x)), "The function should utilise a lambda function"
    assert add(-2, 2) == 0, f"Failed to add -2 and 2. Expected 0, got {add(-2, 2)}"
    print("\033[92m\N{heavy check mark} Well done!")

def check_step_4(
    multiply: Callable[[int, int], int]
) -> None:
    assert isinstance(multiply, type(lambda x:x)), "The function should utilise a lambda function"
    assert multiply(5, 2) == 10, f"Failed to multiply 5 and 2. Expected 10, got {multiply(5, 2)}"
    assert multiply(0, 1) == 0, f"Failed to multiply 0 and 1. Expected 0, got {multiply(0, 1)}"
    print("\033[92m\N{heavy check mark} Well done!")