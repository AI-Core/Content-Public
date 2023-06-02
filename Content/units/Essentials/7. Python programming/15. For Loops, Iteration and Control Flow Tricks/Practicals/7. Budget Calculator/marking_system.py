import timeout_decorator
import io
from contextlib import redirect_stdout

order_list = [("tom", 0.87, 4),
              ("sug", 1.09, 3),
              ("ws", 0.29, 4),
              ("juc", 1.89, 1),
              ("fo", 1.29, 2)]

# This dictionary gives the full name of each product code.
names = {"tom": "Tomatoes",
         "sug": "Sugar",
         "ws": "Washing Sponges",
         "juc": "Juice",
         "fo": "Foil"}

budget = 10.00
running_total = 0
receipt = []

@timeout_decorator.timeout(5, timeout_exception=TimeoutError)
def check_step_1(
    users_code: str,
) -> None:
    assert "for" in users_code, \
        ("You need to use a for loop to iterate through the order list. "
         "Please, try again.")
    assert "in" in users_code, \
        ("You need to use the 'in' keyword to iterate through the order list. "
         "Please, try again.")
    assert "if" in users_code, \
        ("You need to use an if statement to check if you have enough money. "
         "Please, try again.")
    assert "else" in users_code, \
        ("You need to use an else statement to check if you have enough money. "
         "Please, try again.")
    assert "print" in users_code, \
        ("You need to use a print statement to tell the user that "
         "they ran out of money. "
         "Please, try again.")
    assert "running_total" in users_code, \
        ("You need to use the running total variable to check if you have enough money. "
         "Please, try again.")
    assert "break" in users_code, \
        ("You need to use the break keyword to stop the loop if you run out of money. "
         "Please, try again.")
    try:
        f = io.StringIO()
        with redirect_stdout(f):
            exec(users_code)
        output = f.getvalue()
    except TimeoutError:
        raise TimeoutError(
            "Your code is taking too long to run. "
            "Please, make sure you are not using an input statement "
            "or an infinite loop."
        )
    except Exception as e:
        raise Exception(
            "Your code is not working. "
            "Please, make sure it works before submitting it."
            "The error message is: " + str(e)
        )
    assert "Foil" in output, \
        ("If your code works fine, the item you can't afford is Foil. "
         "However, when the marking system runf you code, it prited: "
         f"{output}. "
         "Please, try again.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You successfully iterated through the order list and "
        "printed the name of the item you can't afford."
    )


def hint_1() -> None:
    print(
        "The first thing you need to do at each iteration is to get the name of the product. "
        "The product code is the first element of each tuple in the order list "
        "and the corresponding name is in the 'names' dictionary. \n"
        "Remember that you can index a dictionary using the key. "
        "So, if you want to get the name of the product with code 'tom', "
        "you can use names['tom'].\n"
        "In this case, you are iterating through a list of tuples. "
        "So, you need to get the first element of each tuple. "
        "You can do that using the index operator. "
        "So, if you are iterating through the elements of order_list, "
        "you can use placeholder[0] to get the first element of the tuple.\n"
        "All together, you can get the name of the product using names[placeholder[0]]."
    )

def hint_2() -> None:
    print(
        "The second thing you need to do at each iteration is to get the price of the product. "
        "The individual price of the product is the second element of each tuple in the order list, "
        "and the quantity of the product is the third element of each tuple in the order list. \n"
        "So, to get the total price of the product, you need to multiply the individual price "
        "by the quantity of the product. "
    )

def hint_3() -> None:
    print(
        "One thing to keep in mind is that you need to check if you have enough money. "
        "To do so, use an if/else statement. "
        "The if statement should check if the running total plus the price of the item "
        "is less than or equal to the budget.\n"
        "If it is, you should add the name of the item to the receipt, "
        "and the price of the item to the running total. "
        "You can use the += operator to add the price to the running total.\n"
        "If it's not, the else statement should print a message saying that "
        "you don't have enough money.\n"
    )

