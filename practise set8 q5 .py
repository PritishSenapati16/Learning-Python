# Q5 --- Write a python function to print first n lines of the following pattern:
'''
***
**       for n = 3
*
'''

# Ans ---
# signing in 
def pattern(n):
    if(n==0):
        return 
    print("*" * n)
    pattern(n-1)

pattern(0)
# signing off  