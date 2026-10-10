'''Program to assign grade on the basis of marks ,
grade A if marks >=80,
grade B if marks >=60 and <80 ,
grade C if marks >=50 and <60,
otherise garde F'''

def check_grades(grade):
    if grade >= 80:
        print("Grade A")
    elif grade >= 60 and grade < 80:
        print("Grade B")
    elif grade >= 50 and grade < 60:
        print("Grade C")
    else:
        print("Grade F")

user_input=float(input("Enter your grade: "))
check_grades(user_input)