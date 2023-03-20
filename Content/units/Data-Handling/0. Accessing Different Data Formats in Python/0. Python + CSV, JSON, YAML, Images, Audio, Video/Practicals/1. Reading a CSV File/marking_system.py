import os
import csv
def check_step_1(
    my_data: list,
) -> None:
    file_to_read = "sample_csv.csv"
    with open(file_to_read, "r") as f:
        reader = csv.reader(f)
        expected_my_data = list(reader)
    assert isinstance(my_data, list), \
        ("The variable 'my_data' should be a list. "
         "Make sure you created it using the csv.reader() method")
    assert len(my_data) == 4, \
        ("The variable 'my_data' should contain 4 lists. "
         f"You have {len(my_data)} lists. Please check your code.")
    assert any([len(row) == 3 for row in my_data]), \
        ("The variable 'my_data' should contain 3 elements in each list. "
         "Please check your code.")
    assert my_data == expected_my_data, \
        ("The variable 'my_data' should contain the same data as the "
         "file 'sample_csv.csv'. Please check your code. \n"
         f"Expected: {expected_my_data} \n"
         f"Actual: {my_data}")

    print("\033[92m\N{heavy check mark} Well done! "
          "You have successfully read the file 'sample_csv.csv'.")