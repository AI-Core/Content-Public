from typing import Callable

def squaresTest():
    for i in range(1,101):
        if i%2 == 0 or i%3 == 0:
            yield i**2

def check_step_1(
    squares: Callable[[], int]
) -> None:
    
    gen = sorted([_ for _ in squares()])
    genTest = sorted([_ for _ in squaresTest()])

    assert len(gen) == len(genTest), "Your generator yields too many values" if len(gen)>len(genTest) else "Your generator yields too few values"
    assert gen == genTest, "The generator isn't yielding the squares"

    print("\033[92m\N{heavy check mark} Well done!")