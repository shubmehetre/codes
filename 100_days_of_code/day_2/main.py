# This is day 2

print("Wecome!\nThis is a simple tip calculator\n")

tot_bill = int(float(input("what was the total bill:  $")))
num_of_ppl = int(input("how many people are splitting this bill?  "))

# user shud enter valid values for tip percent
while True:
    tip_percent = int(input("what percent of tip you want to give: 10, 12, 15?  "))
    if tip_percent in (10,12,15):
        tip = (tot_bill * tip_percent) / 100
        result = (tot_bill + tip) / num_of_ppl
        break
    else:
        print("INVALID! Tip can be 10, 12 or  15 percent")

print(f"Each person should pay: {result:.2f}")
