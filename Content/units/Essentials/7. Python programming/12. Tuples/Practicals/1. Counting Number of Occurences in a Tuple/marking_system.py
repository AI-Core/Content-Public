def check_step_1(
    ans: str,
) -> None:
    assert isinstance(ans, str), \
        ("The data type of 'ans' is incorrect. "
         "It should be a string. Make sure you are using the form in this cell.")
    assert ans == "count()", \
        ("Your answer is incorrect. "
         "Please, try again.")

    print(
        "\033[92m\N{heavy check mark} Well done! "
        "The 'count()' method is used to count the number of times an element appears in a tuple."
    )

def check_step_2(
    count_1: int,
    count_2: int,
    my_tuple: tuple,
) -> None:
    expected_my_tuple = (1, 'f', [1, 2, 3], [4, 5], ('f', 'd'), ('f', 'd', 'e'), [1, 2, 3], 'a')
    assert isinstance(count_1, int), \
        ("The data type of 'count_1' is incorrect. "
         "It should be an integer. Make sure you are using the correct method.")
    assert isinstance(count_2, int), \
        ("The data type of 'count_2' is incorrect. "
         "It should be an integer. Make sure you are using the correct method.")
    assert isinstance(my_tuple, tuple), \
        ("The data type of 'my_tuple' is incorrect. "
         "It should be a tuple. Please, run the cell again.")
    assert my_tuple == expected_my_tuple, \
        ("The tuple 'my_tuple' is incorrect. "
         "Please, run the cell again.")
    expected_count_1 = my_tuple.count([1, 2, 3])
    expected_count_2 = my_tuple.count(('f', 'd'))
    assert count_1 == expected_count_1, \
        ("The value of 'count_1' is incorrect. "
         "You need to count the number of times the list [1, 2, 3] appears in the tuple 'my_tuple'. "
         "A list is treated as a single object in a tuple.")
    
    assert count_2 == expected_count_2, \
        ("The value of 'count_2' is incorrect. "
         "You need to count the number of times the tuple ('f', 'd') appears in the tuple 'my_tuple'. "
         "A tuple is treated as a single object in a tuple.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "Each element in a tuple is treated as a single object, regardless of its data type."
    )

