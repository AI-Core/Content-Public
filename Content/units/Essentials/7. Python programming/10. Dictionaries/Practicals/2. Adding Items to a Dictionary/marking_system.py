def check_step_1(
    my_dict: dict,
) -> None:
    expected_dict = {"key_1": 1, "key_2": 2, "key_3": 3}
    assert isinstance(my_dict, dict), \
        ("The data type of 'my_dict' is incorrect. "
         "It should be a dictionary. Please, try again.")
    assert my_dict == expected_dict, \
        ("The value of 'my_dict' is incorrect. "
         "It should be a dictionary with the values: "
         "{'key_1': 1, 'key_2': 2, 'key_3': 3}. Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully added a new key-value pair to the dictionary."
    )


def check_step_2(
    my_dict: dict,
    ans: str,
) -> None:
    '''
    Checks that the answer is correct
    '''
    assert isinstance(my_dict, dict), \
        ("The data type of 'my_dict' is incorrect. "
         "It should be a dictionary. Please, try again.")
    assert isinstance(ans, str), \
        ("The data type of 'ans' is incorrect. "
         "It should be a string. Make sure you are using the form in this cell.")
    assert my_dict == {"key_1": 1, "key_2": 2, "key_3": 3, "key_4": 4}, \
        ("The value of 'my_dict' is incorrect. "
         "It should be a dictionary with the values: "
         "{'key_1': 1, 'key_2': 2, 'key_3': 3, 'key_4': 4}. Please, try again.")
    assert ans == "dictionary", \
        ("Your answer is incorrect. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully added a new key-value pair to the dictionary using the update() method."
    )
