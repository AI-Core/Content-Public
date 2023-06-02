import os
import timeout_decorator
import io
from contextlib import redirect_stdout

@timeout_decorator.timeout(5, timeout_exception=TimeoutError)
def check_step_1(
    users_code: str,
) -> None:
    n_1_possibilities = [
        "n= 1",
        "n =1",
        "n=1",
    ]
    n_1_increment_possibilities = [
        "n=n+1",
        "n = n+1",
        "n = n +1",
        "n=n +1",
        "n+=1",
        "n +=1",
    ]
    assert len(users_code) > 0, \
        ("Your code is empty. "
         "Please, try again.")
    assert "while" in users_code, \
        ("You did not use a while loop. "
         "Please, try again.")
    for line in users_code.split("\n"):
        if any([n_1 in line for n_1 in n_1_possibilities]):
            print(
                "Great, you are assigning 1 to n, "
                "but the coding style is not correct. "
                "It should look like this: "
                '"n = 1" (Note the spaces).'
            )
            break
    for line in users_code.split("\n"):
        if any([n_1_increment in line for n_1_increment in n_1_increment_possibilities]):
            print(
                "Great, you are incrementing the value of n, "
                "but the coding style is not correct. "
                "It should look like this: "
                '"n = n + 1", or "n += 1" (Note the spaces).'
            )
            break
    assert "print" in users_code, \
        ("You did not use the print function. "
         "You should print the value of n in each iteration. "
         "Please, try again.")
    # Execute the code and store the output in a file
    try:
        f = io.StringIO()
        with redirect_stdout(f):
            exec(users_code)
        output = f.getvalue()
    except TimeoutError:
        raise TimeoutError(
            "Your code is taking too long to run. "
            "Please, try again."
        )
    except Exception as e:
        raise AssertionError(
            "Your code is not working. "
            f"Please, try again. Error: {e}"
        )
    assert '51' not in output, \
        ("You are printing 51 when running the code. "
         "The code should print the numbers from 1 to 50. "
         "Please, try again.")
    assert output.splitlines()[0] == '1', \
        ("The first number you have to print is 1. "
         f"Your code is printing {output.splitlines()[0]} instead. "
         "Please, try again.")
    assert '1' in output and '50' in output, \
        ("You are not printing the numbers from 1 to 50. "
         "The marking system is looking for the numbers 1 and 50 in the output. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully printed the numbers from 1 to 50 using a while loop. "
    )

@timeout_decorator.timeout(5, timeout_exception=TimeoutError)
def check_step_2(
    users_code: str,
) -> None:
    assert len(users_code) > 0, \
        ("Your code is empty. "
         "Please, try again.")
    assert "for" in users_code, \
        ("You did not use a for loop. "
         "Please, try again.")
    assert "range" in users_code, \
        ("You did not use the range function. "
         "Please, try again.")
    assert "51" in users_code, \
        ("You did not use the range function correctly. "
         "The range function should start at 1 and end at 50. "
         "So, the second argument should be 51. "
         "If you defined the right range, make sure you are using "
         "the correct coding style: range(1, 51). "
         "Please, try again.")
    assert "print" in users_code, \
        ("You did not use the print function. "
         "You should print the value of n in each iteration. "
         "Please, try again.")
    # Execute the code and store the output in a file
    try:
        f = io.StringIO()
        with redirect_stdout(f):
            exec(users_code)
        output = f.getvalue()
        lines = output.splitlines()
    except TimeoutError:
        raise TimeoutError(
            "Your code is taking too long to run. "
            "Please, try again."
        )
    except Exception as e:
        raise AssertionError(
            "Your code is not working. "
            f"Please, try again. Error: {e}"
        )
    assert '51' not in lines, \
        ("You are printing 51 when running the code. "
         "The code should print the numbers from 1 to 50. "
         "Please, try again.")
    assert '0' not in lines, \
        ("You are printing 0 when running the code. "
         "The code should print the numbers from 1 to 50. "
         "Please, try again.")
    assert '1' in lines and '50' in lines, \
        ("You are not printing the numbers from 1 to 50. "
         "The marking system is looking for the numbers 1 and 50 in the output. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully printed the numbers from 1 to 50 using a for loop. "
    )
