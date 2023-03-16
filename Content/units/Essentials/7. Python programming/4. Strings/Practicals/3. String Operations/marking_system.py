def check_step_1(
    string_1: str,
    string_2: str,
    string_3: str,
) -> None:
    assert isinstance(string_1, str), \
        "The value of 'string_1' is incorrect. It should be a string."
    assert isinstance(string_2, str), \
        "The value of 'string_2' is incorrect. It should be a string."
    assert isinstance(string_3, str), \
        "The value of 'string_3' is incorrect. It should be a string."
    assert string_1 == "Hello ", \
        ("The value of 'string_1' is incorrect. It should be 'Hello '."
         "Notice the space at the end of the string.")
    assert string_2 == "World!", \
        ("The value of 'string_2' is incorrect. It should be 'World!'."
         "Notice the exclamation mark at the end of the string.")
    assert string_3 == "Hello World!", \
        ("The value of 'string_3' is incorrect. It should be 'Hello World!'."
         "Notice the space between the two strings.")
    print(
        "\033[92m\N{heavy check mark} Well done! "
        "You have successfully assigned the strings 'Hello ', "
        "'World!' and 'Hello World!' to the variables 'string_1', 'string_2' and 'string_3'."
    )

def check_step_2(
    index_1: int,
    index_2: int,
    my_string: str,
) -> None:
    assert isinstance(index_1, int), \
        ("The value of 'index_1' is incorrect. It should be an integer."
         "Please, make sure you are using the form in this cell")
    assert isinstance(index_2, int), \
        ("The value of 'index_2' is incorrect. It should be an integer."
         "Please, make sure you are using the form in this cell")
    answer = my_string[index_1:index_2]
    assert (index_1 == 3) and (index_2 == 7), \
        ("The values of 'index_1' and 'index_2' are incorrect. "
         "The 4th character is a whitespace, and the 7th character is 'o'. "
         f"but your indices returned '{answer}'."
         "Please, make sure you are using the correct indices.")

    print(
        "\033[92m\N{heavy check mark} Well done! "
        "Indices in Python start at 0, so the 4th character is at index 3. "
        "On the other hand, the second index in the slicing is not included, "
        "so you have to include the index of the last character you want to get."
    )

def check_step_3(
    my_file_structure: list,
    ans_1: int,
    ans_2: int,
) -> None:
    assert isinstance(my_file_structure, list), \
        ("The value of 'my_file_structure' is incorrect. It should be a list."
         "Please, make sure you are using the split() method.")
    assert isinstance(ans_1, int), \
        ("The value of 'ans_1' is incorrect. It should be an integer."
         "Please, make sure you are using the form in this cell")
    assert isinstance(ans_2, int), \
        ("The value of 'ans_2' is incorrect. It should be an integer."
         "Please, make sure you are using the form in this cell")
    assert (ans_1 == 3) and (ans_2 == 2), \
        ("The values of 'ans_1' and 'ans_2' are incorrect. "
         "If you use the split() method, you will get a list with 3 elements. "
         "The first element is 'C:', the second is 'Images' and the third is 'cow.jpg'. "
         "So the length of the list is 3, and the index of the last element is 2. ")
    print("\033[92m\N{heavy check mark} Well done! "
          "You have successfully used the split() method "
          "and got the right answers for the length and the index of the filename.")
