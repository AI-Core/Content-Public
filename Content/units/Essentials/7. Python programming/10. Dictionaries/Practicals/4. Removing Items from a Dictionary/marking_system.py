def check_step_1(
    my_dict: dict,
    ans: str,
) -> None:
    assert isinstance(my_dict, dict), \
        ("The data type of 'my_dict' is incorrect. "
         "It should be a dictionary. Please, try again.")
    assert my_dict == {"key_2": 2, "key_3": 3}, \
        ("The value of 'my_dict' is incorrect. "
         "It should be a dictionary with the values: "
         "{'key_2': 2, 'key_3': 3}. Please, try again.")
    assert ans == "del my_dict['key_1']", \
        ("Your answer is incorrect. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully removed the key 'key_1' from the dictionary using the del keyword. "
        "You can also use the del keyword to delete variables."
    )

def check_step_2(
    my_dict: dict,
    my_value: int,
) -> None:
    '''
    Checks that the answer is correct
    '''
    assert isinstance(my_dict, dict), \
        ("The data type of 'my_dict' is incorrect. "
         "It should be a dictionary. Please, try again.")
    assert my_dict == {"key_3": 3}, \
        ("The value of 'my_dict' is incorrect. "
         "It should be a dictionary with the values: "
         "{'key_3': 3}. Please, try again.")
    assert isinstance(my_value, int), \
        ("The data type of 'my_value' is incorrect. "
         "It should be an integer. Please, try again.")
    assert my_value == 2, \
        ("The value of 'my_value' is incorrect. "
         "It should be the value of the key 'key_2' in the dictionary. Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully removed the key 'key_2' from the dictionary "
        "and assigned its value to the variable 'my_value' using the pop method."
    )
