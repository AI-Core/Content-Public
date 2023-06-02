def check_step_1(
    users_code: str,
) -> None:
    assert len(users_code) > 0, \
        ("Your code is empty. "
         "Please, try again.")
    assert "if" in users_code, \
        ("Your code does not contain an 'if' statement. "
         "Please, try again.")
    assert "==" in users_code, \
        ("Your code does not contain an '==' operator. "
         "It will be needed to compare the first letters of the strings. "
         "Please, try again.")
    assert "print" in users_code, \
        ("Your code does not contain a 'print' statement. "
         "You have to print the result of the comparison. "
         "Please, try again.")
    assert "else" in users_code, \
        ("Your code does not contain an 'else' statement. "
         "Please, try again.")
    assert "The first letters are the same" in users_code, \
        ("Your code does not print the correct message when the first letters are the same. "
         "It should print 'The first letters are the same'. "
         "Please, try again.")
    assert "The first letters are different" in users_code, \
        ("Your code does not print the correct message when the first letters are different. "
         "It should print 'The first letters are different'. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully compared the first letters of the strings "
        "using the 'if' statement."
    )
