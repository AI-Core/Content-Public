def check_step_1(
    my_string: str,
) -> None:
    assert isinstance(my_string, str), \
        "The value of 'my_string' is incorrect. It should be a string."
    assert my_string == "Hello World", \
        ("The value of 'my_string' is incorrect. "
         f"It should be 'Hello World' but it is '{my_string}'.")
    print("\033[92m\N{heavy check mark} Well done! "
          "You created a string with the value 'Hello World'.")
    

def check_step_2(
    my_string: str,
    my_length: int,
) -> None:
    assert isinstance(my_string, str), \
        "The value of 'my_string' is incorrect. It should be a string."
    assert isinstance(my_length, int), \
        ("The value of 'my_length' is incorrect. It should be an integer."
         "Please, make sure you are using the len() function.")
    assert my_string == "Hello World", \
        ("The value of 'my_string' is incorrect. "
         f"It should be 'Hello World' but it is '{my_string}'.")
    assert my_length == len(my_string), \
        ("The value of 'my_length' is incorrect. "
         "It should be the length of the string 'Hello World' (11).")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You created a string with the value 'Hello World' and "
        "you used the len() function to get its length."
    )

def check_step_3(
    ans_1: str,
) -> None:
    possible_answers = ["", "It checks the number of characters", "It checks the number of words in it"]
    assert isinstance(ans_1, str), \
        ("The value of 'ans_1' is incorrect. It should be a string."
         "Please, make sure you are using the form in this cell")
    assert ans_1 in possible_answers, \
        ("The value of 'ans_1' is not recognized. "
         "Please, use the drop-down menu to select the correct answer.")
    assert ans_1 == "It checks the number of characters", \
        ("Your answer is incorrect. "
         "Please, try again.")
    print("\033[92m\N{heavy check mark} Well done! "
          "The len() function checks the number of characters in a string.")
