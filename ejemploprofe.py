class Team:
    def __init__(self):
        self.team_list = []
        self.team_list2 = []

    #metodo encargado de agregar usuarios al la lista del team
    def add_user_to_team(self, user):
        self.team_list.append(user)
    def add_user_to_team2(self, user):
        self.team_list2.append(user)

class User:
    def __init__(self, name = "", age = 0):
        self.__name = name
        self.__age = self.set_age(age)

    def __str__(self):
        return f"Name: {self.__name} Age: {self.__age}"

    def get_age(self):
        return self.__age
    def set_age(self, age):
        #logica para setear la edad
        self.__age = age
        return age

    def get_name(self):
        return self.__name
user_1 = User("Jose",36)
user_2 = User("Maria",23)
user_3 = User("Pablo",28)
user_4 = User("Juana",21)
user_5 = User("Valentina",19)
user_6 = User("Nicolas",20)
user_7 = User("Alexis", 20)
user_8 = User("Facundo",19)

file_team = open("file.txt","w")
team_thunder = Team()


file_team.write("Team 1 \n")
file_team.write(str(user_1))
file_team.write("\n")
team_thunder.add_user_to_team(user_1)
print(team_thunder.team_list[0])

file_team.write(str(user_2))
file_team.write("\n")
team_thunder.add_user_to_team(user_2)
print(team_thunder.team_list[1])

file_team.write(str(user_3))
file_team.write("\n")
team_thunder.add_user_to_team(user_3)
print(team_thunder.team_list[2])

file_team.write(str(user_4))
file_team.write("\n")
team_thunder.add_user_to_team(user_4)
print(team_thunder.team_list[3])

print("TEAM 2:")
file_team.write("TEAM 2 \n")
file_team.write(str(user_5))
file_team.write("\n")
team_thunder.add_user_to_team(user_5)
print(team_thunder.team_list[4])

file_team.write(str(user_6))
file_team.write("\n")
team_thunder.add_user_to_team(user_6)
print(team_thunder.team_list[5])

file_team.write(str(user_7))
file_team.write("\n")
team_thunder.add_user_to_team(user_7)
print(team_thunder.team_list[6])

file_team.write(str(user_8))
file_team.write("\n")
team_thunder.add_user_to_team(user_8)
print(team_thunder.team_list[7])
