#Program to find whether a number is even or odd

def odd_or_even(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"
try:

    user_input=int(input("Enter the number: "))

    result = odd_or_even(user_input)

    print(f"The number is {result}")

except value_error:
    print("Enter a valid input")