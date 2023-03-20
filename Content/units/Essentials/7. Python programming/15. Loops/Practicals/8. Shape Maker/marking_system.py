import io
from contextlib import redirect_stdout
import timeout_decorator

@timeout_decorator.timeout(5, timeout_exception=TimeoutError)
def check_step_1(
    users_code: str,
) -> None:
    '''
    Asserts that the user's code contains a for loop, a range function,
    a print function and a * character to print the pattern.
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
    '''
    assert len(users_code) > 0, \
        ("Your code is empty. "
         "Please, try again.")
    assert "for" in users_code, \
        ("Your code does not contain a 'for' loop. "
         "Please, try again.")
    assert "range" in users_code, \
        ("Your code does not contain the 'range' function. "
         "You need to use it to create a range of numbers. "
         "Please, try again.")
    assert "print" in users_code, \
        ("Your code does not contain the 'print' function. "
         "You need it to print the pattern. "
         "Please, try again.")
    assert "*" in users_code, \
        ("Your code does not contain the '*' character. "
         "It is the character that you need to print to create the pattern. "
         "Please, try again.")
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
        raise Exception(
            "Your code is not working. "
            "Please, try again." + str(e)
        )
    
    output = output.strip()
    output = output.split("\n")
    assert len(output) > 8, \
        ("Your code is not printing the correct pattern. "
         "The number of lines should be at least 9 (one for each row)"
         "Please, try again.")
    assert len(output[0]) == 1, \
        ("Your code is not printing the correct pattern. "
         "The first line should contain one '*'. "
         "Please, try again.")
    assert len(output[1]) == 2, \
        ("Your code is not printing the correct pattern. "
         "The second line should contain two '*'. "
         "Please, try again.")
    assert len(output[4]) == 5, \
        ("Your code is not printing the correct pattern. "
         "The fifth line should contain five '*'. "
         "Please, try again.")
    assert len(output[5]) == 4, \
        ("Your code is not printing the correct pattern. "
         "The sixth line should contain four '*'. "
         "Please, try again.")
    
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully printed the pattern using for loops."
    )

def check_solution_2() -> None:
    print(
        "This problem was hard, so we have provided the solution for you. "
        "This is the code:\n"
        "for i in range(1, 8, 2):\n"
        "    print(' ' * ((7 - i) // 2) + '*' * i)\n"
        "for i in range(5, 0, -2):\n"
        "    print(' ' * ((7 - i) // 2) + '*' * i)\n"
        "Did you get the it right? "
    )