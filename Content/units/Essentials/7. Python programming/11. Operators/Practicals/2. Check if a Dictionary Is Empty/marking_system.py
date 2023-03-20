def check_step_1(
    ans_1: str,
    ans_2: str,
    ans_3: str,
) -> None:
    assert isinstance(ans_1, str), \
        ("The data type of 'ans_1' is incorrect. "
         "It should be a string. Make sure you are using the form in this cell.")
    assert isinstance(ans_2, str), \
        ("The data type of 'ans_2' is incorrect. "
         "It should be a string. Make sure you are using the form in this cell.")
    assert isinstance(ans_3, str), \
        ("The data type of 'ans_3' is incorrect. "
         "It should be a string. Make sure you are using the form in this cell.")

    assert ans_1 == "not bool(my_dict)", \
        ("Your answer is incorrect. "
         "Just using bool(my_dict) will return False if the dictionary is empty.")
    assert ans_2 == "len(my_dict) == 0", \
        ("Your answer is incorrect. "
         "If you use 'len(my_dict) != 1', you will get True if the dictionary has more than one element.")
    assert ans_3 == "my_dict == {}", \
        ("Your answer is incorrect. "
         "If you use 'my_dict is {}', you will get False because Python is creating a new object ."
         "Remember that 'is' is used to check if two objects are the same object.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "All your answers are correct. "
        "The same methods you used to check if the dictionary is empty can be used on other data types."
    )
