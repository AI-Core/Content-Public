from typing import Callable

class PalindromeError(Exception):
    def __init__(self, message=None):
        if message is None:
            message = "The function should return True if the word is a palindrome, and False otherwise."
        super().__init__(message)

def check_step_1(
    is_palindrome: Callable[[str], bool]
) -> None:
    try:
        word = "racecar"
        output_1 = is_palindrome(word)
        if not output_1:
            raise PalindromeError(
                "The marking system tried to run your function "
                f"using the argument {word}, so it should return True, "
                f"but it returned {output_1}. Please, try again."
            )

        word = "palindrome"
        output_2 = is_palindrome(word)
        if output_2:
            raise PalindromeError(
                "The marking system tried to run your function "
                f"using the argument {word}, so it should return False, "
                f"but it returned {output_2}. Please, try again."
            )

    except PalindromeError as e:
        raise PalindromeError(e)

    except Exception as e:
        raise Exception(
            "The marking system tried to run your function "
            "but something went wrong. Check the error message below. "
            "Please, try again.\n" + str(e)
        )

    else:
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "Your function now checks if the word is a palindrome"
        )

def check_step_2(
    is_palindrome: Callable[[str], bool]
) -> None:
    try:
        word = "racecar"
        output_1 = is_palindrome(word)
        if not output_1:
            raise PalindromeError(
                "The marking system tried to run your function "
                f"using the argument {word}, so it should return True, "
                f"but it returned {output_1}. Please, try again."
            )

        word = "RaCeCar"
        output_2 = is_palindrome(word)
        if not output_2:
            raise PalindromeError(
                "The marking system tried to run your function "
                f"using the argument {word}, so it should return True, "
                f"but it returned {output_2}. Please, try again and remember "
                "that the function should be case-insensitive."
            )

        word = ".Rac!Ec,ar"
        output_3 = is_palindrome(word)
        if not output_3:
            raise PalindromeError(
                "The marking system tried to run your function "
                f"using the argument {word}, so it should return True, "
                f"but it returned {output_3}. Please, try again and remember "
                "that the function should ignore punctuation."
            )

    except PalindromeError as e:
        raise PalindromeError(e)

    except Exception as e:
        raise Exception(
            "The marking system tried to run your function "
            "but something went wrong. Check the error message below. "
            "Please, try again.\n" + str(e)
        )

    else:
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "Your function now ignores case and punctuation"
        )
