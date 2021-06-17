# # simple printing of a string
# str1 = "my first string"
# print(str1)

# # indexing in strings
# str2 = 'my second string'
# print(f'0th elemet = {str2[0]}')

# # splicing in strings
# print(f'splicing 1 : {str1[1:6:2]}')
# print(f'splicing 2 : {str1[1::2]}')

# # 
# print(str1.__len__())

# # some string functions 
# print(f'index function : {str2.index(" ")}')
# print(f'title function : {str1.title()}')
# print(f'strip + title function : {str1.strip().title()}')
# print(f'isspace funciton  : {str1.isspace()}')

# ############################################################################################################################################

# # Using variables in strings
# fname = "sam"
# lname = "harris"

# # full_name = fname + lname
# full_name = f'{fname} {lname}'

# print(full_name.title())

# ############################################################################################################################################

# # user_name = input("enter you name : ")
# # print(f'Hello there, {user_name.title()}')
# ############################################################################################################################################

# # using some basic string formatting
# author_name = "Robert Shuller"
# quote = "Tough times never last, only Tough people do!"
# print(f'"{quote}"\n\t\t\t --{author_name}')
# ############################################################################################################################################

# # more stripping 
# another_name = "\tshubham mehetre      "
# print(another_name)
# print(f'now stripping spaces : {another_name.strip()}')
# ############################################################################################################################################

# # split(' ') will split the string with what argument is provided (space in this case). it will returns the items as a list

# full_name = "Shubham Anil Mehetre"

# print(full_name.split(' '))

# for i in full_name.split(" "):
#     print(i)
