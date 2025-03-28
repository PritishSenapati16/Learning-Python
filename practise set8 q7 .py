# Q7 --- Write a python function to remove a given word from a list ad strip it at the same time .

# Ans ---
# signing in 
def rem(l, word):
    n = []
    for item in l:
        if not(item == word): 
            n.append(item.strip(word)) 
    return n     
        
l = ["Harry", "Rohan", "Shubham", "an"] 
print(rem(l, "an"))
# signing off