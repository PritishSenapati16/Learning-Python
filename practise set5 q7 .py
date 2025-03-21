# Q7 --- If the names of 2 friends are same; what will happen to the program in problem 6 ? 

# Ans --- 
# signing in
d = {}
name = input("enter the name")
lang = input("enter the language ")
d.update({name:lang})

name = input("enter the name")
lang = input("enter the language ")
d.update({name:lang})

name = input("enter the name")
lang = input("enter the language ")
d.update({name:lang})

name = input("enter the name")
lang = input("enter the language ")
d.update({name:lang})

print(d)
# signing off 

# It will be printed only one time if names of 2 friends are same and the language spoken by the same name at last will be printed .