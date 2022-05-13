
import Codes.Banco.file as f

class Bank:
    def __init__(self):
        self.queue_1 = []
        self.queue_2 = []

    def add_user_queue(self,user,queue):
        if queue == 1:
            self.queue_1.append(str(user))
            with open(f.PATH_Q1, "a") as fd:
                fd.write(str(user))
        if queue == 2:
            self.queue_2.append(str(user))
            with open(f.PATH_2,"a") as fd:
                fd.write(str(user))