def check_step_1(
    my_list_1: list,
    my_list_2: list,
) -> None:
    assert isinstance(my_list_1, list), \
        ("The data type of my_list_1 is incorrect. "
         "It should be a list.")
    assert isinstance(my_list_2, list), \
        ("The data type of my_list_2 is incorrect. "
         "It should be a list.")
    expected_list_2 = [5, 6, 7, 8]
    expected_list_1 = [1, 2, 3, 4, [5, 6, 7, 8]]
    expected_len = len(expected_list_1)
    assert my_list_2 == expected_list_2, \
        ("The value of my_list_2 is incorrect. "
         "Have you changed the value of my_list_2? "
         "It should be [5, 6, 7, 8].")
    assert len(my_list_1) == expected_len, \
        ("The length of my_list_1 is incorrect. "
         f"It should be {expected_len} because "
         "the append method adds the whole list as a single element.")
    assert my_list_1 == expected_list_1, \
        ("The value of my_list_1 is incorrect. "
         f"It should be {expected_list_1} because "
         "the last element of my_list_1 is list_2.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully appended a list to another list."
    )

def check_step_2(
    my_list_1: list,
    my_list_2: list,
) -> None:
    assert isinstance(my_list_1, list), \
        ("The data type of my_list_1 is incorrect. "
         "It should be a list.")
    assert isinstance(my_list_2, list), \
        ("The data type of my_list_2 is incorrect. "
         "It should be a list.")
    expected_list_2 = [5, 6, 7, 8]
    expected_list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
    expected_len = len(expected_list_1)
    assert my_list_2 == expected_list_2, \
        ("The value of my_list_2 is incorrect. "
         "Have you changed the value of my_list_2? "
         "It should be [5, 6, 7, 8].")
    assert len(my_list_1) == expected_len, \
        ("The length of my_list_1 is incorrect. "
         f"It should be {expected_len} because "
         "the extend method adds the elements of the list to the list.")
    assert my_list_1 == expected_list_1, \
        ("The value of my_list_1 is incorrect. "
         f"It should be {expected_list_1} because "
         "the extend method adds the elements of the list to the list.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully extended a list with another list."
    )