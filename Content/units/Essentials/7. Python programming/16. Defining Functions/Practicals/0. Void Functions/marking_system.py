from typing import Callable
import io
from contextlib import redirect_stdout

def check_step_1(
    void_function: Callable,
) -> None:
    try:
        f = io.StringIO()
        with redirect_stdout(f):
            output = void_function()

    except Exception as e:
        raise Exception(
            "The marking system tried to run your function "
            "but something went wrong. Check the error message below. "
            "Please, try again.\n" + str(e)
        )
    assert output is None, \
        ("Your function is not a void function. "
         "It should not return anything. "
         "Please, try again.")

    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You created a void function."
    )