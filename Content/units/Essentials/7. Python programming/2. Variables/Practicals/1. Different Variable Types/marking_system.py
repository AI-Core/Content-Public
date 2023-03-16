def check_step_1(
    num: int,
    text_num: str,
    decimal_num: float,
) -> None:
    assert isinstance(num, int), "The variable 'num' should be a number."
    assert num == 23, "The variable 'num' should be equal to 23."
    assert isinstance(text_num, str), "The variable 'text_num' should be a text. Make sure you use quotation marks."
    assert text_num == "57", "The variable 'text_num' should be equal to '57'."
    assert isinstance(decimal_num, float), \
        "The variable 'decimal_num' should be a decimal number. Make sure you use a decimal point."
    assert decimal_num == 98.3, "The variable 'decimal_num' should be equal to 98.3."

    print("\033[92m\N{heavy check mark} Well done!")

def check_step_2(
    num_type: str,
    text_num_type: str,
    decimal_num_type: str,
) -> None:
    assert num_type == "int", "The variable 'num' should be an integer."
    assert text_num_type == "str", "The variable 'text_num' should be a string."
    assert decimal_num_type == "float", "The variable 'decimal_num' should be a float."
    print("\033[92m\N{heavy check mark} Well done!")

def check_step_3(
    ans_1: str,
    ans_2: str,
) -> None:
    ans_1_options = [
        "Yes",
        "No, because you can't add variables with different types",
        "No, because you can't add integers and floats"
    ]
    ans_2_options = [
        "Yes",
        "No, because you can't add variables with different types",
        "No, because you can't add integers and strings"
    ]
    if ans_1 not in ans_1_options:
        print("\033[91m\N{cross mark} Your answer for question 1 is not recognised. Please try again.")
    if ans_2 not in ans_2_options:
        print("\033[91m\N{cross mark} Your answer for question 2 is not recognised. Please try again.")
    if ans_1 == ans_1_options[0] and ans_2 == ans_2_options[2]:
        print("\033[92m\N{heavy check mark} Well done!")
    elif ans_1 == ans_1_options[1] or ans_2 == ans_2_options[1]:
        print("\033[91m\N{cross mark} Your answer for question 1 or 2 is almost correct, but not quite right. "
              "For example, integers and floats can be added together and they are different types. "
              "Please try again.")
    else:
        print("\033[91m\N{cross mark} Your answer for question 1 or 2 is incorrect. Please try again.")

def check_step_4(
    ans_1: str,
) -> None:
    ans_1_options = [
        "Yes",
        "No, because you can't add variables with different types",
        "No, because you can't add integers and strings"
    ]
    if ans_1 not in ans_1_options:
        print("\033[91m\N{cross mark} Your answer for question 1 is not recognised. Please try again.")
    if ans_1 == ans_1_options[0]:
        print("\033[92m\N{heavy check mark} Well done! You can add new_num and num because they are both integers.")
    else:
        print("\033[91m\N{cross mark} That's not quite right. Please try again.")
