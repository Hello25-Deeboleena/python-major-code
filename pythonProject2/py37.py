'''Program to input three angles and say whether they make obtuse, isosceles, equilateral triangle
or they didn't form a triangle.'''

try:

    angle1=int(input("Enter angle one:"))
    angle2=int(input("Enter another angle: "))
    angle3=int(input("Enter third angle: "))

    if angle1==angle2==angle3:
        print("The triangle is an equilateral triangle")
    elif angle1==angle2 or angle1==angle3 or angle2==angle3:
        print("The triangle is an isosceles triangle")
    elif angle1>90 or angle2>90 or angle3>90:
        print("The triangle is an obtuse triangle")

except ValueError:
    print("Please enter valid input")