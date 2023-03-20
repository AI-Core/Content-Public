def check_step_1(
    my_dict_1: dict,
    my_dict_2: dict,
    my_dict_3: dict,
    my_list: list,
) -> None:
    assert isinstance(my_dict_1, dict), \
        ("The variable my_dict_1 should be a dictionary. "
         "Please, try again.")
    assert isinstance(my_dict_2, dict), \
        ("The variable my_dict_2 should be a dictionary. "
         "Please, try again.")
    assert isinstance(my_dict_3, dict), \
        ("The variable my_dict_3 should be a dictionary. "
         "Please, try again.")
    assert isinstance(my_list, list), \
        ("The variable my_list should be a list. "
         "Please, try again.")
    assert len(my_dict_1) == 3, \
        ("The dictionary my_dict_1 should have 3 key-value pairs. "
         "Please, try again.")
    assert len(my_dict_2) == 3, \
        ("The dictionary my_dict_2 should have 3 key-value pairs. "
         "Please, try again.")
    assert len(my_dict_3) == 3, \
        ("The dictionary my_dict_3 should have 3 key-value pairs. "
         "Please, try again.")
    assert len(my_list) == 3, \
        ("The list my_list should have 3 elements, each of which is a dictionary. "
         "Please, try again.")
    expected_keys = ['name', 'age', 'favourite_colour']
    for key in expected_keys:
        assert key in my_dict_1, \
            ("The dictionary my_dict_1 should have the key '{}'.".format(key))
        assert key in my_dict_2, \
            ("The dictionary my_dict_2 should have the key '{}'.".format(key))
        assert key in my_dict_3, \
            ("The dictionary my_dict_3 should have the key '{}'.".format(key))

    assert my_list == [my_dict_1, my_dict_2, my_dict_3], \
        ("The list my_list should have 3 elements, each of which is a dictionary. "
         "The first element should be my_dict_1, the second element should be my_dict_2, "
         "and the third element should be my_dict_3. "
         "Please, try again.")

    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully created three dictionaries and nested them in a list."
    )

def check_step_2(
    my_dict_1: dict,
    my_dict_2: dict,
    my_dict_3: dict,
    my_list: list,
    names_dict: dict,
) -> None:
    assert isinstance(my_dict_1, dict), \
        ("The variable my_dict_1 should be a dictionary. "
         "Please, try again.")
    assert isinstance(my_dict_2, dict), \
        ("The variable my_dict_2 should be a dictionary. "
         "Please, try again.")
    assert isinstance(my_dict_3, dict), \
        ("The variable my_dict_3 should be a dictionary. "
         "Please, try again.")
    assert isinstance(my_list, list), \
        ("The variable my_list should be a list. "
         "Please, try again.")
    assert len(my_dict_1) == 3, \
        ("The dictionary my_dict_1 should have 3 key-value pairs. "
         "Please, try again.")
    assert len(my_dict_2) == 3, \
        ("The dictionary my_dict_2 should have 3 key-value pairs. "
         "Please, try again.")
    assert len(my_dict_3) == 3, \
        ("The dictionary my_dict_3 should have 3 key-value pairs. "
         "Please, try again.")
    assert len(my_list) == 3, \
        ("The list my_list should have 3 elements, each of which is a dictionary. "
         "Please, try again.")
    expected_keys = ['name', 'age', 'favourite_colour']
    for key in expected_keys:
        assert key in my_dict_1, \
            ("The dictionary my_dict_1 should have the key '{}'.".format(key))
        assert key in my_dict_2, \
            ("The dictionary my_dict_2 should have the key '{}'.".format(key))
        assert key in my_dict_3, \
            ("The dictionary my_dict_3 should have the key '{}'.".format(key))

    assert my_list == [my_dict_1, my_dict_2, my_dict_3], \
        ("The list my_list should have 3 elements, each of which is a dictionary. "
         "The first element should be my_dict_1, the second element should be my_dict_2, "
         "and the third element should be my_dict_3. "
         "Please, try again.")

    assert isinstance(names_dict, dict), \
        ("The variable names_dict should be a dictionary. "
         "Please, try again.")

    expected_keys_names = []
    expected_values = []
    for user_dict in my_list:
        expected_keys_names.append(user_dict['name'])
        expected_values.append({
            'age': user_dict['age'],
            'favourite_colour': user_dict['favourite_colour']
        })

    assert len(names_dict) == 3, \
        ("The dictionary names_dict should have 3 key-value pairs. "
         "Each key should be a name, and each value should be a dictionary with two key-value pairs. "
         "Please, try again.")

    for key in expected_keys_names:
        assert key in names_dict, \
            (f"The dictionary names_dict should have the key '{key}'. "
             "Please, try again.")

    for expected_value in expected_values:
        assert expected_value in names_dict.values(), \
            (f"The dictionary names_dict should have the value '{expected_value}'. "
             "Please, try again.")

    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully created a new dictionary where the "
        "new keys are the names of the users and the new values are dictionaries "
        "with the age and favourite colour of each user."
    )

def hint_1(
    my_dict_1: dict,
    my_dict_2: dict,
    my_dict_3: dict,
    my_list: list,
) -> None:
    assert isinstance(my_dict_1, dict), \
        ("The variable my_dict_1 should be a dictionary. "
         "Please, try again.")
    assert isinstance(my_dict_2, dict), \
        ("The variable my_dict_2 should be a dictionary. "
         "Please, try again.")
    assert isinstance(my_dict_3, dict), \
        ("The variable my_dict_3 should be a dictionary. "
         "Please, try again.")
    assert isinstance(my_list, list), \
        ("The variable my_list should be a list. "
         "Please, try again.")
    assert len(my_dict_1) == 3, \
        ("The dictionary my_dict_1 should have 3 key-value pairs. "
         "Please, try again.")
    assert len(my_dict_2) == 3, \
        ("The dictionary my_dict_2 should have 3 key-value pairs. "
         "Please, try again.")
    assert len(my_dict_3) == 3, \
        ("The dictionary my_dict_3 should have 3 key-value pairs. "
         "Please, try again.")
    assert len(my_list) == 3, \
        ("The list my_list should have 3 elements, each of which is a dictionary. "
         "Please, try again.")

    names_dict = {}
    for my_dict in my_list:
        name = my_dict["name"]
        age = my_dict["age"]
        favourite_colour = my_dict["favourite_colour"]
        names_dict[name] = {"age": age, "favourite_colour": favourite_colour}

    print(
        "First, create an empty dictionary called names_dict. "
        "Then, loop through my_list and get the name, age, and favourite colour of each person. "
        "Finally, add the name as a key to the names_dict dictionary "
        "and the age and favourite colour as a value. "
        f"In your case, 'names_dict' should look like this: {names_dict}"
    )
