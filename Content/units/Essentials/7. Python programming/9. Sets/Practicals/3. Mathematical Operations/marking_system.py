expected_set_1 = {15, 25, 35, 45, 55}
expected_set_2 = {35, 45, 55, 65, 75}

def check_step_1(
    common_items: set,
    ans: str,
    set_1: set,
    set_2: set,
) -> None:
    assert isinstance(common_items, set), \
        ("The data type of common_items is incorrect. "
         "It should be a set. Please, make sure you created it using a set method.")
    assert isinstance(set_1, set), \
        ("The data type of set_1 is incorrect. "
         "It should be a set. Please, run the cell in step 1 to create the variable 'set_1'.")
    assert set_1 == expected_set_1, \
        ("The set_1 is incorrect. "
         "It should contain the following elements: {15, 25, 35, 45, 55}. "
         "Please, run the cell in step 1 to create the variable 'set_1'.")
    assert isinstance(set_2, set), \
        ("The data type of set_2 is incorrect. "
         "It should be a set. Please, run the cell in step 1 to create the variable 'set_2'.")
    assert set_2 == expected_set_2, \
        ("The set_2 is incorrect. "
         "It should contain the following elements: {35, 45, 55, 65, 75}. "
         "Please, run the cell in step 1 to create the variable 'set_2'.")
    assert isinstance(ans, str), \
        ("The data type of ans is incorrect. "
         "It should be a string. Please, make sure you are using the form in this cell.")
    assert ans == "intersection", \
        ("The answer is incorrect. "
         "Please, try again.")
    expected_common_items = set_1.intersection(set_2)
    assert expected_common_items == common_items, \
        ("Your set is incorrect. "
         "It should contain the common elements between set_1 and set_2. "
         f"The common elements between {set_1} and {set_2} are {expected_common_items}.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully found the common elements between two sets."
    )

def check_step_2(
    set_1_only: set,
    ans: str,
    set_1: set,
    set_2: set,
) -> None:
    assert isinstance(set_1_only, set), \
        ("The data type of set_1_only is incorrect. "
         "It should be a set. Please, make sure you created it using a set method.")
    assert isinstance(set_1, set), \
        ("The data type of set_1 is incorrect. "
         "It should be a set. Please, run the cell in step 1 to create the variable 'set_1'.")
    assert set_1 == expected_set_1, \
        ("The set_1 is incorrect. "
         "It should contain the following elements: {15, 25, 35, 45, 55}. "
         "Please, run the cell in step 1 to create the variable 'set_1'.")
    assert isinstance(set_2, set), \
        ("The data type of set_2 is incorrect. "
         "It should be a set. Please, run the cell in step 1 to create the variable 'set_2'.")
    assert set_2 == expected_set_2, \
        ("The set_2 is incorrect. "
         "It should contain the following elements: {35, 45, 55, 65, 75}. "
         "Please, run the cell in step 1 to create the variable 'set_2'.")
    assert isinstance(ans, str), \
        ("The data type of ans is incorrect. "
         "It should be a string. Please, make sure you are using the form in this cell.")
    assert ans == "difference", \
        ("The answer is incorrect. "
         "Please, try again.")
    expected_set_1_only = set_1.difference(set_2)
    assert expected_set_1_only == set_1_only, \
        ("Your set is incorrect. "
         "It should contain the elements that are only in set_1. "
         f"The elements that are only in {set_1} are {expected_set_1_only}.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully found the elements that are only in set_1."
    )

