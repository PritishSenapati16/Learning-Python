# Q1 --- Write a program using functions to find greatest of three numbers.

# Ans --- 
# signing in 
a = 1
b = 2 
c = 5

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    
    elif(b>a and b>c):
        return b
    
    elif(c>a and c>b):
        return c
    
print(greatest(a,b,c))
# signing off