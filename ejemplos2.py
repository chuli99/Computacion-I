class User:
    #CONSTRUCTOR DE UNA CLASE
    def __init__(self,name,age):
        self.__name = self.set_name(name)
        self.__age = self.set_age(age)
    #No tiene parametros o atributos porque la vamos a usar para devolver el valor de name
    def get_name(self):
        return self.__name
    #Set es para darle un valor a ese get.
    def set_name(self,name):
        return name
    def get_age(self):
        return self.__age    
    def set_age(self,age):
        if age <= 0:
            print("Edad no disponible")
        else:
            return age
user1 = User("Juan Carlos", 38)
print(user1.get_age())