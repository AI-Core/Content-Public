from typing import Callable, Optional, Union

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

def check_step_2(validate_profile: Callable[[str, int, str], Optional[Union[str, bool]]]) -> None:
    try:
        name = "John"
        age = 20
        email = "john@hotmail.com"
        expected_1 = True
        output_1 = validate_profile(name, age, email)

        if output_1 != expected_1:
            raise ProfileError(
                "The marking system tried to run your function "
                f"using the arguments {name}, {age}, and {email}, "
                f"so it should return {expected_1}, but it returned "
                f"{output_1}. Please, try again."
            )

        name = "John!"
        expected_2 = "Invalid name"
        output_2 = validate_profile(name, age, email)

        if output_2 != expected_2:
            raise ProfileError(
                "The marking system tried to run your function "
                f"using the arguments {name}, {age}, and {email}, "
                f"so it should return {expected_2}, but it returned "
                f"{output_2}. Please, try again."
            )

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
    validate_profile: Callable[[str, int, str], Union[bool, str]]
) -> None:
    try:
        name = "John"
        age = 20
        email = "john@hotmail.com"
        expected_1 = True
        output_1 = validate_profile(name, age, email)

        if output_1 != expected_1:
            raise ProfileError(
                "The marking system tried to run your function "
                f"using the arguments {name}, {age}, and {email}, "
                f"so it should return {expected_1}, but it returned "
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


from typing import Callable, Optional, Union

def check_step_4(
    validate_profile: Callable[[str, int, str], Union[bool, str]]
) -> None:
    try:
        name = "John"
        age = 20
        email = "john@hotmail.com"
        expected_1 = True
        output_1 = validate_profile(name, age, email)

        if output_1 != expected_1:
            raise ProfileError(
                "The marking system tried to run your function "
                f"using the arguments {name}, {age}, and {email}, "
                f"so it should return {expected_1}, but it returned "
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
    check_name: Callable[[str], Union[bool, str]],
    check_email: Callable[[str], Union[bool, str]],
    check_age: Callable[[int], Union[bool, str]],
    validate_profile: Callable[[str, int, str], Union[bool, str]]
) -> None:
    try:
        # Check Name Validation
        name_invalid = "John!"
        name_valid = "John"
        assert check_name(name_valid) == True
        assert check_name(name_invalid) == "Invalid name"

        # Check Email Validation
        email_invalid = "johnathotmail.com"
        email_valid = "john@hotmail.com"
        assert check_email(email_valid) == True
        assert check_email(email_invalid) == "Invalid email"

        # Check Age Validation
        age_valid = 20
        age_invalid = 11
        assert check_age(age_valid) == True
        assert check_age(age_invalid) == "Invalid age"

        # Check Full Profile Validation
        assert validate_profile(name_valid, age_valid, email_valid) == "Profile created"
        assert validate_profile(name_invalid, age_valid, email_valid) == "Invalid name"
        assert validate_profile(name_valid, age_invalid, email_valid) == "Invalid age"
        assert validate_profile(name_valid, age_valid, email_invalid) == "Invalid email"

    except AssertionError:
        raise ProfileError(
            "The marking system found an inconsistency in your validation functions. Please, try again."
        )
    except ProfileError as e:
        raise ProfileError(e)
    except Exception as e:
        raise Exception(
            "The marking system tried to run your functions "
            "but something went wrong. Check the error message below. "
            "Please, try again.\n" + str(e)
        )
    else:
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "Your function now checks if the name, email, and age are valid"
        )
