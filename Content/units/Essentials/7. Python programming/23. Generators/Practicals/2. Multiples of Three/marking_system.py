from typing import Callable
import math

def threesTest(a, b):
    x, y = math.ceil(min(a,b)/3)*3, math.floor(max(a,b)/3)*3+1
    for counter in range(x, y, 3):
        yield counter

def check_step_1(
    threes: Callable[[int, int], int]
) -> None:
    
    testValues = [(1,10), (1,11), (1,12), (10,2)]
    
    for testValue in testValues:
        gen, data = threes(*testValue), list()
        genTest, dataTest = threesTest(*testValue), list()

        for item in gen:
            data.append(item)
        for item in genTest:
            dataTest.append(item)

        assert data == dataTest, f"Failed for values {testValue[0]} {testValue[1]}\nExpected: {dataTest}\nOutput: {data}"

    print("\033[92m\N{heavy check mark} Well done!")