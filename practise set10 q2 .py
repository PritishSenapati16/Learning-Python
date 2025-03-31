# Q2 --- Write a class"calculator" capable of finding square , cube and square root of a number.

# Ans ---
# signing in 
class Calculator :
    def __init__(self,n):
        self.n = n 

    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The square is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The square is {self.n**0.5}")

    
a = Calculator(6)
a.square()
a.cube()
a.squareroot()

print("End of program")
# signing off 




    