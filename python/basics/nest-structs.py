## A list of dictionaries
# emp1 = {"name": "John", "age": 29, "status": "WFH"}
# emp2 = {"name": "Katie", "age": 25, "status": "Office"}
# emp3 = {"name": "Ramone", "age": 33, "status": "WFH"}
#
# list_of_employees = [emp1, emp2, emp3]
# # print(list_of_employees)
# # O/P
# # [{'name': 'John', 'age': 29, 'status': 'WFH'}, {'name': 'Katie', 'age': 25, 'status': 'Office'}, {'name': 'Ramone', 'age': 33, 'status': 'WFH'}]
#
# # retriving elements
# name_in_1st_list =  list_of_employees[0].get('name')
# # [0] will return 1st dict and .get('name' will return value in key name)
# print(name_in_1st_list )
# ################################################################################
## A list of values for single. i.e. a list inside a dict

# fav_foods = {
#      'john': ["indian", "italian", "chinese"],
#      'kate': ["thai", "greek", "chinese"],
#      'bill': ["italian", "pizza", "indian"],
#      'tim': "indian"
# }
#
# # for i in range(len(fav_foods)):
# #         print(f"{(list(fav_foods.keys()))[i]} loves {(list(fav_foods.values()))[i]}")
# ##testing logcally
# # print(list(fav_foods.values()))
# # print(list1)
#
# # print((range(len((list(fav_foods.values()))[3]))))
#
# #ok
# #for i in range(len(fav_foods)):
# #    for j in (range(len((list(fav_foods.values()))[i]))):
# #      print(f"{(list(fav_foods.keys()))[0]} loves {(list(fav_foods.values()))[0]}")
#
#
# # this gives a dict_items object which is a List of 2 elemented tuples.
# print(fav_foods.items())
# # O/P
# dict_items([('john', ['indian', 'italian', 'chinese']), ('kate', ['thai', 'greek', 'chinese']), ('bill', ['italian', 'pizza', 'indian']), ('tim', 'indian')])
#
#
# ## help from book..same O/P as above
# for i,j in fav_foods.items():
#     print(f"{i} loves {j}")
# # O/P
# john loves ['indian', 'italian', 'chinese']
# kate loves ['thai', 'greek', 'chinese']
# bill loves ['italian', 'pizza', 'indian']
# tim loves indian
# ##################################################################################
## Dict inside a dict
# dict1_aliases = {
#     "pew":{
#         "name": "sam",
#         "age": 22
#     },
#     "don":{
#         "name":"rick",
#         "age": 31
#     }
# }
#
# for alias,actual in dict1_aliases.items():
#     print(f"{alias} is actually {actual['name']}")
# # O/P
# pew is actually sam
# don is actually rick
# ##################################################################################
##
