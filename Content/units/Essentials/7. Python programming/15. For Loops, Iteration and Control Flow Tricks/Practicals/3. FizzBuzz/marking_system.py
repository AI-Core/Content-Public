import timeout_decorator
import io
from contextlib import redirect_stdout

class FizzBuzzError(Exception):
    def __init__(self, message=None):
        if message is None:
            message = "The number is not in the range."
        super().__init__(message)


@timeout_decorator.timeout(5, timeout_exception=TimeoutError)
def check_step_1(
    users_code: str,
) -> None:
    assert "for" in users_code, \
        ("You should use a for loop with the range function to loop through the numbers from 1 to 100. "
         "Please, try again.")
    assert "if" in users_code, \
        ("You should use an if statement to check if the number is divisible by 3 and 5. "
         "Please, try again.")
    assert "print" in users_code, \
        ("You should use the print function to print 'Fizz', 'Buzz', 'FizzBuzz' or the number. "
         "Please, try again.")
    try:
        f = io.StringIO()
        with redirect_stdout(f):
            exec(users_code)
        output = f.getvalue()
        if output.splitlines()[0] != "1":
            raise FizzBuzzError("The first number your code should print is 1. Please, try again.")
        if output.splitlines()[-1] != "Buzz":
            raise FizzBuzzError("The last string your code should print is 'Buzz'. Please, try again.")
        output = output.strip()
        line = output.split('\n')
        if line[0] != '1':
            raise FizzBuzzError("The first number your code should print is 1. Please, try again.")
        if line[1] != '2':
            raise FizzBuzzError("The second number your code should print is 2. Please, try again.")
        if line[2] != 'Fizz':
            raise FizzBuzzError("The third number your code should print is 'Fizz'. Please, try again.")
        if line[3] != '4':
            raise FizzBuzzError("The fourth number your code should print is 4. Please, try again.")
        if line[4] != 'Buzz':
            raise FizzBuzzError("The fifth number your code should print is 'Buzz'. Please, try again.")
        if line[5] != 'Fizz':
            raise FizzBuzzError("The sixth number your code should print is 'Fizz'. Please, try again.")
        if line[14] != 'FizzBuzz':
            raise FizzBuzzError("The fifteenth number your code should print is 'FizzBuzz'. Please, try again.")
        if line[29] != 'FizzBuzz':
            raise FizzBuzzError("The thirtieth number your code should print is 'FizzBuzz'. Please, try again.")
        if line[99] != 'Buzz':
            raise FizzBuzzError("The hundredth number your code should print is 'Buzz'. Please, try again.")

    except FizzBuzzError as e:
        raise FizzBuzzError(e) from e

    except TimeoutError:
        raise TimeoutError("Your code is taking too long to run. "
                           "Make sure that you are using a for loop with the "
                           "range function to loop through the numbers from 1 to 100. "
                           "Please, try again.")
    except Exception as e:
        raise Exception("Your code is not working. "
                        "Before testing it, make sure you can run it without any errors. "
                        "Please, try again.") from e
    else:
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "You successfully completed the FizzBuzz challenge"
        )
