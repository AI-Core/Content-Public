import os
from unittest.mock import patch
import timeout_decorator

@timeout_decorator.timeout(5, timeout_exception=TimeoutError)
def check_step_1() -> None:
    file_to_run = 'assertions.py'
    assert file_to_run in os.listdir(), (
        "You haven't created the file 'assertions.py'. "
        "Please, create it and try again."
    )
    with open(file_to_run, 'r') as f:
        users_code = f.read()

    assert len(users_code) > 0, (
        "Your code is empty. "
        "Please, try again."
    )
    assert "input" in users_code, (
        "Your code does not contain the input() function. "
        "You need to ask the user for a name. "
        "Please, try again."
    )
    assert "assert" in users_code, (
        "Your code does not contain the assert statement. "
        "You need to assert that the name is John. "
        "Please, try again."
    )
    try:
        # Run the file using two inputs
        with patch('builtins.input', side_effect=['John']):
            os.system(f'python {file_to_run} > output.txt')
        with open('output.txt', 'r') as f:
            output = f.read()
        assert 'Hello, John' in output, (
            "Your code does not print the correct output. "
            "When the user inputs 'John', the output should be 'Hello, John!', "
            "but your code printed: "
            f"{output}"
        )
        with patch('builtins.input', side_effect=['Jane']):
            os.system(f'python {file_to_run} 2> output.txt')
        with open('output.txt', 'r') as f:
            output = f.read()
        assert 'You are not John' in output, (
            "Your code does not print the correct output. "
            "When the user enters a name other than 'John', the output should be "
            "'You are not John', but your code printed: "
            f"{output}"
        )

    except TimeoutError:
        assert False, (
            "Your code is taking too long to run. "
            "Have you added another input() function? "
            "If so, please remove it and try again. "
            "If not, make sure there are no loops in your code (e.g. while, for)."
        )

    else:
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "You successfully created a simple assertion that checks "
            "if the user's name is John."
        )

    finally:
        if "output.txt" in os.listdir():
            os.remove('output.txt')
