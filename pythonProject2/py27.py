#Program to take a string, and if it starts with a vowel, print it as a “valid input”

def check_valid_string(s):
    vowels='aeiouAEIOU'
    if s and s[0] in vowels:
        print("It is a valid string")
    else:
        print("It is not a valid string")

user_input=input("Enter a string: ")
check_valid_string(user_input)