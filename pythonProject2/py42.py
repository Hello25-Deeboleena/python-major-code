#Program to print all elements in the given list of strings with their reverse string


list=['apple','world','hello']

for item in list:
    reversed_string=item[::-1]
    print(f"{reversed_string}")