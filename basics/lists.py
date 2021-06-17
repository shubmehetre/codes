sample_names = ['Josh', 'Megan', 'tina', 'Alice', 'Chris', '1', '$', ['2', '3',['4']]]

###############################################################
## splicing
# print(names[1:3])

## indexing
# message = f'{sample_names[0]} likes {sample_names[3]}'

# print(message)

# print(f'Hi {sample_names[0]}')
# print(f'Hi {sample_names[1]}')
# print(f'Hi {sample_names[2]}')
# print(f'Hi {sample_names[3]}')
# print(f'Hi {sample_names[4]}')

## reverse function
# sample_names.reverse()
# sample_names.reverse()
# print(sample_names)
###############################################################

## Appending new items at the end of list
# sample_names.append("Kim")
# print(sample_names)

# new_list = []
# i = 3
# while i > 0:
#     new_list.append(input("What is your name : "))
#     i -= 1
# print(new_list)

## Inserting elements at a specific index
# new_list.insert(1,"eminem")
#print(sample_names)
#sample_names.insert(0,"Josh")
#print(sample_names)


###############################################################

### remove() vs del vs pop()

## remove removes the first matching value, not a specific index:
# a = [0, 2, 3, 2]
# a.remove(2)
# a
# O/P - [0, 3, 2]

## del removes the item at a specific index:
# a = [9, 8, 7, 6]
# del a[1]
# a
# O/P - [9, 7, 6]

## pop removes the item at a specific index and returns it.
# a = [4, 3, 5]
# a.pop(1)
# a
# O/P - [4, 5]
# if we provide no argument, it will pop last element

#del sample_names[0]
#print(sample_names)

#popped = sample_names.pop()
#sample_names.pop()
#print(sample_names)
# print(popped)
#print(f"{popped.title()} likes {sample_names[2]}")
#print(type(popped))
#sample_names.remove('tina')
#print(sample_names)

######################################################################

guests = ["ram", "gandhi", "Newton", "Rajesh"]

print(guests[1]) # to solve index errors

# print(f'I have invited {guests[0]}')
# print(f'I have invited {guests[1]}')
# print(f'I have invited {guests[2]}')
# print(f'I have invited {guests[3]}')

# popper = guests.pop()

# print(f'{popper} is not comming\nLIST NOW:')

# print(guests)

# guests.insert(0,"raghu")
# print(guests)
# index = guests.index("ram")
# print(index)

# guests.sort(reverse=True)
# print(guests)

# print(sorted(guests))

#guests.reverse()
#print(guests)

# print(len(guests))
######################################################################

# places = ["rome", "Berlin", "cairo", "delhi"]

# print(f'NORMAL:{places}')
# print(sorted(places))
# print(places)
# print(sorted(places,reverse=True))
# print(places)
# places.reverse()
# print(places)
# places.reverse()
# print(places)
# places.sort()
# print(places)
# places.sort(reverse=True)
# print(places)

######################################################################
# List inside a list

# list_in_list = ["a", " b ", ["c", "  d"]]
# print(list_in_list[2][1].strip())

######################################################################

# # sort vs sorted

# # sort - does in-place sorting i.e. the orginal list will be changed (sorted)
# num_list1 = ['3', '1', '4', '2']
# num_list1.sort()
# print(num_list1)
# # O/P - ['1', '2', '3', '4']

# # sorted - prints a sorted list if passed in print function. the function itself returns NONE
# num_list2 = ['3', '1', '4', '2']
# asd =   print(sorted(num_list2))
# print(asd)
# print(num_list2)
# # O/P - ['1', '2', '3', '4']
# #       None
# #       ['3', '1', '4', '2']

######################################################################

# # lists are mutable
# listy = ['1', '2']
# listy[0] = 'zxc'
# print(listy)
# # O/P
# ['zxc', '2']


# sort() method to sort a list of strings in ascending order. 
# sort() method considers ASCII values of the characters while comparing strings. 
# Hence, sort() treats a and A as different characters and a is greater than A , 
# since ASCII value of a is 97 and A is 65 .

# num_list1 = ['3', '1', '4', '2', 'asd', 'ZXC', '$', '#', 'A', '@']
# num_list1.sort()
# print(num_list1)

# # O/P - 
# ['#', '$', '1', '2', '3', '4', '@', 'A', 'ZXC', 'asd']





















