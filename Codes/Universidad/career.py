class Student:
    def __init__(self, name = '',description =''):
        self.__name = self.set_name(name)
        self.__description = self.set_description(description)
        self.list_courses = []
        self.list_students = []
        self.list_universities = []

    def __str__(self):
        return f"Name:{self.__name} - Description:{self.__description}"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        return name

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description
        return description

    def add_courses(self,course):
        self.list_courses.append(course)

    def add_students(self,student):
        self.list_students.append(student)

    def add_universities(self,university):
        self.list_universities.append(university)

career = Student('Ingenieria en Informatica' ,'Ciencia que estudia la rama de la informatica')

