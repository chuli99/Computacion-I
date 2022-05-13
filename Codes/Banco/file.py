import os

PATH_1 = r'C:\Users\julia\PycharmProjects\Computacion-I\Codes\Banco\queue1.txt'
PATH_2 = r'C:\Users\julia\PycharmProjects\Computacion-I\Codes\Banco\queue2.txt'

if os.path.exists(PATH_1) and os.path.exists(PATH_2):
    pass
elif not os.path.exists(PATH_1) and not os.path.exists(PATH_2):
    fd_1 = open(PATH_1)
    fd_2 = open(PATH_2)
    fd_1.close()
    fd_2.close()

