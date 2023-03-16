def check_step_1(
    fahrenheit: float,
) -> None:
    assert isinstance(fahrenheit, float), \
        ("The value of 'fahrenheit' is incorrect. It should be a float obtained from the input() function."
         "Please, make sure you casted it to a float.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have correctly obtained the user's temperature in Fahrenheit and stored it in the variable 'fahrenheit'. "
    )

def check_step_2(
    fahrenheit: float,
    celsius: float,
) -> None:
    given_celsius = (fahrenheit - 32) * 5 / 9
    assert isinstance(fahrenheit, float), \
        ("The value of 'fahrenheit' is incorrect. It should be a float obtained from the input() function."
         "Please, make sure you casted it to a float.")
    assert isinstance(celsius, float), \
        "The value of 'celsius' is incorrect. It should be a float obtained from the formula."
    assert celsius == given_celsius, \
        ("The value of 'celsius' is incorrect. "
         "It should be a float obtained from the formula: "
         "(fahrenheit - 32) * 5 / 9. "
         f"In your case, your value for 'farhenheit' retuns"
         f"{given_celsius} when using the formula, but your value for 'celsius' is {celsius}.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have correctly calculated the user's temperature in Celsius and stored it in the variable 'celsius'. "
    )


def check_step_3(
    age_as_int: int,
    ans_1: str,
) -> None:
    assert isinstance(age_as_int, int), \
        "The value of 'age_as_int' is incorrect. It should be an integer obtained from the input() function."
    assert isinstance(ans_1, str), \
        ("The value of your answer is incorrect. It should be a string. "
         "Please, make sure you are using the form in this cell")
    assert ans_1 == "int", \
        ("The value of your answer is incorrect. "
         "Unless you are not using the input() function, "
         "the type of the variable 'age_as_int' should be 'int'. ")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have correctly casted the user's age to an integer and stored it in the variable 'age_as_int'."
    )
