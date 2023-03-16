def check_step_1(
    ans_1: str,
) -> None:
    assert isinstance(ans_1, str), \
        ("The value of 'ans_1' is incorrect. It should be a string."
         "Please, make sure you are using the form in this cell")
    if (ans_1 == "true") or (ans_1 == "false"):
        raise ValueError(
            "The answer is incorrect. "
            "In Python, booleans are written with a capital letter. "
            "So, it should be 'True' or 'False'. "
            "Please, try again."
        )
    assert ans_1 == "True", \
        ("The value of 'ans_1' is incorrect. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "int_2 is greater than int_1, so the condition is True."
    )


def check_step_2(
    ans_1: str,
    ans_2: str,
) -> None:
    assert isinstance(ans_1, str), \
        ("The value of 'ans_1' is incorrect. It should be a string."
         "Please, make sure you are using the form in this cell")
    assert isinstance(ans_2, str), \
        ("The value of 'ans_2' is incorrect. It should be a string."
         "Please, make sure you are using the form in this cell")
    assert (ans_1 == "False") and (ans_2 == "True"), \
        ("Your answers are incorrect. "
         "In Python, the absence of a value is considered as False. "
         "So, a '0' are considered as False, but a non-zero number are considered as True "
         "even if it is negative. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "In Python, the absence of a value is considered as False. "
        "So, for example and empty string or a '0' are considered as False, "
        "whereas a non-empty string or a non-zero number are considered as True."
    )

def check_step_3(
    ans_1: str,
) -> None:
    possible_answers = ["==", "!=", ">", "<", ">=", "<="]
    assert isinstance(ans_1, str), \
        ("The value of 'ans_1' is incorrect. It should be a string."
         "Please, make sure you are using the form in this cell")
    assert ans_1 in possible_answers, \
        ("The value of 'ans_1' is not recognized. "
         "Please, make sure you are using the form in this cell")
    assert ans_1 == "!=", \
        ("The value of 'ans_1' is incorrect. "
         "Please, try again.")
    print("\033[92m\N{heavy check mark} Well done! "
          "To check if two values are different, we use the '!=' operator.")