def check_step_3(
    set_2_only: set,
    ans: str,
    set_1: set,
    set_2: set,
) -> None:
    assert isinstance(set_2_only, set), \
        ("The data type of set_1_only is incorrect. "
         "It should be a set. Please, make sure you created it using a set method.")
    assert isinstance(set_1, set), \
        ("The data type of set_1 is incorrect. "
         "It should be a set. Please, run the cell in step 1 to create the variable 'set_1'.")
    assert set_1 == expected_set_1, \
        ("The set_1 is incorrect. "
         "It should contain the following elements: {15, 25, 35, 45, 55}. "
         "Please, run the cell in step 1 to create the variable 'set_1'.")
    assert isinstance(set_2, set), \
        ("The data type of set_2 is incorrect. "
         "It should be a set. Please, run the cell in step 1 to create the variable 'set_2'.")
    assert set_2 == expected_set_2, \
        ("The set_2 is incorrect. "
         "It should contain the following elements: {35, 45, 55, 65, 75}. "
         "Please, run the cell in step 1 to create the variable 'set_2'.")
    assert isinstance(ans, str), \
        ("The data type of ans is incorrect. "
         "It should be a string. Please, make sure you are using the form in this cell.")
    assert ans == "difference", \
        ("The answer is incorrect. "
         "Please, try again.")
    expected_set_2_only = set_2.difference(set_1)
    assert expected_set_2_only == set_2_only, \
        ("Your set is incorrect. "
         "It should contain the elements that are only in set_2. "
         f"The elements that are only in {set_2} are {expected_set_2_only}.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully found the elements that are only in set_2."
    )

def check_step_4(
    set_1_and_2: set,
    ans: str,
    set_1: set,
    set_2: set,
) -> None:
    assert isinstance(set_1_and_2, set), \
        ("The data type of set_1_and_2 is incorrect. "
         "It should be a set. Please, make sure you created it using a set method.")
    assert isinstance(set_1, set), \
        ("The data type of set_1 is incorrect. "
         "It should be a set. Please, run the cell in step 1 to create the variable 'set_1'.")
    assert set_1 == expected_set_1, \
        ("The set_1 is incorrect. "
         "It should contain the following elements: {15, 25, 35, 45, 55}. "
         "Please, run the cell in step 1 to create the variable 'set_1'.")
    assert isinstance(set_2, set), \
        ("The data type of set_2 is incorrect. "
         "It should be a set. Please, run the cell in step 1 to create the variable 'set_2'.")
    assert set_2 == expected_set_2, \
        ("The set_2 is incorrect. "
         "It should contain the following elements: {35, 45, 55, 65, 75}. "
         "Please, run the cell in step 1 to create the variable 'set_2'.")
    assert isinstance(ans, str), \
        ("The data type of ans is incorrect. "
         "It should be a string. Please, make sure you are using the form in this cell.")
    assert ans == "union", \
        ("The answer is incorrect. "
         "Please, try again.")
    expected_set_1_and_2 = set_1.union(set_2)
    assert expected_set_1_and_2 == set_1_and_2, \
        ("Your set is incorrect. "
         "It should contain the elements that are in set_1 or set_2. "
         f"The elements that are in {set_1} or {set_2} are {expected_set_1_and_2}.") 
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully found the elements that are in set_1 or set_2."
    )

def check_step_5(
    set_1_or_2: set,
    ans: str,
    set_1: set,
    set_2: set,
) -> None:
    assert isinstance(set_1_or_2, set), \
        ("The data type of set_1_or_2 is incorrect. "
            "It should be a set. Please, make sure you created it using a set method.")
    assert isinstance(set_1, set), \
        ("The data type of set_1 is incorrect. "
         "It should be a set. Please, run the cell in step 1 to create the variable 'set_1'.")
    assert set_1 == expected_set_1, \
        ("The set_1 is incorrect. "
         "It should contain the following elements: {15, 25, 35, 45, 55}. "
         "Please, run the cell in step 1 to create the variable 'set_1'.")
    assert isinstance(set_2, set), \
        ("The data type of set_2 is incorrect. "
         "It should be a set. Please, run the cell in step 1 to create the variable 'set_2'.")
    assert set_2 == expected_set_2, \
        ("The set_2 is incorrect. "
         "It should contain the following elements: {35, 45, 55, 65, 75}. "
         "Please, run the cell in step 1 to create the variable 'set_2'.")
    assert isinstance(ans, str), \
        ("The data type of ans is incorrect. "
         "It should be a string. Please, make sure you are using the form in this cell.")
    assert ans == "symmetric_difference", \
        ("The answer is incorrect. "
         "Please, try again.")
    expected_set_1_or_2 = set_1.symmetric_difference(set_2)
    assert expected_set_1_or_2 == set_1_or_2, \
        ("Your set is incorrect. "
         "It should contain the elements that are in set_1 or set_2 but not both. "
         "Please, make sure you are using the correct set method.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully found the elements that are in set_1 or set_2 but not both."
    )



