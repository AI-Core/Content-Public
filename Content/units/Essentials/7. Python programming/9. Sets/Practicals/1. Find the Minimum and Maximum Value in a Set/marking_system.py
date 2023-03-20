def check_step_1(
    max_int: int,
    max_str: str,
    set_int: set,
    set_str: set,
) -> None:
    expected_set_int = {8, 16, 24, 1, 25, 3, 10, 65, 55}
    expected_set_str = {'f', 'l', 'k', 'a', 'w'}
    assert isinstance(max_int, int), \
        ("The data type of max_int is incorrect. "
         "It should be an integer, please make sure you are getting the maximum value from 'set_int'.")
    assert isinstance(max_str, str), \
        ("The data type of max_str is incorrect. "
         "It should be a string, please make sure you are getting the maximum value from 'set_str'.")
    assert isinstance(set_int, set), \
        ("The data type of set_int is incorrect. "
         "It should be a set. Please, rerun the cell in step 1 to create the variable 'set_int'.")
    assert isinstance(set_str, set), \
        ("The data type of set_str is incorrect. "
         "It should be a set. Please, rerun the cell in step 1 to create the variable 'set_str'.")
    assert max_int == max(expected_set_int), \
        ("The maximum value of set_int is incorrect. "
         f"It should be {max(expected_set_int)}. "
         f"But your maximum value is {max_int}.")
    assert max_str == max(expected_set_str), \
        ("The maximum value of set_str is incorrect. "
         f"It should be {max(expected_set_str)}. "
         f"But your maximum value is {max_str}.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully found the maximum values in a set. "
        "Notice that the maximum value for alphabetical sets is the element that comes last in the alphabet."
    )

def check_step_2(
    min_int: int,
    min_str: str,
    set_int: set,
    set_str: set,
) -> None:
    expected_set_int = {4, 12, 10, 9, 4, 13}
    expected_set_str = {'b', 'z', 't', 'm', 'y', 'c'}
    assert isinstance(min_int, int), \
        ("The data type of min_int is incorrect. "
         "It should be an integer, please make sure you are getting the minimum value from 'set_int'.")
    assert isinstance(min_str, str), \
        ("The data type of min_str is incorrect. "
         "It should be a string, please make sure you are getting the minimum value from 'set_str'.")
    assert isinstance(set_int, set), \
        ("The data type of set_int is incorrect. "
         "It should be a set. Please, rerun the cell in step 2 to create the variable 'set_int'.")
    assert isinstance(set_str, set), \
        ("The data type of set_str is incorrect. "
         "It should be a set. Please, rerun the cell in step 2 to create the variable 'set_str'.")
    assert min_int == min(expected_set_int), \
        ("The minimum value of set_int is incorrect. "
         f"It should be {min(expected_set_int)}. "
         f"But your minimum value is {min_int}.")
    assert min_str == min(expected_set_str), \
        ("The minimum value of set_str is incorrect. "
         f"It should be {min(expected_set_str)}. "
         f"But your minimum value is {min_str}.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully found the minimum values in a set. "
        "Notice that the minimum value for alphabetical sets is the element that comes first in the alphabet."
    )
