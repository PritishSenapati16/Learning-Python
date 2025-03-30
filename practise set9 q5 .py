# Q5 --- Repeat the program 4 for a list of such words to be censored.

# Ans ---
# signing in

words = ["Donkey" , "Bad", "Good"]

with open ("cute.txt","r") as f:
    content = f.read()

for word in words:
    content = content.replace(word , "#" * len(word))

with open("cute.txt","w") as f:
    f.write(content)  
    
# signing off     