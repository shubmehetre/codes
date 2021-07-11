import json

class CreateUser:
    def __init__(self,filename):
        self.filename = filename

    def new_user(self):
        name = input("Enter name : ")
        with open(self.filename, 'w') as f:
            json.dump(name,f)
        return name


class GreetUser:
    def __init__(self, filename):
        self.filename = filename

    def greet_existing_user(self):
        try:
            with open(self.filename) as f:
                name = json.load(f)
        except FileNotFoundError:
            return None
        else:
            return name
