#Si, eran dos Clases Alumno y Curso. Alumno tiene nombre, edad y nota. Se tiene que saber
# si alumno está aprobado o desaprobado y Son dos curso,
# con una lista alumno, con cuatro alumnos cada uno
class Student:
    def __init__(self,name,age,mark):
        self.__name = name
        self.__age = age
        self.__mark = mark
    def __str__(self):
        return f"Nombre: {self.__name} - Edad: {self.__age} - Calificación: {self.__mark}"
    def set_age(self, age):
        self.__age = age
    def set_mark(self , mark):
        self.__mark = mark
    def get_name(self):
        return self.__name
    def get_age(self):
        if self.__age < 0:
            alert = ("Edad inexsistente")
            return (alert)
        else:
            return self.__age
    def get_mark(self):
        if self.__mark < 7:
            return "DESAPROBADO"
        else:
            return "APROBADO"
class Classroom:
    def __init__(self):
        self.list = []
    def add_student(self,student):
        self.list.append(student)
    def remove_student(self,student):
        self.list.remove(student)
    def get_list(self):
        for i in range(len(self.list)):
            print(self.list[i])

student1 = Student("Eva",20,8)
student2 = Student("Cristian",24,4)
student3 = Student("Angel",19,8)
student4 = Student("Julián",21,7)
student5 = Student("Lionel",27,10)
student6 = Student("Paulo",21,6)
student7 = Student("Martin",29,9)
student8 = Student("Juan Roman",31,10)

print(student6.get_age())
print(student1.get_mark())

classA = Classroom()
classB = Classroom()

classA.add_student(student1)
classA.add_student(student2)
classA.add_student(student3)
classA.add_student(student4)
classB.add_student(student5)
classB.add_student(student6)
classB.add_student(student7)
classB.add_student(student8)

print(classA.get_list())



