# Q4 --- A file contains a word "Donkey"multiple times.You need to write a program which replace this word by Parimal by updating the same file.

# Ans ---
# signing in 
word = "Donkey"

with open ("Donkey.txt","r") as f:
    content = f.read()

contentNew = content.replace(word , "Parimal")

with open("Donkey.txt","w") as f:
    f.write(contentNew)

# signing off 