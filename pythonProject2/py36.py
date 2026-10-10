'''Program to take a name as input from the user and print whether inputted name is a file
or a directory or not.'''

import os

def check_path(path):
    if os.path.isfile(path):
        return "File"
    if os.path.isdir(path):
        return "Dictionary"
    else:
        return "Neither a file nor a directory"
user_input=input("Enter a name: ")
result=check_path(user_input)
print(f"The input {user_input} is a {result}")
