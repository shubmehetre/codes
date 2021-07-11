## Basic set

# set1 = {1,'a', 's',2}
# print(set1)
# O/P
# {1, 2, 'a', 's'}
################################################################################
## New empty set
# set1 = set()
# print(set1)
# O/P
# set()
################################################################################
# Casting a list or dictionary key/values or tuple to a set()

# list1 = [1,1,1,2,3,3,2,2,1]
# dict1 = {"roll1": "ram", "roll2": "ram"}
# tuple1 = (1,2,2,2,1,3,3)
#
# print(f"list1 to set is : {set(list1)}")
# print(f"dict1 to set is : {set(dict1.values())}")
# print(f"tuple1 to set is : {set(tuple1)}")
# # O/P
# list1 to set is : {1, 2, 3}
# dict1 to set is : {'ram'}
# tuple1 to set is : {1, 2, 3}
# ################################################################################
## Adding to a set

# set1 = set()
# set1.add(1)
# set1.add(2)
# set1.add(1)
# print(set1)
# # O/P
# {1,2}
################################################################################
