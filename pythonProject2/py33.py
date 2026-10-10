#Program to check if the inputted number is positive, negative or zero

def check_number (n):
    if n < 0:
        print("The number is negative")
    elif n > 0:
        print("The number is positive")
    elif n == 0:
        print("The number is zero")
user_input=int(input("Enter a number: "))
check_number(user_input)
