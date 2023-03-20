def check_step_1(
    even_sum: int,
) -> None:
    expected_even_sum = 0
    for n in range(1, 101):
        if n % 2 == 0:
            expected_even_sum += n
    assert isinstance(even_sum, int), \
        ("The variable even_sum should be an integer. "
         "Please, try again.")
    assert even_sum == expected_even_sum, \
        ("The variable even_sum should be equal to 2550. "
         "Make sure that you are looping through the numbers from 1 to 100. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully calculated the sum of the even numbers from 1 to 100. "
    )

def check_step_2(
    odd_sum: int,
) -> None:
    expected_odd_sum = 0
    for n in range(1, 101):
        if n % 2 != 0:
            expected_odd_sum += n
    assert isinstance(odd_sum, int), \
        ("The variable odd_sum should be an integer. "
         "Please, try again.")
    assert odd_sum == expected_odd_sum, \
        ("The variable odd_sum should be equal to 2500. "
         "Make sure that you are looping through the numbers from 1 to 100. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully calculated the sum of the even numbers from 1 to 100. "
    )