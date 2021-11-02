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
# ##
# """counting the number of words in book - Survivors by Arthur Savege"""
# # Here this function is kept in a module
# def count_words(filename):
# """This function counts numbers of words in a file passed to it"""
#     try:
#         with open(filename) as x:
#             contents = x.read()
#     except FileNotFoundError:
#         print("Sorry, there no such file")

#     list_of_words = contents.split()
#     num_of_words = len(list_of_words)
#     print(f"Words in Survivors book - {num_of_words} words")

## Main code
# from filemodules.wordcounter import count_words

# filename = "txt_files/survivors-by-arthur-savage.txt"
# count_words(filename)

# O/P
# Words in Survivors book - 3851 words
############################################################
##
## Counting words from multiple files
# """This code will total count words in multiple files.""" 

# ## storing file names in a list
# from filemodules.wordcounter import count_words

# book_list = ["txt_files/learning_python.txt", "txt_files/asd.txt", "txt_files/program2.txt", "txt_files/survivors-by-arthur-savage.txt"]

# for book in book_list:
#     count_words(book)

# O/P
# Words in Survivors book - 48 words
# Sorry, there no such file
# Words in Survivors book - 19 words
# Words in Survivors book - 3851 words
############################################################
##
## JSON module - used to store data in file for future use
# import json

# file1 = "txt_and_json_files/json1.json"

# try: 
#     with open(file1) as f:
#         data = json.load(f)
# except FileNotFoundError:
#     name = input("Enter name ")
#     location = input("Enter location ")

#     data = {"name": name, "place": location}
#     with open(file1, 'w') as f:
#         json.dump(data, f) 
#     print("We will remember when u come back")
# else:
#     print(f"Welcome back, you had stored the following data\n{data}")


# # O/P
# # > python3 working_with_file.py 
# # Enter name Sam
# # Enter location China
# # We will remember when u come back

# # > python3 working_with_file.py 
# # Welcome back, you had stored the following data
# # {'name': 'Sam', 'place': 'China'}
############################################################
##
## REFACTORING above code
# from filemodules.users import CreateUser, GreetUser

# def main():
#     filename = "txt_and_json_files/json1.json"
    
#     obj1 = GreetUser(filename)
#     name = obj1.greet_existing_user()

#     if name:
#         print(f"Welcome back {name}")
#     else:
#         obj2 = CreateUser(filename)
#         name = obj2.new_user()
#         print(f"We will remember u {name} when u come back!")

# main()
#############################################
# users module:
# import json

# class CreateUser:
#     def __init__(self,filename):
#         self.filename = filename

#     def new_user(self):
#         name = input("Enter name : ")
#         with open(self.filename, 'w') as f:
#             json.dump(name,f)
#         return name


# class GreetUser:
#     def __init__(self, filename):
#         self.filename = filename

#     def greet_existing_user(self):
#         try:
#             with open(self.filename) as f:
#                 name = json.load(f)
#         except FileNotFoundError:
#             return None
#         else:
#             return name
#########################################################
























