# Q1 -- Create a class (2-D vector) and use it to create another class representing 3D vector.

# Ans ---
# Signing in 
class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The Vector is {self.i}i + {self.j}j")


class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k =+ k

    def show(self):
        print(f"The Vector is {self.i}i + {self.j}j + {self.k}k")


x = TwoDVector(3, 4)
x.show()

y = ThreeDVector(3, 4, 6)
y.show()
print("END OF THE PROGRAM")
# Signing off
   