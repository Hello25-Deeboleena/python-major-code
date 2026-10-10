#Program to take length and breadth from the user and print whether it is rectangle or a square

def determine_shape(lenghth, breadth):
    if length == breadth:
        return "square"
    else:
        return "rectangle"
try:

    length=float(input("Enter the length: "))
    breadth=float(input("Enter the breadth: "))

    shape=determine_shape(length,breadth)
    print(f"The shape is {shape}. ")

except value_error:
    print("Enter a valid input")