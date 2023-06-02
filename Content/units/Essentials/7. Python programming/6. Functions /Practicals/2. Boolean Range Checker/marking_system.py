from typing import Callable
import io
from contextlib import redirect_stdout

class RangeError(Exception):
    def __init__(self, message=None):
        if message is None:
            message = "The number is not in the range."
        super().__init__(message)

def check_step_1(
    in_range: Callable[[int, int, int], bool],
) -> None:
    try:
        kwargs = {
            "lower_bound": 1,
            "upper_bound": 10,
            "number": 5,
        }
        output_1 = in_range(**kwargs)
        if not isinstance(output_1, bool):
            raise RangeError(
                "The marking system tried to run your function "
                f"using the arguments {kwargs}, so it should return "
                "a boolean value, but it returned a value of type "
                f"{type(output_1)}. Please, try again."
            )
        if output_1 is False:
            raise RangeError(
                "The marking system tried to run your function "
                f"using the arguments {kwargs}, so it should return "
                "True, but it returned False. Please, try again."
            )
        
        kwargs = {
            "lower_bound": 5,
            "upper_bound": 10,
            "number": 1,
        }
        output_2 = in_range(**kwargs)
        if not isinstance(output_2, bool):
            raise RangeError(
                "The marking system tried to run your function "
                f"using the arguments {kwargs}, so it should return "
                "a boolean value, but it returned a value of type "
                f"{type(output_2)}. Please, try again."
            )
        if output_2 is True:
            raise RangeError(
                "The marking system tried to run your function "
                f"using the arguments {kwargs}, so it should return "
                "False, but it returned True. Please, try again."
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
