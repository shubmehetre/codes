# Python3 code to demonstrate working of Converting binary to string
# Using BinarytoDecimal(binary)+chr()

# Defining BinarytoDecimal() function
def BinaryToDecimal(b_num):
    '''binary to decimal converter function'''
    decimal = 0
    b_num = list(b_num)   # Converting binary num into a list
    for i in range(len(b_num)):
        pop_num = b_num.pop()   # we can now use pop method to the list
        if pop_num == '1':   # ignoring the 0s
            decimal = decimal + pow(2,i)
    return decimal


x = input("Enter a binary num: ")
ans = (BinaryToDecimal(x))
print(ans)
# print(f"answer is {ans}")
