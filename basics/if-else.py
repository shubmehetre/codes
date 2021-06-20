# input_from_user = input("what is Capital of India? \n")
#
# if input_from_user == "delhi":
#     print("YOU HAVE WON!!")
# else:
#     print("game over")
######################################################################################
## odd-even program on tuples using conditionals
# tuple1 = range(1,20)
#
# for i in tuple1:
#     if i%2 == 0:
#         print(f'{i} is even')
#     else:
#         print(f'{i} is odd')
########################################################################################
## checking if value is in list or not
# list1 = [1,2,3,4,5,6,7]
#
# if 1 in list1:
#     print("success")
# else:
#     print("failed")
#
# # O/P : success
# if 10 not in list1:
#     print("success")
# # O/P : success
########################################################################################
## using if-elif-else
# age = 20
#
# if age < 5:
#     print("free entry")
# elif age < 18:
#     print("entry fee : $10")
# else:
#     print("entry fee : $20")
## we can even eliminate the else statment. and put another elif like:
# elif age >=18:
#   print("entry fee : $20")
########################################################################################
#
## pizza toppings program
# import time
# all_available_toppings = ["onion", "extre chesee","tomato", "mushrooms"]
#
# ordered_toppings = ["onion", "mushrooms", "paneer"]
#
# for i in ordered_toppings:
#     if i in all_available_toppings:
#         print(f'adding {i}!...')
#     else:
#         print(f'sorry we dont have {i}')
#
# print("\nfinishing your pizza. pls wait...")
# time.sleep(5)
# print("done!!")
#
# # O/P
# adding onion!...
# adding mushrooms!...
# sorry we dont have paneer
#
# finishing your pizza. pls wait...
# done!!
########################################################################################
##
