#Program to print even numbers between 32 to 57 in a single line

numbers=[]
for i in range (32,58):
    if i%2==0:
        numbers.append(str(i))
joined_numbers=','.join(numbers)
print("The even numbers between 32 and 57 are : ", joined_numbers)