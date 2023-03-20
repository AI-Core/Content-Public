def check_step_1(
    name_1: str,
    name_2: str,
) -> None:
    '''
    Checks that name_1 and name_2 are non-empty strings
    '''
    assert isinstance(name_1, str), \
        ("The data type of 'name_1' is incorrect. "
         "It should be a string. Please, try again.")
    assert isinstance(name_2, str), \
        ("The data type of 'name_2' is incorrect. "
         "It should be a string. Please, try again.")
    assert len(name_1) > 3, \
        ("The value of 'name_1' is incorrect. "
         "It should contain at least 4 characters. Please, try again.")
    assert len(name_2) > 3, \
        ("The value of 'name_2' is incorrect. "
         "It should contain at least 4 characters. Please, try again.")
    
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "The variables 'name_1' and 'name_2' are strings with at least 4 characters."
    )


def check_step_2(
    name_1: str,
    name_2: str,
    name_intersection: set,
) -> None:
    '''
    Checks that the answer is correct
    '''
    assert isinstance(name_1, str), \
        ("The data type of 'name_1' is incorrect. "
         "It should be a string. Please, try again.")
    assert isinstance(name_2, str), \
        ("The data type of 'name_2' is incorrect. "
         "It should be a string. Please, try again.")
    assert len(name_1) > 3, \
        ("The value of 'name_1' is incorrect. "
         "It should contain at least 4 characters. Please, try again.")
    assert len(name_2) > 3, \
        ("The value of 'name_2' is incorrect. "
         "It should contain at least 4 characters. Please, try again.")
    assert isinstance(name_intersection, set), \
        ("The data type of 'name_intersection' is incorrect. "
         "It should be a set. Please, use the right set method. Try again.")
    
    name_1_set = set(name_1)
    name_2_set = set(name_2)
    name_intersection_correct = name_1_set.intersection(name_2_set)

    assert name_intersection == name_intersection_correct, \
        ("The value of 'name_intersection' is incorrect. "
         "It should be the intersection of 'name_1' and 'name_2'. "
         f"In your case, it is {name_intersection_correct}. "
         "Try to find the way to get the intersection of two sets.")    
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully found the intersection of the two names."
    )
