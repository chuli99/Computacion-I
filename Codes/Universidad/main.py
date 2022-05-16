from university import University
from student import Student
from course import Course
from inscription import Inscription
from career import career

University1 = University('Universidad de Mendoza', 'Espana 1390', 'www.um.edu.ar')
print(University1)
student1 = Student('Julian','Castillo', 42210213 ,'juliancastillo0399@gmail.com')

print(student1.dni_verificator(student1.get_dni()))
