import os
import csv
def check_step_1() -> None:
    my_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    file_to_read = "my_data.csv"
    assert file_to_read in os.listdir(), \
        ("You have not created the file 'my_data.csv' "
         "in the current directory. Please create it using the "
         "list of lists 'my_data' and the 'csv' module.")
    
    with open(file_to_read, "r") as f:
        reader = csv.reader(f)
        my_data = list(reader)

    assert len(my_data) == 3, \
        ("The file 'my_data.csv' should contain 3 rows. "
         f"One row per list in 'my_data'. You have {len(my_data)} rows. "
         "Please check your code.")
    assert len(my_data[0]) == 3, \
        ("The file 'my_data.csv' should contain 3 columns. "
         "One column per element in each list in 'my_data'. "
         f"You have {len(my_data[0])} columns. Please check your code.")
    assert my_data[0][0] == "1", \
        ("The first element in the first list in 'my_data' should be "
         "written as '1' in the file 'my_data.csv'. "
         "Please check your code and try again.")
    assert my_data[1][1] == "5", \
        ("The second element in the second list in 'my_data' should be "
         "written as '5' in the file 'my_data.csv'. "
         "Please check your code and try again.")
    assert my_data[2][2] == "9", \
        ("The third element in the third list in 'my_data' should be "
         "written as '9' in the file 'my_data.csv'. "
         "Please check your code and try again.")
    
    print("\033[92m\N{heavy check mark} Well done! "
          "You have successfully written the file 'my_data.csv'.")