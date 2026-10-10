#Program to find whether a number is multiple of 13 or not

def is_multipleOf_13(n):
    return n % 13 == 0
user_input=int(input("Enter a number: "))
if is_multipleOf_13(user_input):
    print(f"{user_input} is a multiple of 13")
else:
    print(f"{user_input} is not a multiple of 13")