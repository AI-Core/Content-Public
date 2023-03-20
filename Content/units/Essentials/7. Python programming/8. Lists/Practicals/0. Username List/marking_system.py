def check_step_1(
    usernames_type: str,
) -> None:
    assert isinstance(usernames_type, str), \
        ("The value of 'usernames_type' is incorrect. "
         "Please, make sure you are using the form in this cell")

    assert usernames_type == "list", \
        ("Your answer is incorrect. "
         "Please, try again.")

    print(
        "\033[92m\N{heavy check mark} Well done! "
        "The variable 'usernames' is a list."
    )

def check_step_2(
    usernames: list,
    usernames_len: int,
) -> None:
    assert isinstance(usernames, list), \
        ("The value of 'usernames' is incorrect. "
         "Please, run the cell in step 1 again to create the variable 'usernames'.")
    assert isinstance(usernames_len, int), \
        ("The value of 'usernames_len' is incorrect. "
         "Please, make sure you are using the form in this cell")

    assert usernames_len == len(usernames), \
        ("Your answer is incorrect. "
         f"The length of your 'usernames' list should be {len(usernames)}")

    print(
        "\033[92m\N{heavy check mark} Well done! "
        "The length of the list 'usernames' is correct."
    )

def check_step_3(
    username_type: str,
) -> None:
    assert isinstance(username_type, str), \
        ("The value of 'usernames_type' is incorrect. "
         "Please, make sure you are using the form in this cell")

    assert username_type == "str", \
        ("Your answer is incorrect. "
         "Please, try again.")

    print(
        "\033[92m\N{heavy check mark} Well done! "
        "The variable 'username' is a string. In this case, you have a list "
        "of strings, but lists can contain any type of data."
    )

def check_step_4(
    usernames: list,
    usernames_2: list,
    user_example: str,
) -> None:
    '''
    Checks that usernames_2 is a copy of the last five elements of usernames

    Then, it will assert that user_example is the second element of usernames_2
    '''
    assert isinstance(usernames, list), \
        ("The value of 'usernames' is incorrect. "
         "Please, run the cell in step 1 again to create the variable 'usernames'.")
    assert isinstance(usernames_2, list), \
        ("The value of 'usernames_2' is incorrect. "
         "Please, run the cell above again to create the variable 'usernames_2'.")
    assert isinstance(user_example, str), \
        ("The type of 'user_example' is incorrect, it should be a string. "
         "Please, make sure you created it using the `pop` method on 'usernames_2'.")

    usernames_2_expected = usernames.copy()[-5:]
    user_example_expected = usernames_2_expected.pop(1)
    
    assert usernames_2_expected == usernames_2, \
        ("The value of 'usernames_2' is incorrect. "
         "Please, run the cell above again to create the variable 'usernames_2'. "
         "Its value should be a copy of the last five elements of 'usernames'.")

    assert user_example == user_example_expected, \
        ("The value of 'user_example' is incorrect. "
         "Please, make sure you created it using the `pop` method on 'usernames_2'.")
    
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully popped the second element of 'usernames_2' and "
        "stored it in the variable 'user_example'."
    )
    

def check_step_5(
    usernames: list,
) -> None:
    '''
    Checks that usernames is a sorted list
    '''
    assert isinstance(usernames, list), \
        ("The value of 'usernames' is incorrect. "
         "Please, run the cell in step 1 again to create the variable 'usernames'.")

    assert usernames == sorted(usernames), \
        ("The value of 'usernames' is incorrect. "
         "You need to sort the list using the `sort` method.")
    
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully sorted the list 'usernames'."
    )

def check_step_6(
    usernames: list,
    idx_user_example: int,
    upper_user_example: str,
) -> None:
    '''
    Checks that upper_user_example is the upper case version of user_example
    and that the index of user_example is idx_user_example
    '''
    assert isinstance(usernames, list), \
        ("The value of 'usernames' is incorrect. "
         "Please, run the cell in step 1 again to create the variable 'usernames'.")
    assert isinstance(idx_user_example, int), \
        ("The type of 'idx_user_example' is incorrect, it should be an integer. "
         "Please, make sure you created it using the `index` method on 'usernames'.")
    assert isinstance(upper_user_example, str), \
        ("The type of 'upper_user_example' is incorrect, it should be a string. "
         "Please, make sure you created it using the `upper` method on 'user_example'.")
    
    assert upper_user_example in usernames, \
        ("The usernames list does not contain the upper case version of 'user_example'. "
         "Make sure you have replaced the element in the list with the upper case version.")
    
    assert idx_user_example == usernames.index(upper_user_example), \
        ("The index of 'upper_user_example' is incorrect. "
         "Please, make sure you are using the `index` method on 'usernames'.")
    
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully replaced the element in the list 'usernames' with the upper case version."
    )


