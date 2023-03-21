import os
from unittest.mock import patch
import timeout_decorator
import io
from contextlib import redirect_stdout

class NameAssertionError(Exception):
    def __init__(self, message=None):
        if message is None:
            message = "The output is not correct."
        super().__init__(message)

@timeout_decorator.timeout(5, timeout_exception=TimeoutError)
def check_step_1(
    users_code: str,
) -> None:
    assert len(users_code) > 0, (
        "Your code is empty. "
        "Please, try again."
    )
    assert 'name = input("Please, enter your name: ")' in users_code, (
        "Your code does not contain the line 'name = input(\"Please, enter your name: \")'. "
        "Please, don't delete the code above the line that says '# Add your code below this line'."
        "Please, try again."
    )
    assert "assert" in users_code, (
        "Your code does not contain the assert statement. "
        "You need to assert that the name is John. "
        "Please, try again."
    )
    try:
        # Run the file using two inputs
        f = io.StringIO()
        with redirect_stdout(f):
            with patch('builtins.input', side_effect=['John']):
                exec(users_code)
        output_1 = f.getvalue()
        if 'Hello, John' not in output_1:
            raise NameAssertionError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the input 'John'. "
                "The output should be 'Hello, John', but your code printed: \n"
                f"{output_1}"
                "Please, try again.")
        f = io.StringIO()
        with redirect_stdout(f):
            with patch('builtins.input', side_effect=['Jane']):
                exec(users_code)
        output_1 = f.getvalue()
    except StopIteration as e:
        raise TimeoutError(
            "Your code is taking too long to run. "
            "Make sure you are using only one input function "
            "and that you haven't used any loops. "
            "Please, try again.")
    except TimeoutError:
        raise TimeoutError(
            "Your code is taking too long to run. "
            "Have you added another input() function? "
            "If so, please remove it and try again. "
            "If not, make sure there are no loops in your code (e.g. while, for)."
        )
    except NameAssertionError as e:
        raise NameAssertionError(e)
    except AssertionError as e:
        e_message = str(e)
        if len(e_message) == 0 or "not John" not in e_message:
            raise NameAssertionError(
                "Your code does not contain the assert statement. "
                "If the user's name is John, the code should print 'Hello, John'. "
                "If it's not, it should print 'You are not John'. "
                "The marking system tried to run your code with the input 'Jane'. "
                "And the assertion error was: \n"
                f"{e}\n"
                "Please, try again.")
        else:
            print(
                "\033[92m\N{heavy check mark} Well done! "
                "You successfully created a simple assertion that checks "
                "if the user's name is John."
            )
    except Exception as e:
        raise NameAssertionError(
            "Your code is not working. "
            "The marking system tried to run your code with the input 'Jane'. "
            "And the error was: \n"
            f"{e}"
            "Please, try again.")

    else:
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "You successfully created a simple assertion that checks "
            "if the user's name is John."
        )
