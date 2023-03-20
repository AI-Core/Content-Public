expected_list_1 = [1, 5, 10, 20, 40, 80]
expected_list_2 = [6, 7, 20, 80, 100]
expected_list_3 = [3, 4, 15, 20, 30, 70, 80, 120]

def check_step_1(
    common_1_2: set,
    list_1: list,
    list_2: list,
) -> None:
    assert isinstance(common_1_2, set), \
        ("The data type of common_1_2 is incorrect. "
         "It should be a set. Please, make sure you created it using a set method.")
    assert isinstance(list_1, list), \
        ("The data type of list_1 is incorrect. "
         "It should be a list. Please, run the cell in step 1 to create the variable 'list_1'.")
    assert list_1 == expected_list_1, \
        ("The list_1 is incorrect. "
         "It should contain the following elements: [1, 5, 10, 20, 40, 80]. "
         "Please, run the cell in step 1 to create the variable 'list_1'.")
    assert isinstance(list_2, list), \
        ("The data type of list_2 is incorrect. "
         "It should be a list. Please, run the cell in step 1 to create the variable 'list_2'.")
    assert list_2 == expected_list_2, \
        ("The list_2 is incorrect. "
         "It should contain the following elements: [6, 7, 20, 80, 100]. "
         "Please, run the cell in step 1 to create the variable 'list_2'.")
    expected_common_1_2 = set(list_1).intersection(set(list_2))
    assert expected_common_1_2 == common_1_2, \
        ("Your set is incorrect. "
         "It should contain the common elements between list_1 and list_2. "
         f"The common elements between {list_1} and {list_2} are {expected_common_1_2}.")
    
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully found the common elements between list_1 and list_2."
    )

def check_step_2(
    common_1_2_3: set,
    list_1: list,
    list_2: list,
    list_3: list,
) -> None:
    assert isinstance(common_1_2_3, set), \
        ("The data type of common_1_2_3 is incorrect. "
         "It should be a set. Please, make sure you created it using a set method.")
    assert isinstance(list_1, list), \
        ("The data type of list_1 is incorrect. "
         "It should be a list. Please, run the cell in step 1 to create the variable 'list_1'.")
    assert list_1 == expected_list_1, \
        ("The list_1 is incorrect. "
         "It should contain the following elements: [1, 5, 10, 20, 40, 80]. "
         "Please, run the cell in step 1 to create the variable 'list_1'.")
    assert isinstance(list_2, list), \
        ("The data type of list_2 is incorrect. "
         "It should be a list. Please, run the cell in step 1 to create the variable 'list_2'.")
    assert list_2 == expected_list_2, \
        ("The list_2 is incorrect. "
         "It should contain the following elements: [6, 7, 20, 80, 100]. "
         "Please, run the cell in step 1 to create the variable 'list_2'.")
    assert isinstance(list_3, list), \
        ("The data type of list_3 is incorrect. "
         "It should be a list. Please, run the cell in step 1 to create the variable 'list_3'.")
    assert list_3 == expected_list_3, \
        ("The list_3 is incorrect. "
         "It should contain the following elements: [3, 4, 15, 20, 30, 70, 80, 120]. "
         "Please, run the cell in step 1 to create the variable 'list_3'.")
    expected_common_1_2_3 = set(list_1).intersection(set(list_2), set(list_3))
    assert expected_common_1_2_3 == common_1_2_3, \
        ("Your set is incorrect. "
         "It should contain the common elements between list_1, list_2 and list_3. "
         f"The common elements between {list_1}, {list_2} and {list_3} are {expected_common_1_2_3}.")
    
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully found the common elements between list_1, list_2 and list_3."
    )
