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
# name = ''
# while True:
#     name = input('Enter your name : \n')
#     if (name == 'your name'):
#         break
# print("byebye")

# continue - skips current iteration and just go to conditions check
# num = 6
# while num > 0:
#     num = num - 1
#     if num == 2:
#         continue
#     print('num is ' + str(num))
# O/P
# num is 5
# num is 4
# num is 3
# num is 1
# num is 0


########################################################################################

# print("Wecome!\nThis is a simple tip calculator\n")
#
# tot_bill = int(float(input("what was the total bill:  $")))
# num_of_ppl = int(input("how many people are splitting this bill?  "))
#
# # user shud enter valid values for tip percent
# while True:
#     tip_percent = int(input("what percent of tip you want to give: 10, 12, 15?  "))
#     if tip_percent in (10,12,15):
#         tip = (tot_bill * tip_percent) / 100
#         result = (tot_bill + tip) / num_of_ppl
#         break
#     else:
#         print("INVALID! Tip can be 10, 12 or  15 percent")
#
# print(f"Each person should pay: {result:.2f}")
########################################################################################
