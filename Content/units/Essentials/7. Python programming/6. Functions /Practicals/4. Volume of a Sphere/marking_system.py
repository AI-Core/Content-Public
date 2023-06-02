from typing import Callable

class SphereError(Exception):
    def __init__(self, message=None):
        if message is None:
            message = "The function should return the volume of a sphere."
        super().__init__(message)

def check_step_1(
    volume_of_sphere: Callable[[float], float],
) -> None:
    try:
        radius = 5
        output_1 = volume_of_sphere(radius)
        expected_1 = 3.14 * 4 / 3 * radius ** 3
        if not isinstance(output_1, float):
            raise SphereError(
                "The marking system tried to run your function "
                f"using the argument {radius}, so it should return "
                "a float value, but it returned a value of type "
                f"{type(output_1)}. Please, try again."
            )
        if abs(output_1 - expected_1) > 1:
            raise SphereError(
                "The marking system tried to run your function "
                f"using the argument {radius}, so it should return "
                f"{expected_1}, but it returned {output_1}. Please, try again."
            )
    except SphereError as e:
        raise SphereError(e)

    except Exception as e:
        raise Exception(
            "The marking system tried to run your function "
            "but something went wrong. Check the error message below. "
            "Please, try again.\n" + str(e)
        )
    else:
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "You created a function that returns the volume of a sphere."
        )
