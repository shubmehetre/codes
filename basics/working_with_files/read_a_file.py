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
with open("txt_files/pi_digits.txt") as x:
    content = x.read()

print(content.strip())
