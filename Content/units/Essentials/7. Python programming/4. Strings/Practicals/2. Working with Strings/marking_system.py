def check_step_1(
    test_string: str,
    second_char: str,
) -> None:
    assert isinstance(test_string, str), "The value of 'test_string' is incorrect. It should be a string."
    assert isinstance(second_char, str), "The value of 'second_char' is incorrect. It should be a string."

    assert test_string == "hello", "The value of 'test_string' is incorrect. It should be 'hello'."
    assert second_char == "e", "The value of 'second_char' is incorrect. It should be 'e'."
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully assigned the string 'hello' to the variable 'test_string'."
    )

def check_step_2(
    ans: str,
) -> None:
    possible_answers = [0, 1, 2, 3, 4]
    try:
        ans = int(ans)
    except ValueError:
        print(
            "\033[91m\N{cross mark} Oops! "
            "The value of 'ans' is incorrect. It should be a number."
        )
        return

    assert ans in possible_answers, \
        "The value of your answer is not recognized. Please, make sure you are using the dropdown menu."
    if ans != 1:
        raise AssertionError(
            "Your answer is incorrect. Please, try running the code again."
        )
    else:
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "The index of 'e' in the string 'hello' is 1. Remember that Python starts counting from 0."
        )

def check_step_3(
    s: str,
) -> None:
    assert isinstance(s, str), \
        "The value of 's' is incorrect. It should be a string."
    expected_s = 'The quick brown fox jumps over the lazy dog'
    expected_s.replace("o", "*")
    assert s == expected_s, \
        ("The value of 's' is incorrect. It should be a string with the following content: "
         f"{expected_s}")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully changed the 'o' characters in the string 's'."
    )

def check_step_4(
    my_sentence: str,
    sentence_length: int,
) -> None:
    assert isinstance(my_sentence, str), \
        "The value of 'my_sentence' is incorrect. It should be a string."
    assert len(my_sentence) > 20, \
        ("The value of 'my_sentence' is incorrect. "
         "It should be a string with more than 20 characters.")
    assert isinstance(sentence_length, int), \
        ("The value of 'sentence_length' is incorrect. It should be an integer. "
         "Please, make sure you are using the form in this cell")
    assert sentence_length == len(my_sentence), \
        ("The value of 'sentence_length' is incorrect. It should be the length of the string 'my_sentence'. "
         "Please, make sure you are using the len() function.")
    print("\033[92m\N{heavy check mark} Well done! "
          "You have successfully calculated the length of the string 'my_sentence'.")
