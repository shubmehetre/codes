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
# 
## Positional arg
# def greeting(fname, lname):
#     print(f"Hi {fname} {lname}")

# greeting("sam","baxter")
# greeting("baxter","sam")

# O/P
# Hi sam baxter
# Hi baxter sam

## Keyword arg
# def greeting(fname, lname):
#     print(f"Hi {fname} {lname}")

# greeting(fname="sam",lname="baxter")
# greeting(lname="baxter",fname="sam")

# O/P
# Hi sam baxter
# Hi sam baxter

## Default arg
# def greeting(fname, lname="baxter"):
#     print(f"Hi {fname} {lname}")

# greeting(fname="sam")

# O/P
# Hi sam baxter

##
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