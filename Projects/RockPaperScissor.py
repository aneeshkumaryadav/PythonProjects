import random

print("R for Rock")
print("P for Paper")
print("S for Scissor")

compWinPoint = 0
userWinPoint = 0

numbersofGame = int(input("How Many Time You Wanna Play : "))
while(numbersofGame > 0):
    gameList = ["r","p","s"]
    computerChoice = random.choice(gameList)

    userInput = input("Enter The Choice : ").lower()
    if(userInput == "r" or userInput == "p" or userInput == "s"):
        if(computerChoice==userInput):
            compWinPoint += 1
            userWinPoint += 1

        elif((computerChoice=="r" and userInput=="p") or (computerChoice=="p" and userInput=="s") or computerChoice=="s" and userInput=="r"):
            userWinPoint += 1

        else:
            compWinPoint += 1
        numbersofGame -= 1
    else:
        print("Enter Valid Character")
    
if(compWinPoint > userWinPoint):
    print(f"Computer Wins 😒 with {compWinPoint} Points")

elif(compWinPoint == userWinPoint):
    print(f"Match Draw 😎 with {compWinPoint} Points")

else:
    print(f"User Wins 😁 with {userWinPoint} Points")