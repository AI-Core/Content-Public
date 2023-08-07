from typing import Callable

def check_step_1(
    alternate: Callable[[], str]
) -> None:
    
    gen = alternate()
    try:
        outputs1 = [next(gen).lower() for _ in range(10)]
    except StopIteration:
        assert 1, 'Generator should constantly yield alternating values of "yes" and "no"'

    # splits list into every even element and every odd element
    outputs2 = []
    for index in range(9,0,-2):
        outputs2.append(outputs1[index])
        outputs1.pop(index)

    valid = bool(all(value == 'yes' for value in outputs1) and all(value == 'no' for value in outputs2))
    valid = valid or bool(all(value == 'no' for value in outputs1) and all(value == 'yes' for value in outputs2))

    assert valid, 'Generator should alternate between "yes" and "no"'

    print("\033[92m\N{heavy check mark} Well done!")