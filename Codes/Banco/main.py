from http import client
from client import Client
from bank import Bank
import const 
#print("MENU")
#print("Ingrese:")
#print("1- Empleado")
#print("2- Cliente")
#choice1 = int(input(''))


#user1 = Client('Julian','Castillo',42210213,0,1)
#user2 = Client('German','Castillo',50203402,0,2)
#user3 = Client('Alexis','Lino',43029290,0,1)
#user4 = Client('Nicolas','Mayoral',43093093,0,2)


while True:
    print(const.MENU)
    option = int(input(""))
    if option == 1:
        print(const.NAME_INPUT)
        name = str(input(''))
        print(const.LAST_NAME_INPUT)
        surname = str(input(''))
        print(const.IND_INPUT)
        id_number = int(input(''))
        print(const.STATE_INPUT)
        state = int(input(''))
        print(user.show_user())
        user = Client(name,surname,id_number,state,queue)
        #state = int(input(STATE_INPUT))
    if option == 2:
        print(const.QUEUE_INPUT)
        queue = int(input(''))

#print(user2.show_user())
#print(user3.show_user())
#print(user4.show_user())

#print(user1)

#list_q1 = Bank()
#list_q2 = Bank()

#list_q1.add_user_queue(user1.show_user(),user1.show_queue())
#list_q2.add_user_queue(user2.show_user(),user2.show_queue())
#list_q1.add_user_queue(user3.show_user(),user3.show_queue())
#list_q2.add_user_queue(user4.show_user(),user4.show_queue())

#print(list_q1.get_q1())
#print(list_q2.get_q2())
