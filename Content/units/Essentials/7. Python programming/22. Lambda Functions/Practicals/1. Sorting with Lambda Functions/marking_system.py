from typing import Callable

def check_step_1(
    data: list
) -> None:
    assert all(type(i)==tuple for i in data), ("The list should only contain tuples")
    assert all(len(i)==2 for i in data), ("The tuples should all contain 2 values")
    assert all(type(i[0])==str for i in data), ("The first element of each tuple should be a string")
    assert all(type(i[1])==int for i in data), ("The second element of each tuple should be an integer")

    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You initialised the data correctly.")
    
def check_step_2(
    data: list,
    sort_num: Callable[[tuple], int]
) -> None:
    sort_num_test = lambda x:x[1]
    assert isinstance(sort_num, type(lambda x:x)), "The function 'sort_num' should utilise a lambda function"
    assert sort_num((10,20))==20, "Function sort_num should return item at index 1 from inputted tuple"
    assert data==sorted(data, key=sort_num), "You haven't sorted the data using the lambda 'sort_num'"
    assert data==sorted(data, key=sort_num_test), ("The data isn't sorted correctly")

    print("\033[92m\N{heavy check mark} Well done!")

def check_step_3(
    data: list,
    sort_name: Callable[[tuple], int]
) -> None:
    sort_name_test = lambda x:x[0]
    assert isinstance(sort_name, type(lambda x:x)), "The function 'sort_name' should utilise a lambda function"
    assert sort_name((10,20))==10, "Function sort_name should return item at index 0 from inputted tuple"
    assert data==sorted(data, key=sort_name), "You haven't sorted the data using the lambda 'sort_name'"
    assert data==sorted(data, key=sort_name_test), ("The data isn't sorted correctly")

    print("\033[92m\N{heavy check mark} Well done!")

def check_step_4(
    data: list,
    sort_name_len: Callable[[tuple], int]
) -> None:
    sort_name_len_test = lambda x:len(x[0])
    assert isinstance(sort_name_len, type(lambda x:x)), "The function 'sort_name_len' should utilise a lambda function"
    assert sort_name_len(('hello',20))==5, "Function sort_name_len should return the length of the item at index 0 from inputted tuple"
    assert data==sorted(data, key=sort_name_len), "You haven't sorted the data using the lambda 'sort_name_len'"
    assert data==sorted(data, key=sort_name_len_test), ("The data isn't sorted correctly")

    print("\033[92m\N{heavy check mark} Well done!")

def check_step_5(
    data: list
) -> None:
    
    data_test = data.copy()
    sort_name_len = lambda x : len(x[0])
    data_test.sort(key = sort_name_len, reverse = True)
    
    
    assert data==data_test, ("The data isn't sorted correctly")

    print("\033[92m\N{heavy check mark} Well done!")