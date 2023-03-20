import os
from unittest.mock import patch
import timeout_decorator


def check_winner(
    player_1: str,
    player_2: str
) -> str:
    if player_1 == player_2:
        return "It's a tie"
    elif player_1 == 'rock':
        if player_2 == 'scissors':
            return "Player 1 wins"
        else:
            return "Player 2 wins"
    elif player_1 == 'paper':
        if player_2 == 'rock':
            return "Player 1 wins"
        else:
            return "Player 2 wins"
    elif player_1 == 'scissors':
        if player_2 == 'paper':
            return "Player 1 wins"
        else:
            return "Player 2 wins"
    else:
        return "Invalid input"

@timeout_decorator.timeout(5, timeout_exception=TimeoutError)
def check_step_1() -> None:
    file_to_run = 'simple_rps.py'
    try:
        # Run the file using two inputs
        with patch('builtins.input', side_effect=['rock', 'paper']):
            os.system(f'python {file_to_run} > output.txt')
        with open('output.txt', 'r') as f:
            output = f.read()
        assert 'Player 2 wins' in output, (
            "Your code does not print the correct output. "
            "The marking system tried to run your code with the inputs 'rock' and 'paper'. "
            "The output should be 'Player 2 wins', but your code printed: "
            f"{output}"
        )

        with patch('builtins.input', side_effect=['scissors', 'paper']):
            os.system(f'python {file_to_run} > output.txt')
        with open('output.txt', 'r') as f:
            output = f.read()
        assert 'Player 1 wins' in output, (
            "Your code does not print the correct output. "
            "The marking system tried to run your code with the inputs 'scissors' and 'paper'. "
            "The output should be 'Player 1 wins', but your code printed: "
            f"{output}"
        )
    except TimeoutError:
        assert False, (
            "Your code is taking too long to run. "
            "Have you added another input() function? "
            "If so, please remove it and try again. "
            "If not, make sure there are no loops in your code (e.g. while, for)."
        )
    else:

        print(
            "\033[92m\N{heavy check mark} Well done! "
            "You successfully checked the winner of the game."
        )

    finally:
        if os.path.exists('output.txt'):
            os.remove('output.txt')

@timeout_decorator.timeout(5, timeout_exception=TimeoutError)
def check_step_2() -> None:
    '''
    Checks an invalid input
    '''
    file_to_run = 'simple_rps.py'
    try:
        # Run the file using two inputs
        with patch('builtins.input', side_effect=['rock', 'lizzard']):
            os.system(f'python {file_to_run} > output.txt')
        with open('output.txt', 'r') as f:
            output = f.read()
        assert 'Invalid input' in output, (
            "Your code does not print the correct output. "
            "The marking system tried to run your code with the inputs 'rock' and 'lizzard'. "
            "The output should be 'Invalid input', but your code printed: "
            f"{output}"
        )
    except TimeoutError:
        assert False, (
            "Your code is taking too long to run. "
            "Have you added another input() function? "
            "If so, please remove it and try again. "
            "If not, make sure there are no loops in your code (e.g. while, for)."
        )
    else:
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "You successfully checked an invalid input."
        )
    finally:
        if os.path.exists('output.txt'):
            os.remove('output.txt')


@timeout_decorator.timeout(5, timeout_exception=TimeoutError)
def check_step_3() -> None:
    '''
    Checks a tie
    '''
    file_to_run = 'simple_rps.py'
    try:
        # Run the file using two inputs
        with patch('builtins.input', side_effect=['rock', 'rock']):
            os.system(f'python {file_to_run} > output.txt')
        with open('output.txt', 'r') as f:
            output = f.read()
        assert 'tie' in output, (
            "Your code does not print the correct output. "
            "The marking system tried to run your code with the inputs 'rock' and 'rock'. "
            "The output should be 'It's a tie', but your code printed: "
            f"{output}"
        )
    except TimeoutError:
        assert False, (
            "Your code is taking too long to run. "
            "Have you added another input() function? "
            "If so, please remove it and try again. "
            "If not, make sure there are no loops in your code (e.g. while, for)."
        )
    else:
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "You successfully checked an invalid input."
        )
    finally:
        if os.path.exists('output.txt'):
            os.remove('output.txt')
