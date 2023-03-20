import io
from contextlib import redirect_stdout
import timeout_decorator

@timeout_decorator.timeout(10, timeout_exception=TimeoutError)
def check_step_1(
    users_code: str,
) -> None:
    '''
    Asserts that the user is checking whether a number is prime
    from 10 to 300
    '''
    prime_numbers_to_check = [13, 17, 293]
    assert len(users_code) > 0, \
        ("Your code is empty. "
         "Please, try again.")
    assert "for" in users_code, \
        ("Your code does not contain a 'for' loop. "
         "Please, try again.")
    assert "range" in users_code, \
        ("Your code does not contain the 'range' function. "
         "Please, try again.")
    assert "print" in users_code, \
        ("Your code does not contain the 'print' function. "
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

    for number in prime_numbers_to_check:
        assert f"{number} is a prime number" in output, \
            ("Your code is not printing the correct output. "
             "The marking system was looking for a line that contains "
             f"'{number} is a prime number' but it did not find it. "
             "Please, check your code and the grammar and try again.")

    assert "299 is not a prime number because it is divisible by 13" in output, \
        ("Your code is not printing the correct output. "
         "The marking system was looking for a line that contains "
         "'299 is not a primer number because it is divisible by 13' "
         "but it did not find it. "
         "Please, check your code and the grammar and try again.")

    assert "143 is not a prime number because it is divisible by 11" in output, \
        ("Your code is not printing the correct output. "
         "The marking system was looking for a line that contains "
         "'143 is not a prime number because it is divisible by 11' "
         "but it did not find it. "
         "Please, check your code and the grammar and try again.")

    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully checked whether all the numbers between 10 and 300 "
        "are prime numbers. This wasn't an easy task!"
    )
