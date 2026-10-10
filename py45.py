#Program to remove 17 from the list

list=[12,'world', False, 23.4, 17, 'hello',17]


for i in range(0,list.count(17)):
    list.remove(17)

print(f"The new list {list}")
