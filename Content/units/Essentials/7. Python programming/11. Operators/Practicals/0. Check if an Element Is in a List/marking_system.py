def check_step_1(
    ans: str,
) -> None:
    assert isinstance(ans, str), \
        ("The data type of 'ans' is incorrect. "
         "It should be a string. Make sure you are using the form in this cell.")
    
    assert ans == "in", \
        ("Your answer is incorrect. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "The 'in' operator is used to check if an element is in a list. "
        "You can also use it for other data types such as strings and dictionaries."
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
    assert ans == "not in", \
        ("Your answer is incorrect. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "The 'not in' operator is used to check if an element is NOT in a list."
    )
