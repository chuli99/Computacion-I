class Client:
    def __init__(self,name = '',surname = '',dni = 0 ,state = 0, queue = 0):
        self.name = name
        self.surname = surname
        self.dni = dni
        self.state = state
        self.queue = queue

    def __str__(self):
        return f"Name:{self.name}-Surname:{self.surname}-Dni: {self.dni}-State:{self.state}"

    def show_user(self):
        return f"Name:{self.name}-Surname:{self.surname}-Dni: {self.dni}-State:{self.state}-queue = {self.queue}"

    def show_queue(self):
        return (self.queue)