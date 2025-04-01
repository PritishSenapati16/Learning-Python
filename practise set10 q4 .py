# Q4 --- Add a static method in problem 2 , to greet the user with hello.

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
        print(f"The squareroot is {self.n**0.5}")

    @staticmethod
    def hello():
        print("Hello") 
  
a = Calculator(6)
a.square()
a.cube()
a.squareroot()
a.hello()

print("End of program")
# signing off 