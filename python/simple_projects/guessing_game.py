# Guessing game
##
import random

magic_num = random.randrange(0, 10)
print(magic_num)
tries = 2

while tries >= 0:
    tries -= 1
    user_choice = int(input("Enter number between 0 - 10 : "))
    if (user_choice == magic_num):
        print("You WON!!!")
        break
    else:
        if (magic_num > 5):
            print("Number is between 5 and 10")
        else:
            print("Number is between 0 and 5")
        print(f"Try again. {tries+1} try left")
        if ()
print("YOU LOSE")
###########################################################################
