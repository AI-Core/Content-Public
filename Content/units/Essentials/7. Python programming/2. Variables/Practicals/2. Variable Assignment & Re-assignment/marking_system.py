def check_step_1(
    num_1: str,
    num_2: str,
) -> None:
    assert num_1 == 37, "The value of 'num_1' is incorrect. It should be 37."
    assert num_2 == 52, "The value of 'num_2' is incorrect. It should be 52."
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully assigned values to the variables 'num_1' and 'num_2'."
    )

def check_step_2(
    sum_value: int,
    prod_value: int,
) -> None:
    assert sum_value == 89, "The value of 'sum_value' is incorrect"
    assert prod_value == 1924, "The value of 'prod_value' is incorrect"
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully obtained the sum and product of 'num_1' and 'num_2'."
    )

def check_step_3(
    num_1: int,
    num_2: int
) -> None:
    assert num_1 == 8, "The value of 'num_1' is incorrect. It should be 8."
    assert num_2 == 3, "The value of 'num_2' is incorrect. It should be 3."
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully reassigned values to the variables 'num_1' and 'num_2'."
    )

def check_step_4(
    sum_value: int,
    prod_value: int,
) -> None:
    assert sum_value == 11, "The value of 'sum_value' is incorrect"
    assert prod_value == 24, "The value of 'prod_value' is incorrect"
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully obtained the new values for the sum and product "
        "of 'num_1' and 'num_2'."
    )
