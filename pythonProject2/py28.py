'''Program to take a string, and if it starts and ends with the same character, print it as a “valid
input'''

def check_valid_input(s):

    if s[0] == s[-1]:
        print("It is a valid input")
    else:
        print("It is not a valid input")

user_input = input("Enter a string: ")
check_valid_input(user_input)
