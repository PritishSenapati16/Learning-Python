# Q8 --- Write a program to make a copy of a text file"this.txt".

# Ans ---
# signing in 
with open("this.txt") as f:
    content = f.read()

with open("this_copy.txt", "w") as f:
    f.write(content)
# signing off 