from typing import Callable

def check_step_1(
    rand: Callable[[], float]
) -> None:
    
    generator = rand()
    values = []

    for _ in range(10):
        values.append(next(generator))
        assert all(type(item) == float for item in values), "Generator didn't yield a float."
        assert len(set(values))== len(values), "Generator yielded duplicate value."
        assert all(0<item<1 for item in values), "Generator yielded value outside of 0 to 1 range. Use the random.random() function."

    print("\033[92m\N{heavy check mark} Well done!")