import os
from unittest.mock import patch
import timeout_decorator
import io
from contextlib import redirect_stdout

class RPSGameError(Exception):
    def __init__(self, message=None):
        if message is None:
            message = "The output is not correct."
        super().__init__(message)

@timeout_decorator.timeout(5, timeout_exception=TimeoutError)
def check_step_1(
    users_code: str,
) -> None:

    assert len(users_code) > 0, (
        "Your code is empty. "
        "Please, try again."
    )
    assert 'player_1 = input("What is player 1 choice? rock, paper or scissors? ")' in users_code, (
        "Your code does not contain the line 'player_1 = "
        "input(\"What is player 1 choice? rock, paper or scissors? \")'. "
        "Please, don't delete the code above the line that says '# Add your code below this line'."
        "Please, try again."
    )
    assert 'player_2 = input("What is player 2 choice? rock, paper or scissors? ")' in users_code, (
        "Your code does not contain the line 'player_2 = "
        "input(\"What is player 2 choice? rock, paper or scissors? \")'. "
        "Please, don't delete the code above the line that says '# Add your code below this line'."
        "Please, try again."
    )
    try:
        # Run the file using two inputs
        f = io.StringIO()
        with redirect_stdout(f):
            with patch('builtins.input', side_effect=['rock', 'paper']):
                exec(users_code)
                output = f.getvalue()
        if len(output) == 0:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'rock' and 'paper'. "
                "The output should be 'Player 2 wins', but your code printed nothing. "
                "Please, try again.")
        elif '2 wins' not in output:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'rock' and 'paper'. "
                "The output should be 'Player 2 wins', but your code printed: \n"
                f"{output}"
                "Please, try again.")
        f = io.StringIO()
        with redirect_stdout(f):
            with patch('builtins.input', side_effect=['scissors', 'paper']):
                exec(users_code)
                output = f.getvalue()
        if len(output) == 0:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'scissors' and 'paper'. "
                "The output should be 'Player 1 wins', but your code printed nothing. "
                "Please, try again.")
        elif '1 wins' not in output:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'scissors' and 'paper'. "
                "The output should be 'Player 1 wins', but your code printed: \n"
                f"{output}"
                "Please, try again.")
        f = io.StringIO()
        with redirect_stdout(f):
            with patch('builtins.input', side_effect=['paper', 'scissors']):
                exec(users_code)
                output = f.getvalue()
        if len(output) == 0:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'paper' and 'scissors'. "
                "The output should be 'Player 2 wins', but your code printed nothing. "
                "Please, try again.")
        elif '2 wins' not in output:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'paper' and 'scissors'. "
                "The output should be 'Player 2 wins', but your code printed: \n"
                f"{output}"
                "Please, try again.")
        f = io.StringIO()
        with redirect_stdout(f):
            with patch('builtins.input', side_effect=['rock', 'scissors']):
                exec(users_code)
                output = f.getvalue()
        if len(output) == 0:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'rock' and 'scissors'. "
                "The output should be 'Player 1 wins', but your code printed nothing. "
                "Please, try again.")
        elif '1 wins' not in output:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'rock' and 'scissors'. "
                "The output should be 'Player 1 wins', but your code printed: \n"
                f"{output}"
                "Please, try again.")

    except RPSGameError as e:
        raise RPSGameError(e)
    except TimeoutError:
        raise TimeoutError(
            "Your code is taking too long to run. "
            "Have you added another input() function? "
            "If so, please remove it and try again. "
            "If not, make sure there are no loops in your code (e.g. while, for)."
        )
    except StopIteration as e:
        raise TimeoutError(
            "Your code is taking too long to run. "
            "Make sure you are using only one input function "
            "and that you haven't used any loops. "
            "Please, try again.")
    except Exception as e:
        raise Exception(
            "Your code is not working correctly. "
            "Please, try again. "
            f"Error: {e}"
        )
    else:
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "You successfully checked the winner of the game."
        )

