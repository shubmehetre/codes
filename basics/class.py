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
    
#     def gas_capacity(self):
#         print("lot of capacity")
# ##CHild
# class Electric_Car(Car):
#     def __init__(self, brand, type, year) -> None:
#         super().__init__(brand, type, year)
#         self.battery = 80
    
#     # overriding
#     def gas_capacity(self):
#         print("this is an electric vehicle")

#     # def battery_capacity(self):
#     #     print(f"this car has battery of {self.battery} kWh")

# my_car = Electric_Car("Tesla", "SUV", 2021)
# my_car.print_details()
# my_car.gas_capacity()
# my_car.goodbye()

# O/P
# Tesla SUV 2021
# this is an electric vehicle
#########################################################################
##
## Overloading

# def product(a, b, c):
#     p = a * b*c
#     print(p)

# def product(a, b):
#     p = a * b
#     print(p)
      



# product(2,3)
# product(10,2,3)
#########################################################################
##
## Making an instance of Class, an attribute
# class Car: 
#     def __init__(self,brand,type,year) -> None:
#         self.brand = brand
#         self.type = type
#         self.year = year

#     def print_details(self):
#         print(f"{self.brand} {self.type} {self.year}")

# class Battery:
#     def __init__(self, size=75) -> None:
#         '''init for Battery. we defined a battery size attribute in it. It has a default value as 75'''
#         self.battery_size = size

#     def tell_battery_size(self):
#         print(f'Battery size of this car is {self.battery_size}-kWh')
    
#     def tell_range(self):
#         if self.battery_size == 75:
#             print(f"This car can go 200 kms")
#         elif self.battery_size == 100:
#             print(f"This car can go 300 kms")
#         else:
#             print(f"pls enter correct battery info")
    
#     def upgrade_battery(self):
#         if self.battery_size:
#             self.battery_size = 100
            


# class Electric_Car(Car):
#     def __init__(self, brand, type, year) -> None:
#         super().__init__(brand, type, year)
#         self.battery = Battery()

# my_car = Electric_Car("Tesla", "Model-S", 2020)
# my_car.print_details()
# my_car.battery.tell_battery_size()
# # my_car.battery.tell_range()
# print("\nincresing battery size now ...\n")
# my_car.battery.upgrade_battery()
# my_car.battery.tell_battery_size()

# O/P
# Tesla Model-S 2020
# Battery size of this car is 100-kWh
# This car can go 300 kms

##############################################################################################################################
##
## tring import

# from modules.car_module import Car
# import modules.car_module

# # Creating a object from imported Car class from module car_module
# my_car = car_module.Car("Tesla", "Model T", 2020)

# # directly importing module without mentioning class, we need to explicitly specify module.class
# my_car = modules.car_module.Car("Tesla", "Model T", 2020)

# testing
# my_car.print_details()
# my_car.gas_capacity()


# O/P
# Tesla Model T 2020
# lot of capacity
#############################################################################################################################
# ##
# ## Standard Library
# import math
# import random
# import time

# list1 = [1,2,3,4,5,6,7,8,9]
# print(f"{list1}\n Shuffling the list ...")
# random.shuffle(list1)
# time.sleep(2)
# print(f"{list1}\n... Et voila!")


# x = math.sqrt(166)
# print(f"\nsquare root : {x:.2f}")

# # O/P
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
#  Shuffling the list ...
# [2, 9, 6, 1, 8, 5, 7, 3, 4]
# ... Et voila!

# square root : 12.88

list1 = [1,2,3,]
dict1 = {"name": "shubham", "location": "Miami"}

class Car:
    def __init__(self, name,year):
        self.name = name
        self.year = year
    
    def print_info(self):
        print(f"Car is : {self.name} from {self.year}")


mycar = Car("Tesla", 2020)

mycar.print_info()






















