def check_step_1(
    my_dict: dict,
    ans: str
) -> None:

    assert isinstance(my_dict, dict), \
        ("The data type of 'my_dict' is incorrect. "
         "It should be a dictionary. Please, try again.")
    assert isinstance(ans, str), \
        ("The data type of 'ans' is incorrect. "
         "It should be a string. Please, try again.")
    assert len(my_dict) == 0, \
        ("The value of 'my_dict' is incorrect. "
         "It should be an empty dictionary. Please, try again.")
    assert ans == "dict", \
        ("Your answer is incorrect. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "When you create a variable with {}, it will correspond to a dictionary."
    )


def check_step_2(
    my_var: set,
    ans: str
) -> None:
    '''
    Checks that the answer is correct
    '''
    assert isinstance(my_var, set), \
        ("The data type of 'my_var' is incorrect. "
         "It should be a set. Please, try again.")
    assert isinstance(ans, str), \
        ("The data type of 'ans' is incorrect. "
         "It should be a string. Please, try again.")
    assert my_var == {4}, \
        ("The value of 'my_var' is incorrect. "
         "It should be a set with the value 4. Please, try again.")
    assert ans == "set", \
        ("Your answer is incorrect. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "If you add values to curly brackets, if there are no colons, it will correspond to a set."
    )

def check_step_3(
    my_var_2: dict,
    ans: str
) -> None:
    assert isinstance(my_var_2, dict), \
        ("The data type of 'my_var_2' is incorrect. "
         "It should be a dictionary. Please, try again.")
    assert isinstance(ans, str), \
        ("The data type of 'ans' is incorrect. "
         "It should be a string. Please, try again.")
    assert my_var_2 == {4: 5}, \
        ("The value of 'my_var_2' is incorrect. "
         "It should be a dictionary with the key 4 and the value 5. Please, try again.")
    assert ans == "dict", \
        ("Your answer is incorrect. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "If you add values to curly brackets, if there are colons, it will correspond to a dictionary. "
        "The key is the value before the colon and the value is the value after the colon. "
        "You can add as many key-value pairs as you want by separating them with commas."
    )
