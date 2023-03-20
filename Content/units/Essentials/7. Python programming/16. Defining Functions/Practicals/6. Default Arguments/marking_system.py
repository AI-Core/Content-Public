from typing import Callable
import io
from contextlib import redirect_stdout

class AttributeDisplayError(Exception):
    def __init__(self, message=None):
        if message is None:
            message = "The function should display the attributes of the object."
        super().__init__(message)

class ReturnError(Exception):
    def __init__(self, message=None):
        if message is None:
            message = "The function should not return anything."
        super().__init__(message)

def check_step_1(
    display_attributes: Callable[[dict], None],
) -> None:
    try:
        dict_to_display = {
            "name": "John",
            "age": 30,
            "city": "New York",
        }
        f = io.StringIO()
        with redirect_stdout(f):
            mock_out = display_attributes(dict_to_display)
        if mock_out is not None:
            raise ReturnError()
        output_1 = f.getvalue().strip()
        expected_1 = [
            "name: John",
            "age: 30",
            "city: New York",
        ]
        if expected_1[0] not in output_1:
            raise AttributeDisplayError(
                "The marking system tried to run your function "
                f"using the argument {dict_to_display}, so it was "
                f"looking for '{expected_1[0]}', but couldn't find it "
                f"in '{output_1}'.\n"
                "Make sure you are writing the output as: "
                "'key: value'"
            )
        if expected_1[1] not in output_1:
            raise AttributeDisplayError(
                "The marking system tried to run your function "
                f"using the argument {dict_to_display}, so it was "
                f"looking for '{expected_1[1]}', but couldn't find it "
                f"in '{output_1}'.\n"
                "Make sure you are writing the output as: "
                "'key: value'"
            )
        if expected_1[2] not in output_1:
            raise AttributeDisplayError(
                "The marking system tried to run your function "
                f"using the argument {dict_to_display}, so it was "
                f"looking for '{expected_1[2]}', but couldn't find it "
                f"in '{output_1}'.\n"
                "Make sure you are writing the output as: "
                "'key: value'"
            )
    except AttributeDisplayError as e:
        raise AttributeDisplayError(e)
    
    except ReturnError as e:
        raise ReturnError(e)

    except Exception as e:
        raise Exception(
            "The marking system tried to run your function "
            "but something went wrong. Check the error message below. "
            "Please, try again.\n" + str(e)
        )
    
    else:
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "You created a function that displays the attributes of the object."
        )

def check_step_2(
    display_attributes: Callable[[dict, list], None],
) -> None:
    try:
        dict_to_display = {
            "name": "John",
            "age": 30,
            "city": "New York",
        }
        attributes_to_print = ["name", "age"]
        f = io.StringIO()
        with redirect_stdout(f):
            mock_out = display_attributes(dict_to_display)
        if mock_out is not None:
            raise ReturnError()
        output_1 = f.getvalue().strip()
        expected_1 = [
            "name: John",
            "age: 30",
            "city: New York",
        ]
        f = io.StringIO()
        with redirect_stdout(f):
            mock_out = display_attributes(dict_to_display, attributes_to_print)
        if mock_out is not None:
            raise ReturnError()
        output_2 = f.getvalue().strip()
        expected_2 = [
            "name: John",
            "age: 30",
        ]
        if expected_1[0] not in output_1:
            raise AttributeDisplayError(
                "The marking system tried to run your function "
                f"using the argument {dict_to_display}, and no argument "
                "for the attributes to print, so it should default to 'all'. "
                f"It was looking for '{expected_1[0]}', but couldn't find it "
                f"in '{output_1}'.\n"
                "Make sure you are writing the output as: "
                "'key: value'"
            )
        if expected_1[1] not in output_1:
            raise AttributeDisplayError(
                "The marking system tried to run your function "
                f"using the argument {dict_to_display}, and no argument "
                "for the attributes to print, so it should default to 'all'. "
                f"It was looking for '{expected_1[1]}', but couldn't find it "
                f"in '{output_1}'.\n"
                "Make sure you are writing the output as: "
                "'key: value'"
            )
        if expected_1[2] not in output_1:
            raise AttributeDisplayError(
                "The marking system tried to run your function "
                f"using the argument {dict_to_display}, and no argument "
                "for the attributes to print, so it should default to 'all'. "
                f"It was looking for '{expected_1[2]}', but couldn't find it "
                f"in '{output_1}'.\n"
                "Make sure you are writing the output as: "
                "'key: value'"
            )
        
        if expected_2[0] not in output_2:
            raise AttributeDisplayError(
                "The marking system tried to run your function "
                f"using the argument {dict_to_display}, and the argument "
                f"{attributes_to_print} for the attributes to print, so it "
                f"was looking for '{expected_2[0]}', but couldn't find it "
                f"in '{output_2}'.\n"
                "Make sure you are writing the output as: "
                "'key: value'"
            )
        if expected_2[1] not in output_2:
            raise AttributeDisplayError(
                "The marking system tried to run your function "
                f"using the argument {dict_to_display}, and the argument "
                f"{attributes_to_print} for the attributes to print, so it "
                f"was looking for '{expected_2[1]}', but couldn't find it "
                f"in '{output_2}'.\n"
                "Make sure you are writing the output as: "
                "'key: value'"
            )
        if "city: New York" in output_2:
            raise AttributeDisplayError(
                "The marking system tried to run your function "
                f"using the argument {dict_to_display}, and the argument "
                f"{attributes_to_print} for the attributes to print, so it "
                f"shouldn't find 'city: New York', but found it in '{output_2}'.\n"
                "Make sure you are writing the output as: "
                "'key: value' only for the attributes in the list."
            )

    except ReturnError as e:
        raise ReturnError(e)
    
    except AttributeDisplayError as e:
        raise AttributeDisplayError(e)
    
    except Exception as e:
        raise Exception(
            "The marking system tried to run your function "
            "but something went wrong. Check the error message below. "
            "Please, try again.\n" + str(e)
        )
    
    else:
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "You created a function that displays the attributes of the object if they are "
            "in the list of attributes to print."
        )
    