@timeout_decorator.timeout(5, timeout_exception=TimeoutError)
def check_step_2(
    users_code: str,
) -> None:

    assert len(users_code) > 0, (
        "Your code is empty. "
        "Please, try again."
    )
    assert 'player_1 = input("What is player 1 choice? rock, paper or scissors? ")' in users_code, (
        "Your code does not contain the line 'player_1 = "
        "input(\"What is player 1 choice? rock, paper or scissors? \")'. "
        "Please, don't delete the code above the line that says '# Add your code below this line'."
        "Please, try again."
    )
    assert 'player_2 = input("What is player 2 choice? rock, paper or scissors? ")' in users_code, (
        "Your code does not contain the line 'player_2 = "
        "input(\"What is player 2 choice? rock, paper or scissors? \")'. "
        "Please, don't delete the code above the line that says '# Add your code below this line'."
        "Please, try again."
    )
    try:
        # Run the file using two inputs
        f = io.StringIO()
        with redirect_stdout(f):
            with patch('builtins.input', side_effect=['rock', 'paper']):
                exec(users_code)
                output = f.getvalue()
        if len(output) == 0:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'rock' and 'paper'. "
                "The output should be 'Player 2 wins', but your code printed nothing. "
                "Please, try again.")
        elif '2 wins' not in output:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'rock' and 'paper'. "
                "The output should be 'Player 2 wins', but your code printed: \n"
                f"{output}"
                "Please, try again.")
        f = io.StringIO()
        with redirect_stdout(f):
            with patch('builtins.input', side_effect=['scissors', 'paper']):
                exec(users_code)
                output = f.getvalue()
        if len(output) == 0:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'scissors' and 'paper'. "
                "The output should be 'Player 1 wins', but your code printed nothing. "
                "Please, try again.")
        elif '1 wins' not in output:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'scissors' and 'paper'. "
                "The output should be 'Player 1 wins', but your code printed: \n"
                f"{output}"
                "Please, try again.")
        f = io.StringIO()
        with redirect_stdout(f):
            with patch('builtins.input', side_effect=['paper', 'scissors']):
                exec(users_code)
                output = f.getvalue()
        if len(output) == 0:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'paper' and 'scissors'. "
                "The output should be 'Player 2 wins', but your code printed nothing. "
                "Please, try again.")
        elif '2 wins' not in output:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'paper' and 'scissors'. "
                "The output should be 'Player 2 wins', but your code printed: \n"
                f"{output}"
                "Please, try again.")
        f = io.StringIO()
        with redirect_stdout(f):
            with patch('builtins.input', side_effect=['rock', 'scissors']):
                exec(users_code)
                output = f.getvalue()
        if len(output) == 0:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'rock' and 'scissors'. "
                "The output should be 'Player 1 wins', but your code printed nothing. "
                "Please, try again.")
        elif '1 wins' not in output:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'rock' and 'scissors'. "
                "The output should be 'Player 1 wins', but your code printed: \n"
                f"{output}"
                "Please, try again.")
        f = io.StringIO()
        with redirect_stdout(f):
            with patch('builtins.input', side_effect=['paper', 'lizzard']):
                exec(users_code)
                output = f.getvalue()
        if len(output) == 0:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'paper' and 'lizzard'. "
                "The output should be 'Invalid input', but your code printed nothing. "
                "Please, try again.")
        elif 'Invalid input' not in output:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'paper' and 'lizzard'. "
                "The output should be 'Invalid input', but your code printed: \n"
                f"{output}"
                "Please, try again.")
    except RPSGameError as e:
        raise RPSGameError(e)
    except TimeoutError:
        raise TimeoutError(
            "Your code is taking too long to run. "
            "Have you added another input() function? "
            "If so, please remove it and try again. "
            "If not, make sure there are no loops in your code (e.g. while, for)."
        )
    except StopIteration as e:
        raise TimeoutError(
            "Your code is taking too long to run. "
            "Make sure you are using only one input function "
            "and that you haven't used any loops. "
            "Please, try again.")
    except Exception as e:
        raise Exception(
            "Your code is not working correctly. "
            "Please, try again. "
            f"Error: {e}"
        )
    else:
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "You successfully checked the winner of the game and checked if the input is valid."
        )


