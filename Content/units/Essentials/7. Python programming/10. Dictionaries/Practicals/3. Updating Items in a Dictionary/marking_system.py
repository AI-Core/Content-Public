def check_step_1(
    my_dict: dict,
) -> None:
    assert isinstance(my_dict, dict), \
        ("The data type of 'my_dict' is incorrect. "
         "It should be a dictionary. Please, try again.")
    assert my_dict == {"key_1": 3, "key_2": 2}, \
        ("The value of 'my_dict' is incorrect. "
         "It should be a dictionary with the values: "
         "{'key_1': 3, 'key_2': 2}. Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully changed the value of the key 'key_1' to 3 using indexing."
    )

def check_step_2(
    my_dict: dict,
) -> None:
    '''
    Checks that the answer is correct
    '''
    assert isinstance(my_dict, dict), \
        ("The data type of 'my_dict' is incorrect. "
         "It should be a dictionary. Please, try again.")
    assert my_dict == {"key_1": 3, "key_2": 4}, \
        ("The value of 'my_dict' is incorrect. "
         "It should be a dictionary with the values: "
         "{'key_1': 3, 'key_2': 4}. Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully changed the value of the key 'key_2' to 4 using the update() method. "
        "Notice that dictionaries allow you to add or update items using the same methods."
    )
