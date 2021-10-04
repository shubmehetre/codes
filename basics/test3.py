# print("Enter 'q' at any time to quit.")
# while True:
#     first = input("\nPlease give me a first name: ")
#     if first == 'q':
#         break
#     last = input("Please give me a last name: ")
#     if last == 'q':
#         break
###################################################################################
bin_data ='0001001010110110'

str_data =' '

# slicing the input and converting it
# in decimal and then converting it in string
for i in range(0, len(bin_data), 7):

    print(i)
    print(bin_data[i])

    # slicing the bin_data from index range [0, 6]
    # and storing it as integer in temp_data
    temp_data = int(bin_data[i:i + 7])
