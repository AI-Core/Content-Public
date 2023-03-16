def check_step_1(
    name: str,
    age: str,
    message: str,
) -> None:
    assert isinstance(name, str), \
        "The value of 'name' is incorrect. It should be a string."
    assert isinstance(age, str), \
        "The value of 'age' is incorrect. It should be a string obtained from the input() function."
    assert isinstance(message, str), \
        "The value of 'message' is incorrect. It should be a string."

    assert message == f"Hello, my name is {name} and I am {age} years old", \
        ("The value of 'message' is incorrect. "
         "It should be a string that contains the following message: "
         f"'Hello, my name is {name} and I am {age} years old'. "
         f"But your message is: {message}")

    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have correctly created the string 'message' "
        "that contains the name and age of the user."
    )