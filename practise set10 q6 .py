# Q6 --- Can u change the self parameter inside a class to something else (say "Harry"). Try changing self to "slf" or "harry" and see the effects.

# Ans ---
# signing in 
from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(harry,fro, to):
        print(f"Ticket is booked in train no: {harry.trainNo} from {fro} to {to}")

    def getStatus(self): 
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(333, 666)}")


t = Train(7654321)
t.book("Cuttack", "Puri")
t.getStatus()
t.getFare("Cuttack", "Puri")
# signing off'