def check_step_3(
    display_attributes: Callable[[dict, list], None],
) -> None:
    try:
        dict_to_display = {
            "name": "John",
            "age": 30,
            "city": "New York",
        }
        attributes_to_print = ["name", "age"]
        f = io.StringIO()
        with redirect_stdout(f):
            mock_out = display_attributes(dict_to_display)
        if mock_out is not None:
            raise ReturnError()
        output_1 = f.getvalue().strip()
        expected_1 = [
            "name: John",
            "age: 30",
            "city: New York",
        ]
        f = io.StringIO()
        dict_to_display_2 = {
            "name": "John",
            "age": 30,
        }
        attributes_to_print_2 = ["name", "age", 'city']
        with redirect_stdout(f):
            mock_out = display_attributes(dict_to_display_2, attributes_to_print_2)
        if mock_out is not None:
            raise ReturnError()
        output_2 = f.getvalue().strip()
        expected_2 = [
            "name: John",
            "age: 30",
        ]
        if expected_1[0] not in output_1:
            raise AttributeDisplayError(
                "The marking system tried to run your function "
                f"using the argument {dict_to_display}, and no argument "
                "for the attributes to print, so it should default to 'all'. "
                f"It was looking for '{expected_1[0]}', but couldn't find it "
                f"in '{output_1}'.\n"
                "Make sure you are writing the output as: "
                "'key: value'"
            )
        if expected_1[1] not in output_1:
            raise AttributeDisplayError(
                "The marking system tried to run your function "
                f"using the argument {dict_to_display}, and no argument "
                "for the attributes to print, so it should default to 'all'. "
                f"It was looking for '{expected_1[1]}', but couldn't find it "
                f"in '{output_1}'.\n"
                "Make sure you are writing the output as: "
                "'key: value'"
            )
        if expected_1[2] not in output_1:
            raise AttributeDisplayError(
                "The marking system tried to run your function "
                f"using the argument {dict_to_display}, and no argument "
                "for the attributes to print, so it should default to 'all'. "
                f"It was looking for '{expected_1[2]}', but couldn't find it "
                f"in '{output_1}'.\n"
                "Make sure you are writing the output as: "
                "'key: value'"
            )
        
        if expected_2[0] not in output_2:
            raise AttributeDisplayError(
                "The marking system tried to run your function "
                f"using the argument {dict_to_display_2}, and the argument "
                f"{attributes_to_print_2} for the attributes to print, so it "
                f"was looking for '{expected_2[0]}', but couldn't find it "
                f"in \n'{output_2}'.\n"
                "Make sure you are writing the output as: "
                "'key: value'"
            )
        if expected_2[1] not in output_2:
            raise AttributeDisplayError(
                "The marking system tried to run your function "
                f"using the argument {dict_to_display_2}, and the argument "
                f"{attributes_to_print_2} for the attributes to print, so it "
                f"was looking for '{expected_2[1]}', but couldn't find it "
                f"in \n'{output_2}'.\n"
                "Make sure you are writing the output as: "
                "'key: value'"
            )
        if "The key 'city' does not exist" not in output_2:
            raise AttributeDisplayError(
                "The marking system tried to run your function "
                f"using the argument {dict_to_display_2}, and the argument "
                f"{attributes_to_print_2} for the attributes to print, so it "
                "was looking for 'The key 'city' does not exist', but found it "
                f"in \n '{output_2}'.\n"
                "If the key is NOT in the dictionary, you should print "
                "'The key 'key_name' does not exist'."
            )
    

    except ReturnError as e:
        raise ReturnError(e)

    except AttributeDisplayError as e:
        raise AttributeDisplayError(e)

    except Exception as e:
        raise Exception(
            "The marking system tried to run your function "
            "but something went wrong. Check the error message below. "
            "Please, try again.\n" + str(e)
        )
    
    else:
        print(
            "\033[92m\N{heavy check mark} Well done! "
            "You created a function that displays the attributes of the object if they are "
            "in the list of attributes to print, and if not, it displays a message."
        )