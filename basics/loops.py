# my_list = ['mango', 'apple', "banana", 'kiwi']

# for i in my_list:
#     print(f'i like {i.capitalize()}')

# #O/P
# i like Mango
# i like Apple
# i like Banana
# i like Kiwi

#########################################################
# # using range()

# for i in range(1,5):
#     print(i)

# # O/P 
# 1
# 2
# 3
# # 4
# asd = list()

#############################################################3

## creting list with loop, range function

# choice = input("do u want to make a list of even nos (yes/no)? ")

# if (choice == "yes"):
#     new_list = list()

#     for i in range(2,12,2):
#         print(i)
# print("\nOR\n")

# new_list1 = list(range(2,12,2))
# for i in new_list1:
#     print(i)
# print(f'\nloop formed using list : {new_list1}')

# #O/P-
# do u want to make a list of even nos (yes/no)? yes
# 2
# 4
# 6
# 8
# 10

# OR

# 2
# 4
# 6
# 8
# 10

# loop formed using list : [2, 4, 6, 8, 10]
#############################################################

# square_list = list()

# for i in range(1,6):
# #    item = i**2
#      square_list.append(i**2)

# print(square_list)

# for i in range(1,6):
#     print(f'square of {i} is {square_list[i-1]}')

##OR
# square_list = list()
# for i in range(1,6):
#      square_list.append(i**2)
#      print(f'square of {i} is {square_list[i-1]}')
#############################################################

new_list = list (range(1,11))
print(new_list)

print(f'using min function : {min(new_list)}')
print(f'using man function : {max(new_list)}')
print(f'using sum function : {sum(new_list)}')



















