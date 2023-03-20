def check_step_1(
    my_dict: dict,
) -> None:
    assert isinstance(my_dict, dict), \
        ("The data type of 'my_dict' is incorrect. "
         "It should be a dictionary. Please, try again.")
    assert my_dict == {"key_1": 1, "key_2": 2}, \
        ("The value of 'my_dict' is incorrect. "
         "It should be a dictionary with the key 'key_1' and the value 1, "
         "and the key 'key_2' and the value 2. Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully created the dictionary. "
    )


def check_step_2(
    my_dict: dict,
    key_1: int,
    key_2: int,
    ans_1: str,
    ans_2: str,
) -> None:
    '''
    Checks that the answer is correct
    '''
    assert isinstance(my_dict, dict), \
        ("The data type of 'my_dict' is incorrect. "
         "It should be a dictionary. Please, try again.")
    assert isinstance(key_1, int), \
        ("The data type of 'key_1' is incorrect. "
         "It should be an integer. Make sure you are accesing the value of the key 'key_1'. Please, try again.")
    assert isinstance(key_2, int), \
        ("The data type of 'key_2' is incorrect. "
         "It should be an integer. Make sure you are accesing the value of the key 'key_2'. Please, try again.")
    assert isinstance(ans_1, str), \
        ("The data type of 'ans_1' is incorrect. "
         "Please, make sure you are using the form in this cell")
    assert isinstance(ans_2, str), \
        ("The data type of 'ans_2' is incorrect. "
         "Please, make sure you are using the form in this cell")
    assert my_dict == {"key_1": 1, "key_2": 2}, \
        ("The value of 'my_dict' is incorrect. "
         "It should be a dictionary with the key 'key_1' and the value 1, "
         "and the key 'key_2' and the value 2. Please, try again.")
    assert key_1 == 1, \
        ("The value of 'key_1' is incorrect. "
         "It should be 1. Make sure you are accesing the value of the key 'key_1'. Please, try again.")
    assert key_2 == 2, \
        ("The value of 'key_2' is incorrect. "
         "It should be 2. Make sure you are accesing the value of the key 'key_2'. Please, try again.")
    assert ans_1 == "my_dict['key_1']", \
        ("Your first answer is incorrect. "
         "Please, try again.")
    assert ans_2 == "my_dict['key_2']", \
        ("Your second answer is incorrect. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully accessed the values of the dictionary. "
    )

def check_step_3(
    my_dict: dict,
    ans: str
) -> None:
    assert isinstance(my_dict, dict), \
        ("The data type of 'my_dict' is incorrect. "
         "It should be a dictionary. Please, try again.")
    assert isinstance(ans, str), \
        ("The data type of 'ans' is incorrect. "
         "It should be a string. Please, make sure you are using the form in this cell")
    assert my_dict == {"key_1": 1, "key_2": 2}, \
        ("The value of 'my_dict' is incorrect. "
         "It should be a dictionary with the key 'key_1' and the value 1, "
         "and the key 'key_2' and the value 2. Please, try again.")
    assert ans == "KeyError", \
        ("Your answer is incorrect. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "A KeyError is raised when you try to access a key that is not in the dictionary."
    )

def check_step_4(
    my_dict: dict,
    my_keys,
) -> None:
    assert isinstance(my_dict, dict), \
        ("The data type of 'my_dict' is incorrect. "
         "It should be a dictionary. Please, try again.")
    assert my_dict == {"key_1": 1, "key_2": 2}, \
        ("The value of 'my_dict' is incorrect. "
         "It should be a dictionary with the key 'key_1' and the value 1, "
         "and the key 'key_2' and the value 2. Please, try again.")
    expected_keys = my_dict.keys()
    expected_type = type(expected_keys)
    assert isinstance(my_keys, expected_type), \
        ("The data type of 'my_keys' is incorrect. "
         "It should be a dict_keys object. Please, create it using the method .keys() on the dictionary.")
    assert my_keys == expected_keys, \
        ("The value of 'my_keys' is incorrect. "
         "It should be a dict_keys object with the keys 'key_1' and 'key_2'. "
         "Please, create it using the method .keys() on the dictionary.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully created a dict_keys object. "
        "This object contains the keys of the dictionary. "
    )

def check_step_5(
    my_dict: dict,
    my_values,
) -> None:
    assert isinstance(my_dict, dict), \
        ("The data type of 'my_dict' is incorrect. "
         "It should be a dictionary. Please, try again.")
    assert my_dict == {"key_1": 1, "key_2": 2}, \
        ("The value of 'my_dict' is incorrect. "
         "It should be a dictionary with the key 'key_1' and the value 1, "
         "and the key 'key_2' and the value 2. Please, try again.")
    expected_values = my_dict.values()
    expected_type = type(expected_values)
    assert isinstance(my_values, expected_type), \
        ("The data type of 'my_values' is incorrect. "
         "It should be a dict_values object. Please, create it using the method .values() on the dictionary.")
    expected_values = list(expected_values)
    my_values = list(my_values)
    assert my_values == expected_values, \
        ("The value of 'my_values' is incorrect. "
         "It should be a dict_values object with the values 1 and 2. "
         "Please, create it using the method .values() on the dictionary.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully created a dict_values object. "
        "This object contains the values of the dictionary. "
    )

def check_step_6(
    my_dict: dict,
    my_items: dict,
    ans: str
) -> None:
    assert isinstance(my_dict, dict), \
        ("The data type of 'my_dict' is incorrect. "
         "It should be a dictionary. Please, try again.")
    assert my_dict == {"key_1": 1, "key_2": 2}, \
        ("The value of 'my_dict' is incorrect. "
         "It should be a dictionary with the key 'key_1' and the value 1, "
         "and the key 'key_2' and the value 2. Please, try again.")
    expected_items = my_dict.items()
    expected_type = type(expected_items)
    assert isinstance(my_items, expected_type), \
        ("The data type of 'my_items' is incorrect. "
         "It should be a dict_items object. Please, create it using the method .items() on the dictionary.")
    assert my_items == expected_items, \
        ("The value of 'my_items' is incorrect. "
         "It should be a dict_items object with the items ('key_1', 1) and ('key_2', 2). "
         "Please, create it using the method .items() on the dictionary.")
    assert isinstance(ans, str), \
        ("The data type of 'ans' is incorrect. "
         "It should be a string. Please, make sure you are using the form in this cell")
    assert ans == "tuple", \
        ("Your answer is incorrect. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully created a dict_items object. "
        "Each item in this object is like a tuple where the first element "
        "is the key and the second element is the value. "
    )
