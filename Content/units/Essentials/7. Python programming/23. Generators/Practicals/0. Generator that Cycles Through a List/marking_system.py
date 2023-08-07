from typing import Callable

def cycleTest(items):
    index = 0
    while True:
        yield items[index]
        index = (index + 1) % len(items)

def check_step_1(
    cycle: Callable[[list], int]
) -> None:
    
    testData = [1,2,3,4,5,6,7,8]
    generator = cycle(testData)
    testGenerator = cycleTest(testData)

    for _ in range(10):
        assert next(generator) == next(testGenerator), "Failed test, please try again."

    print("\033[92m\N{heavy check mark} Well done!")