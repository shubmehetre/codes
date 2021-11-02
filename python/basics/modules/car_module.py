class Car:
    '''general car info'''

    def __init__(self,brand, type, year) -> None:
        self.type = type
        self.year = year
        self.milage = 50
        self.brand = brand
    def milage_indicator(self):
        print(f"Milage is {self.milage}")

    # we check if updated value is greater than current reading of milage
    def milage_updater(self, milage):
        if milage > self.milage:
            self.milage = milage
            print(f"milage updated!!!")
            print(f"new milage is : {milage}")
        else:
            print(f"You sabotaged with milage reading.\nYou are under arrest!!")

    def print_details(self):
        print(f"{self.brand} {self.type} {self.year}")

    def gas_capacity(self):
        print("lot of capacity")
