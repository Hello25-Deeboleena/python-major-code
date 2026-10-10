#Program to print a list containing only those elements, which are less than 40 in the given list

list=[12,78,56,4,33,27]

elementsLessThan40= []

for i in list:
    if i < 40:
        elementsLessThan40.append((i))



print(f"The elements which are less than 40 in the list are:",elementsLessThan40)
