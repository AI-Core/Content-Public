def check_step_1(
    num_1: int,
    num_2: int,
) -> None:
    assert isinstance(num_1, int), \
        ("The value of 'num_1' is incorrect. It should be an integer."
         "Please, make sure you are using the form in this cell")
    assert isinstance(num_2, int), \
        ("The value of 'num_2' is incorrect. It should be an integer."
         "Please, make sure you are using the form in this cell")
    if num_1 < num_2:
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "num_1 is lower than num_2, so the condition is False."
        )
    elif num_1 == num_2:
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "num_1 is equal to num_2, so the condition is False."
        )
    else:
        raise ValueError(
            "The condition is not correct because num_1 is higher than num_2. "
            "Please, enter two numbers such that num_1 is lower or equal to num_2."
        )

def check_step_2(
    ans_1: str,
    ans_2: str,
    ans_3: str,
) -> None:
    assert isinstance(ans_1, str), \
        ("The value of 'ans_1' is incorrect. It should be a string."
         "Please, make sure you are using the form in this cell")
    assert isinstance(ans_2, str), \
        ("The value of 'ans_2' is incorrect. It should be a string."
         "Please, make sure you are using the form in this cell")
    assert isinstance(ans_3, str), \
        ("The value of 'ans_3' is incorrect. It should be a string."
         "Please, make sure you are using the form in this cell")
    assert (ans_1 == "True") and (ans_2 == "False") and (ans_3 == "False"), \
        ("The values of 'ans_1', 'ans_2' and 'ans_3' are incorrect. "
         "In Python, the absence of a value is considered as False. "
         "So, for example and empty string or a '0' are considered as False. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "In Python, the absence of a value is considered as False. "
        "So, for example and empty string or a '0' are considered as False, "
        "whereas a non-empty string or a non-zero number are considered as True."
    )

def check_step_3(
    ans_1: str,
) -> None:
    assert isinstance(ans_1, str), \
        ("The value of 'ans_1' is incorrect. It should be a string."
         "Please, make sure you are using the form in this cell")
    assert ans_1 == "bool", \
        ("The value of 'ans_1' is incorrect. "
         "Please, try again.")
    print("\033[92m\N{heavy check mark} Well done! "
          "The type of a boolean is 'bool'.")

def check_step_4(
    ans_1: str,
) -> None:
    assert isinstance(ans_1, str), \
        ("The value of 'ans_1' is incorrect. It should be a string."
         "Please, make sure you are using the form in this cell")
    assert ans_1 == "False", \
        ("The value of 'ans_1' is incorrect. "
         "Please, try again.")
    print("\033[92m\N{heavy check mark} Well done! "
          "An empty string is considered as False.")
