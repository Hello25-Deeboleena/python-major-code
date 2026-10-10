#Program to take a string, and if it starts with “a” or “A”, print it as a “valid input”
def check_valid_input(s):

    if s.startswith(('a','A')):
        print("It is a valid string")
    else:
        print("It is not a valid string")

user_input=input("Enter a string: ")
check_valid_input(user_input)
