from typing import List

def check_step_1(
    year_1: str,
    year_2: str,
    year_3: str,
    plates: List[str],
) -> None:
    '''
    Checks that each year are the last two characters of the corresponding plate
    '''

    assert isinstance(year_1, str), \
        ("The data type of 'year_1' is incorrect. "
         "It should be a string. Make sure you haven't changed its type")
    assert isinstance(year_2, str), \
        ("The data type of 'year_2' is incorrect. "
         "It should be a string. Make sure you haven't changed its type")
    assert isinstance(year_3, str), \
        ("The data type of 'year_3' is incorrect. "
         "It should be a string. Make sure you haven't changed its type")
    assert isinstance(plates, list), \
        ("The data type of 'plates' is incorrect. "
         "It should be a list. Please, rerun the cell in step 1 to create the variable 'plates'")

    assert year_1 == plates[0].split()[0][-2:], \
        ("The value of 'year_1' is incorrect. "
         "It should be the last two characters of the first element of 'plates'. "
         f"Please, try again. Hint: {plates[0].split()[0][:-2]}")
    assert year_2 == plates[1].split()[0][-2:], \
        ("The value of 'year_2' is incorrect. "
         "It should be the last two characters of the second element of 'plates'")
    assert year_3 == plates[2].split()[0][-2:], \
        ("The value of 'year_3' is incorrect. "
         "It should be the last two characters of the third element of 'plates'")
    
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully created 'year_1', 'year_2' and 'year_3'. "
        "Were you able to create each variable in a single line of code?"
    )

def check_step_2(
    ans: str,
) -> None:
    '''
    Checks that the answer is correct
    '''
    possible_answers = ["str", "int", "float", "list", "tuple", "dict", "set"]
    assert isinstance(ans, str), \
        ("The data type of 'ans' is incorrect. "
         "It should be a string. Please, use the form in this cell to create the variable 'ans'")
    
    assert ans in possible_answers, \
        ("The value of 'ans' is not recognised. "
         "Make sure you are using the form in this cell to create the variable 'ans'")
    
    assert ans == "str", \
        ("Your answer is incorrect. "
         "Please, try again.")
    
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "The variable 'ans' is a string. In this case, you have a list "
        "of strings, and getting a slice of a string returns a string."
    )

def check_step_3(
    year_1: int,
    year_2: int,
    year_3: int,
    plates: List[str],
) -> None:
    '''
    Checks that each year are the last two characters of the corresponding plate
    '''
    assert isinstance(year_1, int), \
        ("The data type of 'year_1' is incorrect. "
         "It should be an integer. Make sure you have changed its type")
    assert isinstance(year_2, int), \
        ("The data type of 'year_2' is incorrect. "
         "It should be an integer. Make sure you have changed its type")
    assert isinstance(year_3, int), \
        ("The data type of 'year_3' is incorrect. "
         "It should be an integer. Make sure you have changed its type")
    assert isinstance(plates, list), \
        ("The data type of 'plates' is incorrect. "
         "It should be a list. Please, rerun the cell in step 1 to create the variable 'plates'")

    expected_year_1 = int(plates[0].split(" ")[0][-2:])
    expected_year_2 = int(plates[1].split(" ")[0][-2:])
    expected_year_3 = int(plates[2].split(" ")[0][-2:])

    assert year_1 == expected_year_1, \
        ("The value of 'year_1' is incorrect. "
         "It should be the last two characters of the first element of 'plates' converted to an integer. "
         f"Please, try again. Hint: {expected_year_1}")
    assert year_2 == expected_year_2, \
        ("The value of 'year_2' is incorrect. "
         "It should be the last two characters of the second element of 'plates' converted to an integer")
    assert year_3 == expected_year_3, \
        ("The value of 'year_3' is incorrect. "
         "It should be the last two characters of the third element of 'plates' converted to an integer")
    
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully casted 'year_1', 'year_2' and 'year_3' to integers. "
    )