def check_step_1(
    answer: str,
) -> None:
    ans_possible = [
        "Yes",
        "No, because the second quotation mark closes the first one",
        "No, because you can't use quotation marks in a string"
    ]
    assert isinstance(answer, str), \
        ("The value of your answer is not a string. "
         "Please, make sure you are using the options in the dropdown menu.")
    assert answer in ans_possible, \
        ("The value of your answer is not recognised. "
         "Please, make sure you are using the options in the dropdown menu.")
    if answer == "Yes":
        raise AssertionError(
            "Not quite right, you shouldn't be able to create the string"
            " because the second quotation mark closes the first one."
        )
    elif answer == "No, because the second quotation mark closes the first one":
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "That's correct, you can't create the string because the second quotation mark closes the first one."
        )
    elif answer == "No, because you can't use quotation marks in a string":
        raise AssertionError(
            "Sorry, the answer is incorrect. You can use quotation marks in a string."
        )

def check_step_2(
    answer: str,
) -> None:
    ans_possible = [
        "Yes",
        "No, because the second quotation mark closes the first one",
        "No, because you can't use quotation marks in a string"
    ]
    assert isinstance(answer, str), \
        ("The value of your answer is not a string. "
         "Please, make sure you are using the options in the dropdown menu.")
    assert answer in ans_possible, \
        ("The value of your answer is not recognised. "
         "Please, make sure you are using the options in the dropdown menu.")
    if answer == "Yes":
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "Here, there wasn't any issue because inside the quotation marks "
            "we are using single quotation marks, and they don't close the string."
        )
    else:
        raise AssertionError(
            "Not quite right, you should be able to create the string "
            "if you use single quotation marks."
        )

def check_step_3(
    answer: str,
) -> None:
    ans_possible = [
        "Yes",
        "No, because the second quotation mark closes the first one",
        "No, because you can't use quotation marks in a string"
    ]
    assert isinstance(answer, str), \
        ("The value of your answer is not a string. "
         "Please, make sure you are using the options in the dropdown menu.")
    assert answer in ans_possible, \
        ("The value of your answer is not recognised. "
         "Please, make sure you are using the options in the dropdown menu.")
    if answer == "Yes":
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "Here, there wasn't any issue because the quotation marks "
            "were escaped with a backslash, so they don't close the string."
        )
    else:
        raise AssertionError(
            "Not quite right, you should be able to create "
            "the string if you escape the quotation marks with a backslash."
        )
