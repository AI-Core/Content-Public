import os

def check_step_1() -> None:
    file_to_read = 'order_conditions.py'
    assert file_to_read in os.listdir(), \
        ("You haven't downloaded the file. "
         "Please, run the first cell to download it")
    with open(file_to_read, 'r') as f:
        users_code = f.read()
    assert len(users_code) > 0, \
        ("Your code is empty. "
         "Please, try again.")
    assert "if x > 0:" not in users_code, \
        ("Your code contains the condition 'if x > 0', "
         "which is not correct. Bear in mind that "
         "any number greater than 0 will trigger this condition. "
         "Please, try again.")
    assert "if x > 15:" not in users_code, \
        ("Your code contains the condition 'if x > 15', "
         "which is not correct. If x is greater than 20, "
         "it is also greater than 15, so the condition "
         "'x > 20' will not be triggered because this condition "
         "is checked first. "
         "Please, try again.")
    assert "if x > 20:" in users_code, \
        ("Your code does not contain the condition 'if x > 20'. "
         "This condition should be checked first. "
         "If, for some reason, you are using different numbers to be "
         "compared, please, use the numbers 20, 15 and 0. ")
    assert "else:" in users_code, \
        ("Your code does not contain the 'else' statement. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully ordered the conditions. "
        "Now, the conditions will be checked in the correct order."
    )