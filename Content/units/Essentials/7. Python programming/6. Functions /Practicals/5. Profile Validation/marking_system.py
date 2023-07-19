from typing import Callable, Optional

class ProfileError(Exception):
    def __init__(self, message=None):
        if message is None:
            message = "The function should return a message if the profile is invalid."
        super().__init__(message)

def check_step_1(
    validate_profile: Callable[[str, str, str], None]
) -> None:
    assert validate_profile.__code__.co_argcount == 3, \
        "'validate_profile' should take 3 arguments. Please, try again."
    assert "name" in validate_profile.__code__.co_varnames, \
        "'name' should be a parameter of 'validate_profile'. Please, try again."
    assert "age" in validate_profile.__code__.co_varnames, \
        "'age' should be a parameter of 'validate_profile'. Please, try again."
    assert "email" in validate_profile.__code__.co_varnames, \
        "'email' should be a parameter of 'validate_profile'. Please, try again."
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have defined the validate_profile function correctly"
    )
def check_step_2(
    validate_profile: Callable[[str, str, str], Optional[str]]
) -> None:
    try:
        name = "John"
        age = 20
        email = "john@hotmail.com"
        output_1 = validate_profile(name, age, email)

        if output_1 is not None:
            raise ProfileError(
                "The marking system tried to run your function "
                f"using the arguments {name}, {age}, and {email}, "
                "so it shouldn't return anything, but it returned "
                f"{output_1}. Please, try again."
            )

        name = "John!"
        age = 20
        email = "john@hotmail.com"
        expected_2 = "Invalid name"
        output_2 = validate_profile(name, age, email)

        if output_2 != expected_2:
            raise ProfileError(
                "The marking system tried to run your function "
                f"using the arguments {name}, {age}, and {email}, "
                f"so it should return {expected_2}, but it returned "
                f"{output_2}. Please, try again."
            )

    except ProfileError as e:
        raise ProfileError(e)

    except Exception as e:
        raise Exception(
            "The marking system tried to run your function "
            "but something went wrong. Check the error message below. "
            "Please, try again.\n" + str(e)
        )
    else:
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "Your function now checks if the name is valid"
        )


def check_step_3(
    validate_profile: Callable[[str, str, str], Optional[str]]
) -> None:
    try:
        name = "John"
        age = 20
        email = "john@hotmail.com"
        output_1 = validate_profile(name, age, email)

        if output_1 is not None:
            raise ProfileError(
                "The marking system tried to run your function "
                f"using the arguments {name}, {age}, and {email}, "
                "so it shouldn't return anything, but it returned "
                f"{output_1}. Please, try again."
            )

        name = "John"
        age = 20
        email = "johnathotmail.com"
        expected_2 = "Invalid email"
        output_2 = validate_profile(name, age, email)

        if output_2 != expected_2:
            raise ProfileError(
                "The marking system tried to run your function "
                f"using the arguments {name}, {age}, and {email}, "
                f"so it should return {expected_2}, but it returned "
                f"{output_2}. Please, try again."
            )

    except ProfileError as e:
        raise ProfileError(e)

    except Exception as e:
        raise Exception(
            "The marking system tried to run your function "
            "but something went wrong. Check the error message below. "
            "Please, try again.\n" + str(e)
        )
    else:
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "Your function now checks if the email is valid"
        )

def check_step_4(
    validate_profile: Callable[[str, str, str], Optional[str]]
) -> None:
    try:
        name = "John"
        age = 20
        email = "john@hotmail.com"
        output_1 = validate_profile(name, age, email)

        if output_1 is not None:
            raise ProfileError(
                "The marking system tried to run your function "
                f"using the arguments {name}, {age}, and {email}, "
                "so it shouldn't return anything, but it returned "
                f"{output_1}. Please, try again."
            )

        name = "John"
        age = 11
        email = "john@hotmail.com"
        expected_2 = "Invalid age"
        output_2 = validate_profile(name, age, email)

        if output_2 != expected_2:
            raise ProfileError(
                "The marking system tried to run your function "
                f"using the arguments {name}, {age}, and {email}, "
                f"so it should return {expected_2}, but it returned "
                f"{output_2}. Please, try again."
            )

    except ProfileError as e:
        raise ProfileError(e)

    except Exception as e:
        raise Exception(
            "The marking system tried to run your function "
            "but something went wrong. Check the error message below. "
            "Please, try again.\n" + str(e)
        )
    else:
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "Your function now checks if the age is valid"
        )

def check_step_5(
    check_name: Callable[[str], None],
    check_email: Callable[[str], None],
    check_age: Callable[[int], None],
    validate_profile: Callable[[str, str, str], None]
) -> None:
    try:
        name = "John"
        output_name_1 = check_name(name)
        if output_name_1 is not None:
            raise ProfileError(
                "The marking system tried to run your the check_name function "
                f"using the argument {name}, so it shouldn't return "
                f"anything, but it returned {output_name_1}. Please, try again."
            )
        name = "John!"
        expected_name_2 = "Invalid name"
        output_name_2 = check_name(name)
        if output_name_2 != expected_name_2:
            raise ProfileError(
                "The marking system tried to run your the check_name function "
                f"using the argument {name}, so it should return "
                f"{expected_name_2}, but it returned {output_name_2}. Please, try again."
            )

        email = "john@hotmail.com"
        output_email_1 = check_email(email)
        if output_email_1 is not None:
            raise ProfileError(
                "The marking system tried to run your the check_email function "
                f"using the argument {email}, so it shouldn't return "
                f"anything, but it returned {output_email_1}. Please, try again."
            )

        email = "johnathotmail.com"
        expected_email_2 = "Invalid email"
        output_email_2 = check_email(email)
        if output_email_2 != expected_email_2:
            raise ProfileError(
                "The marking system tried to run your the check_email function "
                f"using the argument {email}, so it should return "
                f"{expected_email_2}, but it returned {output_email_2}. Please, try again."
            )

        age = 20
        output_age_1 = check_age(age)
        if output_age_1 is not None:
            raise ProfileError(
                "The marking system tried to run your the check_age function "
                f"using the argument {age}, so it shouldn't return "
                f"anything, but it returned {output_age_1}. Please, try again."
            )

        age = 11
        expected_age_2 = "Invalid age"
        output_age_2 = check_age(age)
        if output_age_2 != expected_age_2:
            raise ProfileError(
                "The marking system tried to run your the check_age function "
                f"using the argument {age}, so it should return "
                f"{expected_age_2}, but it returned {output_age_2}. Please, try again."
            )

    except ProfileError as e:
        raise ProfileError(e)

    except Exception as e:
        raise Exception(
            "The marking system tried to run your function "
            "but something went wrong. Check the error message below. "
            "Please, try again.\n" + str(e)
        )

    else:
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "Your function now checks if the name, email, and age are valid"
        )
