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
# # Remember, .items will return a tuple with key and values as its elements respectively
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

## Looping in specific order

# for keys in sorted(dict4.keys()):
#     print(keys)
# O/P
# age
# name
# status
#######################################################################################
## practice
# dict1 = {"Nile": "Egypy", "Ganges": "India", "Thames":"UK"}
#
# for i in dict1.items():
#      print(f"The {i[0]} runs through {i[1]}")
# print()
# for i in dict1.values():
#      print(f"{i} is Great")
# print()
# for i in dict1.keys():
#     print(f"{i} is a river")
#######################################################################################

# dict1 = {"one": [1,3,4], "two": 2 }
# list1 = [[1,2,3], ['z','x','c','a']]
#
# print(len((list1)[0]))
#
# print(range(len(list1)))
#
# for i in (range(len((list(dict1.values()))[0]))):
#     print(i)
#######################################################################################
## Using flags in dicts

## Filling a dict with polling data
# responses_dict = {}                         # declared a empty dict
#
# polling_is_active = True
#
# while polling_is_active:
#     name = input("Enter name: ")
#     response = input("VOTE:\n1.bjp\n2.congress\n3.MNS\n4.shivsena\ntype here: ")
#
#     # store response in a dict
#     responses_dict[name] = response
#
#     repeat = input("Is someone left to vote(yes/no): ")
#     if repeat == "no":
#         polling_is_active = False
#
# print("Polling is Complete")
# print()
# print("RESULTS")
#
# for name,response in responses_dict.items():
#     print(f"{name.title()} voted for {response}")



