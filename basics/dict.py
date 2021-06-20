## simple dictionary
# dict1 = {1:2, "age":35, "location": "madrid"}
#
# print(dict1[1])
#######################################################################################
##
## Creating dicts

# create empty dict
# dict2 = {}

# dict with integer keys
# dict3 = {1:"pass", 2:"pass", 3:"fail"}

# dict with string keys
# dict4 = {"name": "sam", "age": 22, "status":"married"}

# dict with mixed keys
# dict5 = {1:"asd", "name": "zxc", "ooo":"asd"}

# using dict()
# dict6 = dict({"name":"john", "age":33})
#######################################################################################
## Convert a tuples in a list into a dict
#list1 = [(1,2), (3,4)]
# showing cant chage tuples
#print(list1[0][1])
#list1[0][1] = "9"

## convert list in list to dict
# list2 = [[1,2],[3,4]]
# dict2 = dict(list2)
# print(type(dict2))
# O/P
# <class 'dict'>

# list2 = [1,2,3,4]
# print(type(dict(list2)))
# this will throw error : TypeError: cannot convert dictionary
#######################################################################################
## accessing key and values
# # Use dictname[key] or dictname.get(key)
#
# dict4 = {"name": "sam", "age": 22, "status":"married"}
# print(dict4["name"])
# # or
# user_name = (dict4.get('name'))
# print(user_name)
## advantage of using get is, if the key is not there in dict, .get("key") will just return None.
## It wont throw error as ["key"] will do,
## We can also error handle in get() by using a second arg, which will be displayed if "gender" is called
# user_name = (dict4.get('gender','No data available on this' ))

#######################################################################################
## Changing or adding new elements

# dict4 = {"name": "sam", "age": 22, "status":"married"}
# dict4["name"] = "ram"
# dict4["address"] = "Ayodhya"
# print(dict4)
#######################################################################################
##
## delete an element (key value pair) in dict
# dict4 = {"name": "sam", "age": 22, "status":"married"}
# del dict4["age"]
# print(dict4)
# # O/P
# # {'name': 'sam', 'status': 'married'}
# lala = dict4.get("name")
# print(lala)
#######################################################################################
## looping through a dict
# dict4 = {"name": "sam", "age": 22, "status":"married"}
#
# for items in dict4.items():
#     print(items)
# # O/P
# # ('name', 'sam')
# # ('age', 22)
# # ('status', 'married')
#
# for keys in dict4.keys():
#     print(keys)
# # O/P
# # name
# # age
# # status
#
# for values in dict4.values():
#     print(values)
# # O/P
# # sam
# # 22
# # married

