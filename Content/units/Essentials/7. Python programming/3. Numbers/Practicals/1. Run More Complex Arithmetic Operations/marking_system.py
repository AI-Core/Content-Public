def check_step_1(
    a: int,
    b: int,
) -> None:
    assert isinstance(a, int), "The value of 'a' is incorrect. It should be an integer."
    assert isinstance(b, int), "The value of 'b' is incorrect. It should be an integer."
    assert a == 10, "The value of 'a' is incorrect. It should be 10."
    assert b == 7, "The value of 'b' is incorrect. It should be 7."
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully assigned values to the variables 'a' and 'b'."
    )

def check_step_2(
    mod_value: int,
) -> None:
    assert isinstance(mod_value, int), \
        "The value of 'mod_value' is incorrect. It should be an integer."
    assert mod_value == 3, \
        "The value of 'mod_value' is incorrect. Please, try again."
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully assigned the value of the remainder of 'a' divided by 'b' to the variable 'mod_value'."
    )
    

def check_step_3(
    floor_value: int,
) -> None:
    assert isinstance(floor_value, int), \
        "The value of 'floor_value' is incorrect. It should be an integer."
    assert floor_value == 1, \
        "The value of 'floor_value' is incorrect. Please, try again."
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully assigned the value of the floor division of "
        "'a' divided by 'b' to the variable 'floor_value'."
    )

def check_step_4(
    exp_value: int,
) -> None:
    assert isinstance(exp_value, int), \
        "The value of 'exp_value' is incorrect. It should be an integer."
    assert exp_value == 10000000, \
        "The value of 'exp_value' is incorrect. Please, try again."
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully assigned the value of the exponentiation of "
        "'a' to the power of 'b' to the variable 'exp_value'."
    )
