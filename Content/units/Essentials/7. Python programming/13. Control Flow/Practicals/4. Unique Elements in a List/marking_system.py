import os

def check_step_1(
    users_code: str,
) -> None:
    assert len(users_code) > 0, \
        ("Your code is empty. "
         "Please, try again.")
    assert "if" in users_code, \
        ("Your code does not contain an 'if' statement. "
         "Please, try again.")
    assert "set" in users_code, \
        ("Your code does not contain the 'set' function. "
         "You need to convert the list to a set to remove duplicates. "
         "Please, try again.")
    assert "len" in users_code, \
        ("Your code does not contain the 'len' function. "
         "You need to use it to check the length of the list and the set. "
         "Please, try again.")
    assert "==" in users_code, \
        ("Your code does not contain the '==' operator. "
         "You need to use it to compare the length of the list and the set. "
         "Please, try again.")
    assert "print" in users_code, \
        ("Your code does not contain a 'print' statement. "
         "You have to print the result of the check. "
         "Please, try again.")
    assert "All elements are unique" in users_code, \
        ("Your code does not print the case when all elements are unique. "
         "If it does, make sure you are printing 'All elements are unique'. "
         "Please, try again.")
    assert "There are duplicate elements" in users_code, \
        ("Your code does not print the case when there are duplicate elements. "
         "If it does, make sure you are printing 'There are duplicate elements'. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully checked if the list contains unique elements."
    )