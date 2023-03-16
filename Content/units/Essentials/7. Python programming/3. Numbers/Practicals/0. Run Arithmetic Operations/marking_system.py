def check_step_1(
    a: int,
    b: int,
) -> None:
    assert isinstance(a, int), "The value of 'a' is incorrect. It should be an integer."
    assert isinstance(b, int), "The value of 'b' is incorrect. It should be an integer."
    assert a == 5, "The value of 'a' is incorrect. It should be 5."
    assert b == 2, "The value of 'b' is incorrect. It should be 2."
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully assigned values to the variables 'a' and 'b'."
    )

def check_step_2(
    your_code: str,
) -> None:
    assert isinstance(your_code, str), \
        ("The value of 'your_code' is incorrect. It should be a string. "
         "Make sure you are using the form in the instructions")
    assert "print" in your_code, \
        "Your code should contain the 'print' function."
    if ("a+b" in your_code) or ("a +b" in your_code) or ("a+ b" in your_code):
        print("Good job, "
              "you have successfully added the values of 'a' and 'b'. "
              "However, the coding style is incorrect. You should add spaces around the '+' sign.")
    elif ("a + b" in your_code):
        print("\033[92m\N{heavy check mark} Well done! "
              "you have successfully added the values of 'a' and 'b'.")

def check_step_3(
    your_code: str,
) -> None:
    assert isinstance(your_code, str), \
        ("The value of 'your_code' is incorrect. It should be a string. "
         "Make sure you are using the form in the instructions")
    assert "print" in your_code, \
        "Your code should contain the 'print' function."
    if ("a-b" in your_code) or ("a -b" in your_code) or ("a- b" in your_code):
        print("Good job, "
              "you have successfully substracted the values of 'a' and 'b'. "
              "However, the coding style is incorrect. You should add spaces around the '-' sign.")
    elif ("a - b" in your_code):
        print("\033[92m\N{heavy check mark} Well done! "
              "you have successfully substracted the values of 'a' and 'b'.")

def check_step_4(
    your_code: str,
) -> None:
    assert isinstance(your_code, str), \
        ("The value of 'your_code' is incorrect. It should be a string. "
         "Make sure you are using the form in the instructions")
    assert "print" in your_code, \
        "Your code should contain the 'print' function."
    if ("a*b" in your_code) or ("a *b" in your_code) or ("a* b" in your_code):
        print("Good job, you have successfully multiplied the values of 'a' and 'b'. "
              "However, the coding style is incorrect. You should add spaces around the '*' sign.")
    elif ("a * b" in your_code):
        print("\033[92m\N{heavy check mark} Well done! "
              "you have successfully multiplied the values of 'a' and 'b'.")

def check_step_5(
    your_code: str,
) -> None:
    assert isinstance(your_code, str), \
        ("The value of 'your_code' is incorrect. It should be a string. "
         "Make sure you are using the form in the instructions")
    assert "print" in your_code, \
        "Your code should contain the 'print' function."
    if ("a/b" in your_code) or ("a /b" in your_code) or ("a/ b" in your_code):
        print("Good job, you have successfully divided the values of 'a' and 'b'. "
              "However, the coding style is incorrect. You should add spaces around the '/' sign.")
    elif ("a / b" in your_code):
        print("\033[92m\N{heavy check mark} Well done! "
              "you have successfully divided the values of 'a' and 'b'.")