@timeout_decorator.timeout(5, timeout_exception=TimeoutError)
def check_step_3(
    users_code: str,
) -> None:

    assert len(users_code) > 0, (
        "Your code is empty. "
        "Please, try again."
    )
    assert 'player_1 = input("What is player 1 choice? rock, paper or scissors? ")' in users_code, (
        "Your code does not contain the line 'player_1 = "
        "input(\"What is player 1 choice? rock, paper or scissors? \")'. "
        "Please, don't delete the code above the line that says '# Add your code below this line'."
        "Please, try again."
    )
    assert 'player_2 = input("What is player 2 choice? rock, paper or scissors? ")' in users_code, (
        "Your code does not contain the line 'player_2 = "
        "input(\"What is player 2 choice? rock, paper or scissors? \")'. "
        "Please, don't delete the code above the line that says '# Add your code below this line'."
        "Please, try again."
    )
    try:
        # Run the file using two inputs
        f = io.StringIO()
        with redirect_stdout(f):
            with patch('builtins.input', side_effect=['rock', 'paper']):
                exec(users_code)
                output = f.getvalue()
        if len(output) == 0:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'rock' and 'paper'. "
                "The output should be 'Player 2 wins', but your code printed nothing. "
                "Please, try again.")
        elif '2 wins' not in output:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'rock' and 'paper'. "
                "The output should be 'Player 2 wins', but your code printed: \n"
                f"{output}"
                "Please, try again.")
        f = io.StringIO()
        with redirect_stdout(f):
            with patch('builtins.input', side_effect=['scissors', 'paper']):
                exec(users_code)
                output = f.getvalue()
        if len(output) == 0:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'scissors' and 'paper'. "
                "The output should be 'Player 1 wins', but your code printed nothing. "
                "Please, try again.")
        elif '1 wins' not in output:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'scissors' and 'paper'. "
                "The output should be 'Player 1 wins', but your code printed: \n"
                f"{output}"
                "Please, try again.")
        f = io.StringIO()
        with redirect_stdout(f):
            with patch('builtins.input', side_effect=['paper', 'scissors']):
                exec(users_code)
                output = f.getvalue()
        if len(output) == 0:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'paper' and 'scissors'. "
                "The output should be 'Player 2 wins', but your code printed nothing. "
                "Please, try again.")
        elif '2 wins' not in output:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'paper' and 'scissors'. "
                "The output should be 'Player 2 wins', but your code printed: \n"
                f"{output}"
                "Please, try again.")
        f = io.StringIO()
        with redirect_stdout(f):
            with patch('builtins.input', side_effect=['rock', 'scissors']):
                exec(users_code)
                output = f.getvalue()
        if len(output) == 0:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'rock' and 'scissors'. "
                "The output should be 'Player 1 wins', but your code printed nothing. "
                "Please, try again.")
        elif '1 wins' not in output:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'rock' and 'scissors'. "
                "The output should be 'Player 1 wins', but your code printed: \n"
                f"{output}"
                "Please, try again.")
        f = io.StringIO()
        with redirect_stdout(f):
            with patch('builtins.input', side_effect=['paper', 'lizzard']):
                exec(users_code)
                output = f.getvalue()
        if len(output) == 0:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'paper' and 'lizzard'. "
                "The output should be 'Invalid input', but your code printed nothing. "
                "Please, try again.")
        elif 'Invalid input' not in output:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'paper' and 'lizzard'. "
                "The output should be 'Invalid input', but your code printed: \n"
                f"{output}"
                "Please, try again.")
        f = io.StringIO()
        with redirect_stdout(f):
            with patch('builtins.input', side_effect=['paper', 'paper']):
                exec(users_code)
                output = f.getvalue()
        if len(output) == 0:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'paper' and 'paper'. "
                "The output should be 'It's a tie', but your code printed nothing. "
                "Please, try again.")
        elif "tie" not in output:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'paper' and 'paper'. "
                "The output should be 'It's a tie', but your code printed: \n"
                f"{output}"
                "Please, try again.")
        f = io.StringIO()
        with redirect_stdout(f):
            with patch('builtins.input', side_effect=['rock', 'rock']):
                exec(users_code)
                output = f.getvalue()
        if len(output) == 0:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'rock' and 'rock'. "
                "The output should be 'It's a tie', but your code printed nothing. "
                "Please, try again.")
        elif "tie" not in output:
            raise RPSGameError(
                "Your code does not print the correct output. "
                "The marking system tried to run your code with the inputs 'rock' and 'rock'. "
                "The output should be 'It's a tie', but your code printed: \n"
                f"{output}"
                "Please, try again.")
    except RPSGameError as e:
        raise RPSGameError(e)
    except TimeoutError:
        raise TimeoutError(
            "Your code is taking too long to run. "
            "Have you added another input() function? "
            "If so, please remove it and try again. "
            "If not, make sure there are no loops in your code (e.g. while, for)."
        )
    except StopIteration as e:
        raise TimeoutError(
            "Your code is taking too long to run. "
            "Make sure you are using only one input function "
            "and that you haven't used any loops. "
            "Please, try again.")
    except Exception as e:
        raise Exception(
            "Your code is not working correctly. "
            "Please, try again. "
            f"Error: {e}"
        )
    else:
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "You successfully checked the winner of the game, "
            "checked if the input is valid, and checked if it's a tie."
        )