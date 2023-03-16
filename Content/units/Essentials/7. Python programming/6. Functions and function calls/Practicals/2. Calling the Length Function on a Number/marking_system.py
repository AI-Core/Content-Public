def check_step_1(
    my_number: int,
) -> None:
    assert isinstance(my_number, int), \
        "The value of 'my_number' is incorrect. It should be an integer."
    assert my_number == 5, \
        ("The value of 'my_number' is incorrect. "
         f"It should be 5 but it is {my_number}.")
    print("\033[92m\N{heavy check mark} Well done! "
          "You created an integer with the value 5.")
    

def check_step_2(
    ans_1: str,
) -> None:
    possible_answers = ["Yes, it worked", "AssertionError", "TypeError", "NameError", "SyntaxError"]
    assert isinstance(ans_1, str), \
        ("The value of 'ans_1' is incorrect. It should be a string."
         "Please, make sure you are using the form in this cell")
    assert ans_1 in possible_answers, \
        ("The value of 'ans_1' is not recognized. "
         "Please, use the drop-down menu to select the correct answer.")
    assert ans_1 == "TypeError", \
        ("Your answer is incorrect. "
         "Please, try again.")
    print("\033[92m\N{heavy check mark} Well done! "
          "The len() function does not work on numbers."
          "The TypeError is raised because the len() function "
          "can't operate with that Type of data.")