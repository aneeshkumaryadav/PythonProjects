import random

print("R for Rock")
print("P for Paper")
print("S for Scissor")
print()

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
            print(f"Match Draw 😎 +1 Points To Each")
            print()

        elif((computerChoice=="r" and userInput=="p") or (computerChoice=="p" and userInput=="s") or computerChoice=="s" and userInput=="r"):
            userWinPoint += 1
            print(f"User Wins 😁 +1 Point To User")
            print()

        else:
            compWinPoint += 1
            print(f"Computer Wins 😒 +1 Point To Computer")
            print()

        numbersofGame -= 1
    else:
        print("Enter Valid Character")

print("*"*5, "RESULT TABLE", "*"*5)
print(f"User : {userWinPoint}")
print(f"Computer : {compWinPoint}")
print("*"*24)
print()

if(compWinPoint > userWinPoint):
    print(f"Computer Wins 😒 with {abs(compWinPoint - userWinPoint)} Points")

elif(compWinPoint == userWinPoint):
    print(f"Match Draw 😎 with 0 Points")

else:
    print(f"User Wins 😁 with {abs(userWinPoint - compWinPoint)} Points")