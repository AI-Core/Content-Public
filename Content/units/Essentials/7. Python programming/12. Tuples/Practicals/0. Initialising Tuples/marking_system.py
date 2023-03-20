def check_step_1(
    empty_tuple: tuple,
) -> None:
    assert empty_tuple == (), \
        ("The value of 'empty_tuple' is incorrect. "
         "It should be an empty tuple. Use () to create an empty tuple.")

    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You created an empty tuple."
    )

def check_step_2(
    empty_tuple: tuple,
    empty_tuple_2: tuple,
    ans: str,
) -> None:
    assert isinstance(empty_tuple, tuple), \
        ("The data type of 'empty_tuple' is incorrect. "
         "It should be a tuple. Use () to create an empty tuple.")
    assert isinstance(empty_tuple_2, tuple), \
        ("The data type of 'empty_tuple_2' is incorrect. "
         "It should be a tuple. Use the tuple() function to create an empty tuple.")
    assert isinstance(ans, str), \
        ("The data type of 'ans' is incorrect. "
         "It should be a string. Make sure you are using the form in this cell.")
    assert empty_tuple == (), \
        ("The value of 'empty_tuple' is incorrect. "
         "It should be an empty tuple. Use () to create an empty tuple.")
    assert empty_tuple_2 == (), \
        ("The value of 'empty_tuple_2' is incorrect. "
         "It should be an empty tuple. Use the tuple() function to create an empty tuple.")
    assert ans == "No", \
        ("Your answer is incorrect. "
         "Please, try again.")

    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You learned two ways to create an empty tuple. "
        "Both methods will result in the same output."
    )

def check_step_3(
    my_tuple_1: tuple,
    my_tuple_2: tuple,
    my_tuple_3: tuple,
) -> None:
    assert isinstance(my_tuple_1, tuple), \
        ("The data type of 'my_tuple_1' is incorrect. "
         "It should be a tuple. Use () to create a tuple.")
    assert isinstance(my_tuple_2, tuple), \
        ("The data type of 'my_tuple_2' is incorrect. "
         "It should be a tuple. Use the tuple() function to create a tuple.")
    assert isinstance(my_tuple_3, tuple), \
        ("The data type of 'my_tuple_3' is incorrect. "
         "It should be a tuple. Use the tuple() function to create a tuple.")
    my_tuple_1_types = [type(item) for item in my_tuple_1]
    my_tuple_2_types = [type(item) for item in my_tuple_2]
    assert len(my_tuple_1) == 3, \
        ("The value of 'my_tuple_1' is incorrect. "
         "It should contain three elements.")
    assert len(set(my_tuple_1_types)) == 3, \
        ("The value of 'my_tuple_1' is incorrect. "
         "It should contain three different data types.")
    assert len(my_tuple_2) == 3, \
        ("The value of 'my_tuple_2' is incorrect. "
         "It should contain three elements.")
    assert len(set(my_tuple_2_types)) == 3, \
        ("The value of 'my_tuple_2' is incorrect. "
         "It should contain three different data types.")
    expected_tuple_3 = my_tuple_1 + my_tuple_2
    assert my_tuple_3 == expected_tuple_3, \
        ("The value of 'my_tuple_3' is incorrect. "
         "It should be the concatenation of 'my_tuple_1' and 'my_tuple_2'. "
         f"Your answer is {my_tuple_3} but the expected answer is {expected_tuple_3}.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You learned two ways to create a tuple "
        "and how to concatenate two tuples."
    )

