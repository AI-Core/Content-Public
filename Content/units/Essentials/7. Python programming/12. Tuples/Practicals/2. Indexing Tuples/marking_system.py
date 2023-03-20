def check_step_1(
    first_e: int,
) -> None:
    assert isinstance(first_e, int), \
        ("The data type of 'first_e' is incorrect. "
         "It should be an integer. Make sure you are using the correct method.")
    assert first_e == 1, \
        ("The value of 'first_e' is incorrect. "
         "You need to find the right index using the 'index()' method.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "The 'index()' method is used to find the index of an element in a tuple. "
        "Remember that the index of the first element in a tuple is 0."
    )

def check_step_2(
    first_i: int,
    ans: str,
) -> None:
    assert isinstance(first_i, int), \
        ("The data type of 'first_i' is incorrect. "
         "It should be an integer. Make sure you are using the correct method.")
    assert isinstance(ans, str), \
        ("The data type of 'ans' is incorrect. "
         "It should be a string. Make sure you are using the form in this cell.")
    assert ans == "1", \
        ("Your answer is incorrect. "
         "Even though there might be more than 'i' in the tuple, "
         "the 'index()' method will return the index of the first 'i' in the tuple.")
    assert first_i == 2, \
        ("The value of 'first_i' is incorrect. "
         "You need to find the right index using the 'index()' method.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "Notice that the index method just returns the index of the first 'i' in the tuple, "
        "even though there might be more than one 'i' in the tuple."
    )

def check_step_3(
    ans: str,
) -> None:
    assert isinstance(ans, str), \
        ("The data type of 'ans' is incorrect. "
         "It should be a string. Make sure you are using the form in this cell.")
    assert ans == "ValueError: tuple.index(x): x not in tuple", \
        ("Your answer is incorrect. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "The 'index()' method will return a ValueError if the element is not in the tuple."
    )

def check_step_4(
    ans: str,
) -> None:
    assert isinstance(ans, str), \
        ("The data type of 'ans' is incorrect. "
         "It should be a string. Make sure you are using the form in this cell.")
    assert ans == "13", \
        ("Your answer is incorrect. "
         "Make sure that you are specifying the index to start searching from.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You can specify the index to start searching from, so in this case "
        "the 'index()' method will return the index of the first 'i' after index 4."
    )