from typing import Callable

def check_step_1(
    div: Callable[[int, int], float]
) -> None:
    
    try:
        assert div(10,3) == (10/3), "The function 'div' needs to divide the first number by the second"
    except TypeError:
        raise TypeError("The function should only attempt to divide the inputted numbers")

    print("\033[92m\N{heavy check mark} Well done!")

def check_step_2(
    error_handler: Callable[[int], int]
) -> None:
    
    try:
        @error_handler
        def div(a, b):
            return a / b
        assert div(10/3)==None, "'Error_handler' should return wrapper"
    except TypeError:
        raise TypeError("'Error_handler' function should process and execute a function and return its output and the wrapper")

    print("\033[92m\N{heavy check mark} Well done!")

def check_step_3(
    div_err: Callable[[int, int], float]
) -> None:
    
    try:
        print(f'Output for 10/3: {div_err(10,3)}')
        print(f'Output for 1/0: {div_err(10,3)}')
        print(f'Output for "1"/1: {div_err("1",1)}')
    except:
        raise TypeError("The 'error_hander' should not raise errors, only print custom error messages")

    print("\033[92m\N{heavy check mark} Well done!")