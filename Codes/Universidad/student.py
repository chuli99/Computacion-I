class Student:
    def __init__(self, name = '',surname ='', dni = 0, email = ''):
        self.__name = self.set_name(name)
        self.__surname = self.set_surname(surname)
        self.__dni = self.set_dni(dni)
        self.__email = self.set_email(email)
    def __str__(self):
        return f"Name:{self.__name} -Surname:{self.__surname} -Dni: {self.__dni}, Email: {self.__email}"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        return name

    def get_surname(self):
        return self.__address

    def set_surname(self, address):
        self.__address = address
        return address

    def get_dni(self):
        return self.__dni

    def set_dni(self, web):
        self.__web = web
        return web

    def get_email(self):
        return self.__email

    def set_email(self,email):
        self.__email = email
        return email

    def dni_verificator(self,documento):
        if documento == int(documento) and len(str(documento)) == 8:
                return "messi",str(documento)
        else:
            return "elbicho",str(documento)


#student1 = Student('Julian','Castillo', 42210213 ,'juliancastillo0399@gmail.com')

#print(student1)