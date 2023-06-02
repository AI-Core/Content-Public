def check_step_1(
    height: float,
    weight: float,
    bmi: float,
) -> None:
    assert height > 0, \
        ("Your height is not positive. "
         "Please, try again.")
    assert weight > 0, \
        ("Your weight is not positive. "
         "Please, try again.")
    assert bmi > 0, \
        ("Your BMI is not positive. "
         "Please, try again.")
    expected_bmi = weight / (height ** 2)
    assert abs(bmi - expected_bmi) < 0.01, \
        ("Your BMI is not correct. "
         f"It should be {expected_bmi:.2f}, "
         f"but your code calculated {bmi:.2f}. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully calculated the BMI."
    )

def check_step_2(
    users_code: str,
) -> None:
    assert len(users_code) > 0, \
        ("Your code is empty. "
         "Please, try again.")
    assert "if" in users_code, \
        ("Your code does not contain an 'if' statement. "
         "Please, try again.")
    assert "<" in users_code, \
        ("Your code does not contain an '<' operator. "
         "It will be needed to compare the BMI with the ranges. "
         "Please, try again.")
    assert "elif" in users_code, \
        ("Your code does not contain an 'elif' statement. "
         "The bmi should be compared with multiple ranges, "
         "so you need to use the 'elif' statement. "
         "Please, try again.")
    assert "print" in users_code, \
        ("Your code does not contain a 'print' statement. "
         "You have to print the range the BMI belongs to. "
         "Please, try again.")
    assert "else" in users_code, \
        ("Your code does not contain an 'else' statement. "
         "Please, try again.")
    assert "Your BMI is" in users_code, \
        ("Your code does not print the BMI. "
         "Please, try again.")
    assert "You're in the underweight range" in users_code, \
        ("Your code does not print the case when the BMI is in the underweight range. "
         "Please, try again.")
    assert "You're in the healthy weight range" in users_code, \
        ("Your code does not print the case when the BMI is in the healthy weight range. "
         "Please, try again.")
    assert "You're in the overweight range" in users_code, \
        ("Your code does not print the case when the BMI is in the overweight range. "
         "Please, try again.")
    assert "You're in the obese range" in users_code, \
        ("Your code does not print the case when the BMI is in the obese range. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully printed the range the BMI belongs to."
    )
