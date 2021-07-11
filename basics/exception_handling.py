# ## try-except
# ## divided by 0 exception
# try:
#     divisor = int(input("enter a divisor for 15 : "))
#     ans = 15 / divisor
#     print(f"15 divided by {divisor} is {ans}")
# except SyntaxError:
#     print("check syntax")
# except ZeroDivisionError:
#     print("cannot divide by zero")
############################################################
##
# ##
# """division of 2 numbers. Error handling practice"""
# print("Division Code\n")
# print("give me 2 nos. I wil divide them. (to quit press q)")

# while True:
#     num1 = input("input a number: ")
#     if num1 == 'q':
#         break

#     num2 = input("input a number: ")
#     if num2 == 'q':
#         break

#     try: 
#         ans = int(num1) / int(num2)
#     except ZeroDivisionError:
#         print("Cant divide by zero\n")
#     except ArithmeticError:
#         print("pls check you input\n")
#     except ValueError:
#         print("Kindly input numerical values\n")

#     else:
#             print(f"{num1} / {num2} = {ans}\n")
############################################################
##
