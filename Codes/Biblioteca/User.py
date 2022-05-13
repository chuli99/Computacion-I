
class User:
    def __init__(self,name = '',age = 0,address = ''):
        self.name = name
        self.age = age
        self.address = address
    #Formato

    def __str__(self):
        return f"Name:{self.name} - Age:{self.age} - Address:{self.address}"

    def view_user(self):
        return f"Name:{self.name} - Age:{self.age} - Address:{self.address}"

    def view_name(self):
        return f"{self.name}"