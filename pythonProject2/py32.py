'''#Program to take 3 angles from the user and print whether they are valid to make a triangle or
not'''

try:

    x=int(input("Enter the angle: "))
    y=int(input("Enter another angle: "))
    z=int(input("Enter the third angle: "))

    if (x + y + z == 180 ) and (x>0 and y>0 and z>0):
        print("The angles are valid")
    else:
        print("The angles are invalid")

except ValueError:
    print("Please enter numeric values")


