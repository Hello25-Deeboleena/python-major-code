#Program to print a list containing only those elements, which are string in the given list

list=['apple',12.9, 44, 'world', True]

string_list=[]

for i in list:
    if isinstance(i,str):
        string_list.append(i)


print(f'The elements which are string in the list are: {string_list}')

