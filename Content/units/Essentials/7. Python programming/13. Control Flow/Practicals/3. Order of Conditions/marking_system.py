import timeout_decorator
import io
from contextlib import redirect_stdout
import os
from unittest.mock import patch

class ConditionsError(Exception):
    def __init__(self, message=None):
        if message is None:
            message = "The output is not correct."
        super().__init__(message)


@timeout_decorator.timeout(5, timeout_exception=TimeoutError)
def check_step_1(
    users_code: str,
) -> None:

    assert len(users_code) > 0, \
        ("Your code is empty. "
         "Please, try again.")
    assert "x = int(input('Enter a number: '))" in users_code, \
        ("Your code does not contain the line 'x = int(input('Enter a number: '))'. "
         "Please, don't delete the code above the line that says '# Add your code below this line'."
         "Please, try again.")
    try:
        f = io.StringIO()
        with redirect_stdout(f):
            with patch('builtins.input', side_effect=['25']):
                exec(users_code)
        output_1 = f.getvalue()
        if 'greater than 20' not in output_1:
            raise ConditionsError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the input '25'. "
                "The output should be 'x is greater than 20', but your code printed: \n"
                f"{output_1}\n"
                "Please, try again.")
        f = io.StringIO()
        with redirect_stdout(f):
            with patch('builtins.input', side_effect=['16']):
                exec(users_code)
        output_1 = f.getvalue()
        if 'greater than 15' not in output_1:
            raise ConditionsError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the input '16'. "
                "The output should be 'x is greater than 15', but your code printed: \n"
                f"{output_1}"
                "Please, try again.")
        f = io.StringIO()
        with redirect_stdout(f):
            with patch('builtins.input', side_effect=['15']):
                exec(users_code)
        output_1 = f.getvalue()
        if 'greater than 0' not in output_1:
            raise ConditionsError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the input '15'. "
                "The output should be 'x is greater than 10', but your code printed: \n"
                f"{output_1}"
                "Remember that you have to check if x is greater than 15, not greater or equal to 15. "
                "Please, try again.")
        f = io.StringIO()
        with redirect_stdout(f):
            with patch('builtins.input', side_effect=['9']):
                exec(users_code)
        output_1 = f.getvalue()
        if 'greater than 0' not in output_1:
            raise ConditionsError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the input '9'. "
                "The output should be 'x is greater than 0', but your code printed: \n"
                f"{output_1}"
                "Please, try again.")
        f = io.StringIO()
        with redirect_stdout(f):
            with patch('builtins.input', side_effect=['-1']):
                exec(users_code)
        output_1 = f.getvalue()
        if 'less than 0' not in output_1:
            raise ConditionsError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the input '-1'. "
                "The output should be 'x is less than 0', but your code printed: \n"
                f"{output_1}"
                "Please, try again.")
    except TimeoutError:
        raise TimeoutError(
            "Your code is taking too long to run. "
            "Make sure you are using only one input function "
            "and that you haven't used any loops. "
            "Please, try again.")
    except StopIteration as e:
        raise TimeoutError(
            "Your code is taking too long to run. "
            "Make sure you are using only one input function "
            "and that you haven't used any loops. "
            "Please, try again.")
    except ConditionsError as e:
        raise ConditionsError(e) from e
    except Exception as e:
        raise Exception(
            "You code is not working. "
            "Make sure you can run it without any errors. "
            "Please, try again.") from e
    else:
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "You successfully ordered the conditions. "
            "Now, the conditions will be checked in the correct order."
        )
