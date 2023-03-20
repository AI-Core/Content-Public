def check_step_1(
    ans: str,
) -> None:
    assert isinstance(ans, str), \
        ("The data type of 'ans' is incorrect. "
         "It should be a string. Make sure you are using the form in this cell.")

    assert ans == "==", \
        ("Your answer is incorrect. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "The '==' operator is used to check if two numbers or two strings are equal."
        "This is not the same as being the same object as you will see in the next step."
    )


def check_step_2(
    ans: str,
) -> None:
    '''
    Checks that the answer is correct
    '''
    assert isinstance(ans, str), \
        ("The data type of 'ans' is incorrect. "
         "It should be a string. Make sure you are using the form in this cell.")
    assert ans == "is", \
        ("Your answer is incorrect. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "The 'is' operator is used to check if two objects are the same object. "
        "Python creates a new object for each number or string you create. "
        "But when creating a number or string, if you create a variable with the same value, "
        "Python will point the new variable to the same object as the first variable."
    )

def check_step_3(
    ans: str,
) -> None:
    '''
    Checks that the answer is correct
    '''
    assert isinstance(ans, str), \
        ("The data type of 'ans' is incorrect. "
         "It should be a string. Make sure you are using the form in this cell.")
    assert ans == "Because both variables are pointing to the same object (1)", \
        ("Your answer is incorrect. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "The 'is' operator is used to check if two objects are the same object. "
        "For numbers and strings, Python creates a new object for each number or string you create. "
        "In this case, my_number_1 was created with the value 1, so Python created a new object for it. "
        "When my_number_2 was created, Python saw that it had the same value as my_number_1, "
        "so it pointed my_number_2 to the same object as my_number_1."
    )

def check_step_4(
    ans: str,
) -> None:
    '''
    Checks that the answer is correct
    '''
    assert isinstance(ans, str), \
        ("The data type of 'ans' is incorrect. "
         "It should be a string. Make sure you are using the form in this cell.")
    assert ans == "==", \
        ("Your answer is incorrect. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "To simply compare values, you can use the '==' operator. "
    )

def check_step_5(
    ans: str,
) -> None:
    '''
    Checks that the answer is correct
    '''
    assert isinstance(ans, str), \
        ("The data type of 'ans' is incorrect. "
         "It should be a string. Make sure you are using the form in this cell.")
    assert ans == "Because Python creates two different objects for the two lists", \
        ("Your answer is incorrect. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "As opposed to numbers and strings, Python does not create a new object for each list you create. "
        "So, even if they have the same values, Python created two different objects for the two lists."
    )
