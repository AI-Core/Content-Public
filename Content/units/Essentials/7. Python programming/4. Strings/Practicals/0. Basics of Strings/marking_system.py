def check_step_1(
    my_string: str,
) -> None:
    assert isinstance(my_string, str), "The value of 'my_string' is incorrect. It should be a string."
    assert my_string == "Hello World", "The value of 'my_string' is incorrect. It should be 'Hello World'."
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully assigned the string 'Hello World' to the variable 'my_string'."
    )

def check_step_2(
    your_code: str,
) -> None:
    assert isinstance(your_code, str), \
        ("The value of 'your_code' is incorrect. It should be a string. "
         "Make sure you are using the form in the instructions")
    assert "print" in your_code, \
        "Your code should contain the 'print' function."
    assert "my_string" in your_code, \
        ("Your code should contain the variable 'my_string'. "
         "Please, try again.")
    print("\033[92m\N{heavy check mark} Well done! "
          "You have successfully printed the value of the variable 'my_string'.")

def check_step_3(
    your_code: str,
) -> None:
    assert isinstance(your_code, str), \
        ("The value of 'your_code' is incorrect. It should be a string. "
         "Make sure you are using the form in the instructions")
    assert "print" in your_code, \
        "Your code should contain the 'print' function."
    assert "my_string" in your_code, \
        ("Your code should contain the variable 'my_string'. "
         "Please, try again.")
    assert "type" in your_code, \
        ("Your code should contain the 'type' function. "
         "Please, try again.")
    print("\033[92m\N{heavy check mark} Well done! "
          "You have successfully printed the type of the variable 'my_string'.")

def check_step_4(
    my_string: str,
) -> None:
    assert isinstance(my_string, str), "The value of 'my_string' is incorrect. It should be a string."
    if (my_string == "Hello\nWorld") or \
       (my_string == "Hello \n World") or \
       (my_string == "Hello \nWorld") or \
       (my_string == "Hello\n World"):
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "You have successfully assigned the string 'Hello \\nWorld' to the variable 'my_string'."
        )

    else:
        print(
            "\033[91m\N{cross mark} Oops! "
            "You have not assigned the string 'Hello \\nWorld' to the variable 'my_string'."
        )

def check_step_5(
    my_string: str,
) -> None:
    assert isinstance(my_string, str), "The value of 'my_string' is incorrect. It should be a string."
    if (my_string == "Hello\tWorld") or \
       (my_string == "Hello \t World") or \
       (my_string == "Hello \tWorld") or \
       (my_string == "Hello\t World"):
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "You have successfully assigned the string 'Hello \\tWorld' to the variable 'my_string'."
        )

    else:
        print(
            "\033[91m\N{cross mark} Oops! "
            "You have not assigned the string 'Hello \\tWorld' to the variable 'my_string'."
        )