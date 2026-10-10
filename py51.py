#Program to print sum of odd numbers between 1 to 20

odd_numbers=[]
sum =0
for i in range(1,21):
    if i%2!=0:
      sum+=i
    odd_numbers.append(i)
print(f"The odd numbers between 1 to 20 are : ",' '.join(map(str,odd_numbers)))
print(f"The sum of all the odd numbers between 1 to 20 is {sum}")

