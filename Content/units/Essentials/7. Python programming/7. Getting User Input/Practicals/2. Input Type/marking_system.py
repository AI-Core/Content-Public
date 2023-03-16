def check_step_1(
    name: str,
    ans_1: str,
) -> None:
    assert isinstance(name, str), \
        "The value of 'name' is incorrect. It should be a string."
    assert isinstance(ans_1, str), \
        ("The value of your answer is incorrect. It should be a string. "
         "Please, make sure you are using the form in this cell")
    assert ans_1 == "str", \
        ("The value of your answer is incorrect. "
         "Unless you are not using the input() function, "
         "the type of the variable 'name' should be 'str'. ")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have correctly obtained the user's name and stored it in the variable 'name'. "
    )

def check_step_2(
    age: str,
    ans_1: str,
) -> None:
    assert isinstance(age, str), \
        "The value of 'age' is incorrect. It should be a string obtained from the input() function."
    assert isinstance(ans_1, str), \
        ("The value of your answer is incorrect. It should be a string. "
         "Please, make sure you are using the form in this cell")
    assert ans_1 == "str", \
        ("The value of your answer is incorrect. "
         "Unless you are not using the input() function, "
         "the type of the variable 'age' should be 'str'. ")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have correctly obtained the user's age and stored it in the variable 'age'. "
    )

def check_step_3(
    age_as_int: int,
    ans_1: str,
) -> None:
    assert isinstance(age_as_int, int), \
        "The value of 'age_as_int' is incorrect. It should be an integer obtained from the input() function."
    assert isinstance(ans_1, str), \
        ("The value of your answer is incorrect. It should be a string. "
         "Please, make sure you are using the form in this cell")
    assert ans_1 == "int", \
        ("The value of your answer is incorrect. "
         "Unless you are not using the input() function, "
         "the type of the variable 'age_as_int' should be 'int'. ")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have correctly casted the user's age to an integer and stored it in the variable 'age_as_int'."
    )
