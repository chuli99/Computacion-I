#herencia
#heredar atributos de otras clases
#Clase madre
class Character:
    def __init__(self,name, last_name):
        self.name = name
        self.last_name = last_name
    def print_name(self):
        print(self.name, self.last_name)
class Elf(Character):
    #se aplica la sintaxis para que se pueda heredar esos metodos
    pass
pj = Elf("Elfo","Lopez")
pj.print_name()