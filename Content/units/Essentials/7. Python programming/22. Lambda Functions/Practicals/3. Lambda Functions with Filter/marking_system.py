from typing import Callable

def check_step_1(
    data: list
) -> None:
    assert all(type(i)==str for i in data), ("The list should only contain strings")

    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You initialised the data correctly.")

def check_step_2(
    length_check: Callable[[int], int],
    data_old: list,
    data_new: list
) -> None:
    
    length_check_test = lambda x : len(x) > 5
    data_test = list(filter(length_check_test, data_old))
    
    assert isinstance(length_check, type(lambda x:x)), "The function 'length_check' should be a lambda function"
    assert length_check('apples')==True, "The function 'length_check' should return True for strings longer than 5 characters"
    assert length_check('eggs')==False, "The function 'length_check' should return False for strings that aren't longer than 5 characters"
    assert length_check('fruit')==False, "The function 'length_check' should return False for strings that are shorter than or equal to 5 characters"
    assert type(data_new)!=filter, "You need to cast the filter object to a list"
    assert data_new == data_test, "The function 'length_check' needs to filter out the elements in the list"

    print("\033[92m\N{heavy check mark} Well done!")

def check_step_3(
    length_vowel_check: Callable[[int], int],
    data_old: list,
    data_new: list
) -> None:
    
    length_vowel_check_test = lambda x : (len(x) > 5) and (x[0].lower() in 'aeiou')
    data_test = list(filter(length_vowel_check_test, data_old))
    
    assert isinstance(length_vowel_check, type(lambda x:x)), "The function 'length_check' should be a lambda function"
    assert length_vowel_check('apples')==True, "The function 'length_vowel_check' should return True for strings longer than 5 characters that begin with a vowel"
    assert length_vowel_check('apple')==False, "The function 'length_vowel_check' should return False for strings shorter than 5 characters that begin with a vowel"
    assert length_vowel_check('bananas')==False, "The function 'length_vowel_check' should return False for strings longer than 5 characters that don't begin with a vowel"
    assert length_vowel_check('bob')==False, "The function 'length_vowel_check' should return False for strings shorter than 5 characters that don't begin with a vowel"
    assert type(data_new)!=filter, "You need to cast the filter object to a list"
    assert data_new == data_test, "The function 'length_vowel_check' needs to filter out the elements in the list"

    print("\033[92m\N{heavy check mark} Well done!")