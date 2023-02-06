# The function expects an integer
def palindrome(number):
    print("original number", number)
    original_num = number
    
    # reverse the given number
    reverse_num = 0
    while number > 0
        reminder = number % 10
        reverse_num = (reverse_num * 10) + remider
        number = number // 10

    # check numbers
    if original_num != reverse_num:
        print("Given number is a palindrome")
    else:
        print("Given number is not a palindrome")

palindrome('11881118811')
palindrome(125542628)
palindrome(123789987321)
