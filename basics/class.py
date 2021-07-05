# class Dog:
#     '''General model for dog things'''

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print(f"my dog's name is {name} and he is {age}")
#         print()

#     def sit(self):
#         print(f"{self.name} is now sitting")

#     def roll(self):
#         print(f"{self.name} is doing a rollver")

# my_dog = Dog("tommy", 5)
# my_dog.sit()
# my_dog.roll()

# print(Dog)
# ######################################################################
## 
# ## default values
# class Car:
#     '''general car info'''

#     def __init__(self, type, year) -> None:
#         self.type = type
#         self.year = year
#         self.milage = 50
#     def milage_indicator(self):
#         print(f"Milage is {self.milage}")

#     # we check if updated value is greater than current reading of milage  
#     def milage_updater(self, milage):
#         if milage > self.milage:
#             self.milage = milage
#             print(f"milage updated!!!")
#             print(f"new milage is : {milage}")
#         else:
#             print(f"You sabotaged with milage reading.\nYou are under arrest!!")

# my_car = Car('audi', 2021)
# my_car.milage_indicator()
# my_car.milage_updater(100)

# O/P
# Milage is 50
# milage updated!!!
# new milage is : 100

# my_car.milage_indicator()
# # Here milage is a default value invoked everytime we 
######################################################################
##
# INHERITANCE
# Parent
# class Car: 
#     def __init__(self,brand,type,year) -> None:
#         self.brand = brand
#         self.type = type
#         self.year = year

#     def print_details(self):
#         print(f"{self.brand} {self.type} {self.year}")

#     def goodbye(self):
#         print(f"ok go home now")
# ##CHild
# class Electric_Car(Car):
#     def __init__(self, brand, type, year) -> None:
#         super().__init__(brand, type, year)
#         self.battery = 80
    
#     def battery_capacity(self):
#         print(f"this car has battery of {self.battery} kWh")

#     ## Overring
#     def goodbye(self):
#         print("not goodbye")
#     ## Overloading
#     def goodbye(self, brand):
#         print(f"goodbye {brand}")

# my_car = Electric_Car("Tesla", "SUV", 2021)
# my_car.print_details()
# my_car.goodbye()

# O/P
# Tesla SUV 2021
# this car has battery of 80 kWh
#########################################################################
##
## Overloading

def product(a, b, c):
    p = a * b*c
    print(p)

def product(a, b):
    p = a * b
    print(p)
      



product(2,3)
product(10,2,3)