class Client:
    def __init__(self,name = '',surname = '',dni = 0 ,state = 0, queue = 0):
        self.__name = self.set_name(name)
        self.__surname = self.set_surname(surname)
        self.__dni = dni
        self.__state = state
        self.__queue = queue


    def set_name(self, name):
        self.__name = name
        return name

    def set_surname(self,surname):
        self.__surname = surname
        return surname

    def set_dni(self,dni):
        self.__dni = dni
        return dni

    def __str__(self):
        return f"Name:{self.name}-Surname:{self.surname}-Dni: {self.dni}-State:{self.state}"

    def show_user(self):
        return f"Name:{self.__name}-Surname:{self.__surname}-Dni: {self.__dni}"

    def show_queue(self):
        return (self.queue)