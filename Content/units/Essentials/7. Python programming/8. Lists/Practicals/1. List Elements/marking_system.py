def check_step_1(
    list_1: list,
) -> None:
    assert isinstance(list_1, list), \
        ("The data type of 'list_1' is incorrect. "
         "It should be a list")
    assert len(list_1) == 4, \
        ("The length of 'list_1' is incorrect. "
         "It should contain four elements")
    data_types = [type(item) for item in list_1]
    assert len(set(data_types)) == 4, \
        ("The data types of the elements in 'list_1' are incorrect. "
         "It should contain four different data types. "
         f"Your list contains {set(data_types)}")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully created a list with four different data types."
    )


def check_step_2(
    list_2: list,
) -> None:
    '''
    Checks that list_2 is [0] * 10
    '''
    assert isinstance(list_2, list), \
        ("The data type of 'list_2' is incorrect. "
         "It should be a list")
    assert len(list_2) == 10, \
        ("The length of 'list_2' is incorrect. "
         "It should contain ten elements")
    assert list_2 == [0] * 10, \
        ("The value of 'list_2' is incorrect. "
         "It should contain ten zeros")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully created a list with ten zeros."
    )

def check_step_3(
    list_1: list,
    list_2: list,
    list_3: list,
) -> None:
    assert isinstance(list_1, list), \
        ("The data type of 'list_1' is incorrect. "
         "It should be a list")
    assert isinstance(list_2, list), \
        ("The data type of 'list_2' is incorrect. "
         "It should be a list")
    assert isinstance(list_3, list), \
        ("The data type of 'list_3' is incorrect. "
         "It should be a list")
    assert len(list_3) == 2, \
        ("The length of 'list_3' is incorrect. "
         "It should contain two elements: 'list_1' and 'list_2'")
    assert list_3[0] == list_1, \
        ("The first element of 'list_3' is incorrect. "
         "It should be 'list_1'")
    assert list_3[1] == list_2, \
        ("The second element of 'list_3' is incorrect. "
         "It should be 'list_2'")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully created a list with two elements: 'list_1' and 'list_2'. "
        "Remember that you can create nested lists"
    )

def check_step_4(
    list_1: list,
    list_2: list,
    list_4: list,
) -> None:
    '''
    Checks that usernames_2 is a copy of the last five elements of usernames

    Then, it will assert that user_example is the second element of usernames_2
    '''
    assert isinstance(list_1, list), \
        ("The data type of 'list_1' is incorrect. "
         "It should be a list")
    assert isinstance(list_2, list), \
        ("The data type of 'list_2' is incorrect. "
         "It should be a list")
    assert isinstance(list_4, list), \
        ("The data type of 'list_4' is incorrect. "
         "It should be a list")

    assert len(list_4) == 2, \
        ("The length of 'list_4' is incorrect. "
         "It should contain two elements: the fourth element of 'list_1' and the fourth element of 'list_2'")

    expected_fourth_element_1 = list_1[3]
    expected_fourth_element_2 = list_2[3]

    assert list_4[0] == expected_fourth_element_1, \
        ("The first element of 'list_4' is incorrect. "
         "It should be the fourth element of 'list_1'. "
         "In your case, the fourth element of 'list_1' is "
         f"{expected_fourth_element_1} ,"
         f"but you have {list_4[0]}."
         "Remember that Python is zero-indexed")

    assert list_4[1] == expected_fourth_element_2, \
        ("The second element of 'list_4' is incorrect. "
         "It should be the fourth element of 'list_2'. "
         "In your case, the fourth element of 'list_2' is "
         f"{expected_fourth_element_2} ,"
         f"but you have {list_4[1]}"
         "Remember that Python is zero-indexed")

    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully created a list with two elements: the fourth element of 'list_1' and the fourth element of 'list_2'. "
    )
