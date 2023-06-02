def check_step_1(
    my_variable: int,
) -> None:
    assert isinstance(my_variable, int), "The variable 'age' should be an integer."
    assert my_variable == 23, "The variable 'age' should be equal to 23."
    print("\033[92m\N{heavy check mark} Well done!")

def check_step_2(
    your_code: str,
) -> None:
    assert "print" in your_code, "Your code should contain a print statement."
    assert "my_variable" in your_code, "Your print statement should contain the variable 'my_variable'"
    print("\033[92m\N{heavy check mark} Well done!")

def check_step_3(
    my_variable: int,
) -> None:
    assert isinstance(my_variable, int), "The variable 'age' should be an integer."
    assert my_variable == 98, "The variable 'age' should be equal to 98."
    print("\033[92m\N{heavy check mark} Well done!")

def check_step_4(
    your_code: str,
) -> None:
    assert "print" in your_code, "Your code should contain a print statement."
    assert "my_variable" in your_code, "Your print statement should contain the variable 'my_variable'"
    print("\033[92m\N{heavy check mark} Well done!")