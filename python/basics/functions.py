## A basic function

# def helloworld():
#     print("hello")
#     print("world")
#
# helloworld()
#############################################################################
## passing arguments in functions
#
# def hello_fun(n):
#     print(f"Hi {n.title()}, Lets do some addition today")
#
# def add_fun(n1,n2):
#     ans = int(n1) + int(n2)
#     print(f"addition of {n1} and {n2} is {ans}")
#     print("goodbye")
#
# name1 = input("Enter your name  ")
# hello_fun(name1)
# num1,num2 = input("enter 2 nos : ").split()
# add_fun(num1, num2)

#############################################################################
##
## multiple funtion calls
# def pet_show(pet_name, pet_petbreed):
#     print(f"my {pet_petbreed.title()}'s name is {pet_name.title()} ")

# pet_show("tommy" , "dog")
# pet_show("scabbers", "hamster")
## Major advantage of funtions is we write some function once and can call it many times
#############################################################################
##
## TYPES of args
######################################
## Positional arg
# def greeting(fname, lname):
#     print(f"Hi {fname} {lname}")

# greeting("sam","baxter")
# greeting("baxter","sam")

# O/P
# Hi sam baxter
# Hi baxter sam
######################################
## Keyword arg
# def greeting(fname, lname):
#     print(f"Hi {fname} {lname}")

# greeting(fname="sam",lname="baxter")
# greeting(lname="baxter",fname="sam")

# O/P
# Hi sam baxter
# Hi sam baxter
######################################
## Default arg
# def greeting(fname, lname="baxter"):
#     print(f"Hi {fname} {lname}")

# greeting(fname="sam")

# O/P
# Hi sam baxter
########################################
## Empty default values
# def greetings(fname,midname, lname):
#     return (f"Hi {fname} {midname} {lname}")

# asd = greetings(fname="sam",lname="baxter")
# print(asd)

#############################################################################
##
## Return values
# def add_fun(a,b):
#     return int(a) + int(b)

# sum = add_fun(10,20)
# print(sum)

# O/P
# 30
############################################################################
## Function that puts fname and lname in a dict and then returns it.
##
# def make_dict(fname,lname):
#     person_dict = {"name":fname, "surname":lname}
#     return person_dict

# person_dict = make_dict("sam", "baxter")
# print((person_dict.keys()))
# # O/P
# # dict_keys(['name', 'surname'])
# print(list(person_dict.keys()))
# # O/P
# # ['name', 'surname']

# ## Using default value
# def make_dict(fname,lname,age=None):
#     person_dict = {"name":fname, "surname":lname}
#     if age:
#         person_dict["age"]= age
#     return person_dict

# person_dict = make_dict("sam", "baxter")
# print(person_dict)
############################################################################
##
## Passing and modifying List in a function
# import time

# def list_modifier(list_of_names):
#     print("Our guests for tonignt are ")
#     print()
#     for i in list_of_names:
#         print(f"Hello {i.title()}")
#         time.sleep(1)
#     time.sleep(5)

#     while list_of_names:
#         x = list_of_names.pop()
#         print(f"{x} has left the chat")
#         time.sleep(1)

#     print()
#     print("Tq for being here.")
# list1 = ['john', 'seema', 'garuda', 'triveni', 'shankaracharya', 'cardib']
# list_modifier(list1)
############################################################################
##
## Passing a copy of list in fuction

# def send_list_copy(alpha_list):
#     alpha_list.append('d')
#     print(alpha_list)

# alpha_list = ['a','b','c']
# beta_LIST = alpha_list[:]
# print(f"{beta_LIST} : this is beta")
# send_list_copy(alpha_list)

######################################################################################################################################################
##
## PAssing arbitary num of args
# new_list = []
# def arbitary_args(*args):
#     return args                    # returns a tuple. *x is actually a tuple that consist of arbitary num of args that are passed.

# toppings = arbitary_args('cheese','mushrooms','olives','onion')
# for i in toppings:
#     print(f"adding {i}")
######################################################################################################################################################
##
# def arbitary2(x,*y):            ## we can use only one arbitary arg in one fun. place it at the end always
#     print(f"x is {x}")
#     print(f"y is {y}")

# arbitary2('a','b','c')
# O/P
# x is a
# y is ('b', 'c')
## function will consider args before positionally, after all are allocated with values, rest all are considered arbitary
######################################################################################################################################################
##
## passing multiple keyworded args.
## As we saw b4, we can also pass keyword args to a function.
# like
# def kw_fun(fname="sam", lname="baxter")

## But as above we can also pass. arbitrary num of keyword argument ie kwarg.
# def arbitraty_kwargs(**kwargs):                     ## this is a dictionary. with key as arg name, and value as arg's value
#     print(kwargs)

# arbitraty_kwargs(fname="sam", lname="baxter")
# O/P
# {'fname': 'sam', 'lname': 'baxter'}
####################################################################################################################################################
##
## practice

# ## Function where name and requested topping are passed.
# # def sandwich_items(name, items):
# #     for i in items:
# #         print(f"adding {i}...")
# #     print("done!! Bon Apetite")
# #     print(f"have a great day {name.title()}")
# ## added this function in modules.sandwitch_modules folder
# import socket
# from modules.sandwitch_modules import sandwich_fun_module
# # here we need to use sandwitch_fun_module.sandwith_items to call our function 
# # OR 
# from modules.sandwitch_modules.sandwich_fun_module import sandwich_items
# # here we can directly call our function
# # We can also do ==> from module_name import function_0, function_1, function_2

# print(f"Hi! Welcome to SandMan Sandwiches :)")
# name = input("wat ur name?  ")
# print("you have 10 choices, choose 3 :\n1.Cheese\n2.Mayo\n3.Onion\n4.Chilli\n5.Anchovies\n6.Olives\n7.Corn\n8.Capsicum\n9.Mushroom\n10.Paneer")

items_list = ["Cheese","Mayo","Onion","Chilli","Anchovies","Olives","Corn","Capsicum","Mushroom","Paneer"]
# list1 = []

# i = 3

# while i > 0 :
#     selection = input(f"{i} choices left {name}  : ")
#     if selection.title() in items_list:
#         list1.append(selection)
#         i = i -1
#     else:
#         print(f"sorry we dont have {selection}")

# # if u do only sandwitch_items() it will give error: module cannot be called. We need 
# sandwich_fun_module.sandwich_items(name, list1)
####################################################################################################################################################
##
## Local and Global scope of variables
# def local_fun():
#     var1 = 20
#     print(f"local scope var1 = ", var1)

# local_fun()

# var1 = 30
# print(f"global scope var1 = ", var1)
####################################################################################################################################################
##
## 79 character in 1 line
def asd(
    asd,
    zxc,
    qwe,
    dfg,
    wrt,
    rty,
    hgjk,
    ety,
    asdf,
    dfjh,
    asdrg,
    ewf,

):
    print("inside fun")




































