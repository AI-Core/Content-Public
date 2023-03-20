def check_step_1(
    empty_set_1: set,
    set_1_type: str,
) -> None:
    assert isinstance(set_1_type, str), \
        ("The data type of set_1_type is incorrect. "
         "It should be a string. Please, make sure you are using the form in this cell.")
    assert len(empty_set_1) == 0, \
        ("The length of empty_set_1 is incorrect. "
         "It should be 0. "
         f"But your set has {len(empty_set_1)} elements.")
    assert set_1_type == "dict", \
        ("Your answer is incorrect. This is a tricky one. "
         "You can't create an empty set using curly braces. "
         "But it's good to know that curly brackets can be used to create sets or dictionaries. "
         "Please, try again.")

    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have created an empty set without using Python's built-in set() function."
    )

def check_step_2(
    empty_set_2: set,
    set_2_type: str,
) -> None:
    assert isinstance(empty_set_2, set), \
        ("The data type of empty_set_2 is incorrect. "
         "It should be a set.")
    assert isinstance(set_2_type, str), \
        ("The data type of set_2_type is incorrect. "
         "It should be a string. Please, make sure you are using the form in this cell.")
    assert len(empty_set_2) == 0, \
        ("The length of empty_set_2 is incorrect. "
         "It should be 0. "
         f"But your set has {len(empty_set_2)} elements.")
    assert set_2_type == "set", \
        ("Your answer is incorrect. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have created an empty set using Python's built-in set() function."
    )
