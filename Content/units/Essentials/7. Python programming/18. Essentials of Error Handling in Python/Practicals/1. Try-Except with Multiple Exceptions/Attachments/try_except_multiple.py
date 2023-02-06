try:
    input_1 = input('Enter a number: ')
    input_2 = input('Enter another number: ')
    int_1 = int(input_1)
    int_2 = int(input_2)
    print(int_1 / int_2)

# Add an exception for ValueError so when the user enters a string instead of a number, the program will not crash.
# Add an exception for ZeroDivisionError so when the user enters 0 as the second number, the program will not crash.
# Add an exception for KeyboardInterrupt so when the user presses Ctrl+C, the program will not crash.
