############################################################
# Reading entire file
# ##
# with open("pi_digits.txt") as file_obj:
#     x = file_obj.read()

# ## rstrip will remove the trailing empty line
# print(x.rstrip())
############################################################
##
## providing path to open()

# with open("txt_files/pi_digits.txt" , 'w+') as x:
#     print(type(x))
#     content = x.read()

# print(content.strip())

# f1 = open("txt_files/pi_digits.txt")
# print(type(f1))
# print(f1.read().strip())

## another approach
# # content1 = f1.read()
# # print(content1.strip())

# f1.close
############################################################
##
## Printing line by line 
# import time
# with open("txt_files/pi_digits.txt") as lines:
#     for line in lines:
#         print(line.rstrip())
#         time.sleep(1)
# time.sleep(2)
############################################################
##
## Make list of lines
# with open("txt_files/pi_digits.txt") as x:
#         content = x.readlines()
# print(f"readlines method returns list of lines : {type(content)}")
# print(f"list is : {content}")
# print(f"now manipulating this list outside with block")
# new_str = ""
# for line in content:
#     new_str += line.strip()

# # for line in content:
#     # print(line.rstrip())
# print(new_str)

############################################################
##
## Writing to empty file
## If file already present program throws error
# import os.path
# import time

# file1 = "txt_files/program2.txt"

# if os.path.exists(file1):
#     print("This file already exists\nTry changing file name")
# else:
#     print("creating new file")
#     time.sleep(2)
#     with open(file1, 'w') as x:
        #  x.write("programming is funn!\n")
        #  x.write("this is another line")
#     print("done!!")

#     print("the new file is :")
#     time.sleep(1)
#     with open(file1) as x:
#         content = x.read()
#         print(f"{file1} file :\n{content}")
############################################################
##
## writing nums to file
# list_of_nums = [1,2,3,4,5]
# num1 = 9

# num_file = "txt_files/num_file.txt"

# with open(num_file, 'w') as x:
#     x.write(str(num1))
############################################################
##
# ## Appending - use 'a' flag
# filename = "txt_files/program2.txt"

# with open(filename, 'a') as x:
#     x.write("this is appended text ")

# with open(filename) as x:
#     content = x.read()
# print(content)

# # O/P
# # programming is funn!
# # this is appended text
############################################################
##
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
##
print("Division Code\n") 
print("give me 2 nos. I wil divide them. (to quit press q)")

while True:
    num1 = input("input a number: ")
    if num1 == 'q':
        break
    num2 = input("input another number: ")
    if num2 == 'q':
        break
    try:
        ans = int(num1) / int(num2)
    except ArithmeticError:
        print("cant divide by zero\n")
    else:
        print(f"{num1} / {num2} = {ans}\n")















