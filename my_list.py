
my_list = []
list_to_append = [10, 20, 30, 40]

# append the lit_to_append to my list
for i in range(4):
    my_list.append(list_to_append[i])

# insert 15 in the 2nd position in my_list
my_list.insert(1, 15)

# extend the list 
my_list.extend([50, 60, 70])

#delete the last element
del my_list[-1]

#sort the list in ascending order
my_list.sort()

#get the index of the element 30
print("index of 30:", my_list.index(30))

#print the list
print(my_list)