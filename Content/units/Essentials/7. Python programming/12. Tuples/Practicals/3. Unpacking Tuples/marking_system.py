def check_step_1(
    a: str,
    b: str,
    c: int,
    d: bool,
    ans: str,
) -> None:
    assert isinstance(a, str), \
        ("The data type of 'a' is incorrect. "
         "It should be a string containing the word 'Hello'.")
    assert isinstance(b, str), \
        ("The data type of 'b' is incorrect. "
         "It should be a string containing the word 'World'.")
    assert isinstance(c, int), \
        ("The data type of 'c' is incorrect. "
         "It should be an integer containing the number 1.")
    assert isinstance(d, bool), \
        ("The data type of 'd' is incorrect. "
         "It should be a boolean containing the value True.")
    assert isinstance(ans, str), \
        ("The data type of 'ans' is incorrect. "
         "It should be a string. Make sure you are using the form in this cell.")
    assert ans == "ValueError: too many values to unpack", \
        ("Your answer is incorrect. "
         "Please, try again.")
    assert a == "Hello", \
        ("The value of 'a' is incorrect. "
         "Make sure you are unpacking the tuple correctly.")
    assert b == "World", \
        ("The value of 'b' is incorrect. "
         "Make sure you are unpacking the tuple correctly.")
    assert c == 1, \
        ("The value of 'c' is incorrect. "
         "Make sure you are unpacking the tuple correctly.")
    assert d, \
        ("The value of 'd' is incorrect. "
         "Make sure you are unpacking the tuple correctly.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You can unpack a tuple into multiple variables."
    )

def check_step_2(
    ans_x: str,
    ans_y: str,
    ans_z: str,
    my_tuple: tuple,
) -> None:
    given_tuple = (70, "AiCore", 10, "Programming", 70)
    expected_x, *expected_y, expected_z = given_tuple
    assert my_tuple == given_tuple, \
        ("The tuple 'my_tuple' is incorrect. "
         "Please, run the cell to create the tuple again.")

    assert isinstance(ans_x, str), \
        ("The data type of 'ans_x' is incorrect. "
         "It should be a string. Make sure you are using the form in this cell.")
    assert isinstance(ans_y, str), \
        ("The data type of 'ans_y' is incorrect. "
         "It should be a string. Make sure you are using the form in this cell.")
    assert isinstance(ans_z, str), \
        ("The data type of 'ans_z' is incorrect. "
         "It should be a string. Make sure you are using the form in this cell.")
    assert ans_x == "70", \
        ("Your answer is incorrect. "
         f"x should contain the first element of the tuple, which is {expected_x}.")
    assert ans_y == "['AiCore', 10, 'Programming']", \
        ("Your answer is incorrect. "
         f"y should contain the middle elements of the tuple, which are {expected_y}.")
    assert ans_z == "70", \
        ("Your answer is incorrect. "
         f"z should contain the last element of the tuple, which is {expected_z}.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You can use the '*' operator to unpack the extra elements of a tuple into a list."
    )

def check_step_3(
    ans_x: str,
    ans_y: str,
    ans_z: str,
    my_tuple: tuple,
) -> None:
    given_tuple = (70, "AiCore", 10, "Programming", 70)
    expected_x, expected_y, *expected_z = given_tuple
    assert my_tuple == given_tuple, \
        ("The tuple 'my_tuple' is incorrect. "
         "Please, run the cell to create the tuple again.")
    
    assert isinstance(ans_x, str), \
        ("The data type of 'ans_x' is incorrect. "
         "It should be a string. Make sure you are using the form in this cell.")
    assert isinstance(ans_y, str), \
        ("The data type of 'ans_y' is incorrect. "
         "It should be a string. Make sure you are using the form in this cell.")
    assert isinstance(ans_z, str), \
        ("The data type of 'ans_z' is incorrect. "
         "It should be a string. Make sure you are using the form in this cell.")
    assert ans_x == "70", \
        ("Your answer is incorrect. "
         f"x should contain the first element of the tuple, which is {expected_x}.")
    assert ans_y == "AiCore", \
        ("Your answer is incorrect. "
         f"y should contain the second element of the tuple, which is {expected_y}.")
    assert ans_z == "[10, 'Programming', 70]", \
        ("Your answer is incorrect. "
         f"z should contain the last three elements of the tuple, which are {expected_z}.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "Depending on the position of the '*' operator, you can unpack the extra elements of a tuple into a list."
    )
