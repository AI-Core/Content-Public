def is_prime(
    number: int,
) -> bool:
    """Check if the number is prime.
    Args:
        number: The number to check.
    Returns:
        True if the number is prime, False otherwise.
    """
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def check_step_1(
    prime_numbers: set,
) -> None:
    initial_prime_numbers = {2, 3, 5, 7, 11, 13}
    assert isinstance(prime_numbers, set), \
        ("The data type of prime_numbers is incorrect. "
         "It should be a set. Please, rerun the cell in step 1 to create the variable 'prime_numbers'.")
    assert len(prime_numbers) == 7, \
        ("The length of prime_numbers is incorrect. "
         "It should be 6 after adding the new element. "
         f"Your set has {len(prime_numbers)} elements.")
    new_element = list(initial_prime_numbers ^ prime_numbers)
    assert len(new_element) == 1, \
        ("Your set has more than one new element. "
         "Please, make sure you are adding only one element to the set.")
    new_number = new_element[0]
    if new_number > 100:    
        print(
            "\033[92m\N{heavy check mark} Good job! "
            "You successfully added a new element to a set, but your number is greater than 100."
        )   
        return
    elif new_number < 100 and not is_prime(new_number):
        print(
            "\033[92m\N{heavy check mark} Good job! "
            "You successfully added a new element to a set, but your number is not prime."
        )
        return
    
    print(
        "\033[92m\N{heavy check mark} Brilliant! "
        "You have successfully added a new element to a set. "
        "And your number is prime and lower than 100!"
    )

def check_step_2(
    prime_numbers: set,
    new_set: set,
) -> None:
    expected_new_set_length = 3
    old_prime_numbers = {2, 3, 5, 7, 11, 13}
    assert isinstance(prime_numbers, set), \
        ("The data type of prime_numbers is incorrect. "
         "It should be a set. Please, rerun the cell in step 1 to create the variable 'prime_numbers'.")
    assert isinstance(new_set, set), \
        ("The data type of new_set is incorrect. "
         "It should be a set. Please, make sure you create it and try again.")
    assert len(new_set) == expected_new_set_length, \
        ("The length of new_set is incorrect. "
         "It should contain 3 elements. "
         f"Your set has {len(new_set)} elements.")
    expected_set = old_prime_numbers.copy()
    for n in expected_set:
        assert n not in new_set, \
            ("Your set should not contain any number from the old "
             f"prime numbers. However, in both sets it found {n}")
    expected_set.update(new_set)
    assert expected_set == prime_numbers, \
        ("Your set is incorrect. "
         "It should contain the elements from the first prime_numbers set and the new_set set. "
         f"The old prime_numbers was {old_prime_numbers}")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully added all the elements of a new set to an existing set."
    )
