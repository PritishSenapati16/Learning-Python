# Q7 --- Write a program to find out the line number where python is present from Q6.

# Ans ---
# signing in

with open("sexy.txt")as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"Yes python is present.Line no:{lineno}")
        break
    lineno += 1
  

else:
    print("No python is present")  

print("End of program") 

# signing off