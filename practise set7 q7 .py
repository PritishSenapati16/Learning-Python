# Q7 --- Write a program to print the following star pattern.
'''
  *
 ***
***** for n = 3
'''

# Ans --- 
# signing in
n = int(input("enter a number:"))
for i in range(1, n+1):
    print(" "* (n-i), end="")
    print("*"* (2*i-1), end = "")
    print("")
# signing off

