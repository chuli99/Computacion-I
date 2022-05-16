class University:
    def __init__(self,name = '',address = '',web = ''):
        self.__name = self.set_name(name)
        self.__address = self.set_address(address)
        self.__web = self.set_web(web)

    def __str__(self):
        return f"Name:{self.__name} -Address:{self.__address} -Link: {self.__web}"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        return name

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address
        return address

    def get_web(self):
        return self.__address

    def set_web(self, web):
        self.__web = web
        return web

    def show_university(self):
        return f"-Name:{self.name} -Surname:{self.address} -Link: {self.web}"



#university1 = University('Mendoza','Tirasos 1607','um.edu.com.ar')

#print(university1)