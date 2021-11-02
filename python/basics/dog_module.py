class Dog:
    '''General model for dog things'''

    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f"my dog's name is {name} and he is {age}")
        print()

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll(self):
        print(f"{self.name} is doing a rollver")

