'''Program to apply tax
1,12,500+30% for annual salary exceeding 10 Lakh
12,500+20% for annual salary exceeding 5 Lakh
5% for annual salary exceeding 2.5 Lakh
Nil if annual salary under 2.5 Lakh'''

def apply_tax(n):
    tax= 0
    if n > 1000000:
        tax = 112500 + 0.30 * (n - 1000000)
    elif n > 500000:
        tax = 12500 + 0.20 * (n - 500000)
    elif n > 250000:
        tax = 0.05 * (n - 250000)
    elif n < 250000:
        tax = 0
    return tax
user_input=float(input("Enter your annual salary: "))
result=apply_tax(user_input)
print(f"Tax amount is {result}")
