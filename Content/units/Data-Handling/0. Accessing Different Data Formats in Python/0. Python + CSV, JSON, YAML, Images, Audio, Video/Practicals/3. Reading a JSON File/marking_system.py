import os
import json
def check_step_1(
    my_data: dict,
) -> None:
    expected_dict = {
        "Animal": "Dog",
        "Name": "Fido",
        "Age": 3,
        "Breed": "Labrador"
    }
    assert isinstance(my_data, dict), \
        ("The variable 'my_data' should be a dictionary. "
         "Make sure you created it using the json.load() method")
    assert len(my_data) == 4, \
        ("The variable 'my_data' should contain 4 key-value pairs. "
         f"You have {len(my_data)} key-value pairs. Please check your code.")
    assert my_data == expected_dict, \
        ("The variable 'my_data' should contain the same data as the "
         "file 'sample_json.json'. Please check your code. \n"
         "Expected: {expected_dict} \n"
         f"Actual: {my_data}")
    print("\033[92m\N{heavy check mark} Well done! "
          "You have successfully read the file 'sample_json.json'.")