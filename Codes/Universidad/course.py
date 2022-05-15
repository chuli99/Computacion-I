class Course:
    def __init__(self, name='', code=0):
        self.__name = self.set_name(name)
        self.__code = self.set_code(code)

    def __str__(self):
        return f"Name:{self.__name} - Code:{self.__code}"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        return name

    def get_code(self):
        return self.__code

    def set_code(self,code):
        self.__code = code
        return code

course = Course('Algebra lineal',1)

print(course)