from typing import Callable
import io
from contextlib import redirect_stdout

class RangeError(Exception):
    def __init__(self, message=None):
        if message is None:
            message = "The number is not in the range."
        super().__init__(message)

def check_step_1(
    in_range: Callable[[int, int, int], None],
) -> None:
    try:
        f = io.StringIO()
        with redirect_stdout(f):
            kwargs = {
                "lower_bound": 1,
                "upper_bound": 10,
                "number": 5,
            }
            in_range(**kwargs)
        output_1 = f.getvalue()
        expected_1 = "5 is between 1 and 10"
        if expected_1 not in output_1:
            raise RangeError(
                "The marking system tried to run your function "
                f"using the arguments {kwargs}, so it should print "
                f"'{expected_1}', but it printed '{output_1}'. "
                "Make sure that your function accepts the arguments "
                "lower_bound, upper_bound, and number."
            )

        f = io.StringIO()
        with redirect_stdout(f):
            kwargs = {
                "lower_bound": 5,
                "upper_bound": 10,
                "number": 1,
            }
            in_range(**kwargs)
        output_2 = f.getvalue()
        expected_2 = "1 is NOT between 5 and 10"
        if expected_2 not in output_2:
            raise RangeError(
                "The marking system tried to run your function "
                f"using the arguments {kwargs}, so it should print "
                f"'{expected_2}', but it printed '{output_2}'. "
                "Make sure that your function accepts the arguments "
                "lower_bound, upper_bound, and number."
            )
    except RangeError as e:
        raise RangeError(e)
    except Exception as e:
        raise Exception(
            "The marking system tried to run your function "
            "but something went wrong. Check the error message below. "
            "Please, try again.\n" + str(e)
        )
    else:
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "You successfully created a function that checks "
            "whether a number is in a given range."
        )
