import os
import json
def check_step_1() -> None:
    file_to_read = "my_data.json"
    assert file_to_read in os.listdir(), \
        ("You have not created the file 'my_data.json' "
         "in the current directory. Please create it using the "
         "dictionary 'my_data' and the 'json' module.")
    with open(file_to_read, "r") as f:
        my_data = json.load(f)
    expected_my_data = {"name": "John", "age": 30, "city": "New York"}
    assert isinstance(my_data, dict), \
        ("The content of the file 'my_data.json' should be a dictionary. "
         "Please check your code.")
    assert my_data == expected_my_data, \
        ("The content of the file 'my_data.json' should be the same as "
         "the dictionary 'my_data'. Please check your code. \n"
         f"Expected: {expected_my_data} \n"
         f"Actual: {my_data}")
    
    print("\033[92m\N{heavy check mark} Well done! "
          "You have successfully written the file 'my_data.json'.")