# Q2 --- The game()function in a program lets a user play a game and returns the score as an integer.You need to read a file 'HI - score.txt'which is either blank or contains the previous Hi - score. You need write a program to update the HI-score whenever the game () function breaks the Hi - score.

# Ans --- 
# signing in 
import random 

def game():
    print("You are playing the game...")
    score = random.randint(1, 62)
    # Fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)

        else:
            hiscore = 0

    print(f"Your score:{score}")
    if(score>hiscore):
        # write this hiscore to the file
        with open("hiscore.txt","w") as f:
            f.write(str(hiscore))

    return score

game()
# signing off 