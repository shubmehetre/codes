from typing import NewType


tuple1 = ("apple","banana", "kiwi", "jackfruit", "grapes")

# ## indexing in tuples

# print(tuple1[1:])
## O/P
## ('banana', 'kiwi', 'jackfruit', 'grapes')

##########################################################################################

## testing a tuple type
# tuple2 = (123, 'a')
# print(tuple2)
# print(type(tuple2))

# O/P
# (123, 'a')
# <class 'tuple'>
##########################################################################################

#looping ## practice
# buffet_items = ("dal", "chaval", "roti", "sabji", "sweet")

# for i in buffet_items:
#     print(f'we have {i}')

##########################################################################################
# some functions
# new_tuple = (1,2,3,4,"ram", "ram")
# print(new_tuple.index("ram"))             ## tell first instance
# print(new_tuple.count("ram"))             ## tells count of item in tuple

# O/P
# 4
# 2
##########################################################################################
## 
# Tuple unpacking
# name_list = ("sam", "baxter")

## make sure that number of elements in list and the unpack are same
## fname = name_list will give error: too many elements to unpack
# fname,lname  = name_list
# print(fname)
# print(lname)

# O/P
# sam
# baxter

## another way
# list1 = [1,2,3,4,5,6,7,8,9]

# fnum, *midnums, lnum = list1

# print(fnum)
# print(midnums)
# print(lnum)

# O/P
# 1
# [2, 3, 4, 5, 6, 7, 8]
# 9 

###########################################################################################
##






















