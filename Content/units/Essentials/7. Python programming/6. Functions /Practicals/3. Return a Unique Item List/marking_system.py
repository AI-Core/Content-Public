from typing import Callable

class UniqueError(Exception):
    def __init__(self, message=None):
        if message is None:
            message = "The function should return a list with unique elements."
        super().__init__(message)

def check_step_1(
    unique_list: Callable[[list], list],
) -> None:
    try:
        my_list_1 = [1, 3, 5, 6, 4, 3, 2, 3, 3, 4, 3, 4, 5, 6, 6, 4, 3, 2, 12, 3, 5, 63, 4, 5, 3, 3, 2]
        output_1 = unique_list(my_list_1)
        expected_output_1 = [1, 3, 5, 6, 4, 2, 12, 63]
        if len(set(output_1)) != len(expected_output_1):
            raise UniqueError

        my_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        output_2 = unique_list(my_list_2)
        expected_output_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if len(set(output_2)) != len(expected_output_2):
            raise UniqueError

    except UniqueError as e:
        raise UniqueError(e)

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
