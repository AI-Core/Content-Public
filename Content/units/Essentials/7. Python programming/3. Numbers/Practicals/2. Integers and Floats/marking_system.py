def check_step_1(
    a: int,
    b: int,
) -> None:
    assert isinstance(a, int), "The value of 'a' is incorrect. It should be an integer."
    assert isinstance(b, int), "The value of 'b' is incorrect. It should be an integer."
    assert a == 5, "The value of 'a' is incorrect. It should be 5."
    assert b == 2, "The value of 'b' is incorrect. It should be 2."
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully assigned values to the variables 'a' and 'b'."
    )

def check_step_2(
    a_type: str,
    b_type: str,
) -> None:
    assert isinstance(a_type, str), "The value of 'a_type' is incorrect. It should be a string."
    assert isinstance(b_type, str), "The value of 'b_type' is incorrect. It should be a string."
    assert a_type == "int", "The value of 'a_type' is incorrect. Please, try again."
    assert b_type == "int", "The value of 'b_type' is incorrect. Please, try again."
    print(
        "\033[92m\N{heavy check mark} Well done! Your answer is correct."
    )

def check_step_3(
    c: float,
) -> None:
    assert isinstance(c, float), "The value of 'c' is incorrect. It should be a float."
    assert c == 5 / 2, "The value of 'c' is incorrect. Please, try again."
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully assigned the value of the division of 'a' by 'b' to the variable 'c'."
    )

def check_step_4(
    c_type: str,
) -> None:
    assert isinstance(c_type, str), "The value of 'c_type' is incorrect. It should be a string."
    assert c_type == "float", "The value of 'c_type' is incorrect. Please, try again."
    print(
        "\033[92m\N{heavy check mark} Well done! Your answer is correct."
    )

def check_step_5(
    d: int
) -> None:
    assert isinstance(d, int), "The value of 'd' is incorrect. It should be an integer."
    assert d == 2, "The value of 'd' is incorrect. Please, try again."
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully assigned the value of the floor division of 'a' by 'b' to the variable 'd'."
        "By default, Python returns a float when performing a division operation, "
        "but it returns an integer when performing a floor division operation."
    )

def check_step_6(
    d_type: str,
) -> None:
    assert isinstance(d_type, str), \
        ("The value of 'd_type' is incorrect. It should be a string. "
         "Please, make sure you are using the form in this cell")
    assert d_type == "int", \
        ("The value of 'd_type' is incorrect. Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! A floor division operation returns an integer."
    )

