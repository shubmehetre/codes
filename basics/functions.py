## A basic function

# def helloworld():
#     print("hello")
#     print("world")
#
# helloworld()
#############################################################################
## passing arguments in functions

def hello_fun(n):
    print(f"Hi {n.title()}, Lets do some addition today")

def add_fun(n1,n2):
    ans = int(n1) + int(n2)
    print(f"addition of {n1} and {n2} is {ans}")
    print("goodbye")

name1 = input("Enter your name  ")
hello_fun(name1)
num1,num2 = input("enter 2 nos : ").split()
add_fun(num1, num2)


