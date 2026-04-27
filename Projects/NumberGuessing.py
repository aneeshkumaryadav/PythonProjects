import random

print("E for Easy")
print("M for Medium")
print("H for Hard")
difficulty = input("Enter The Difficulty Range : ").lower()
if(difficulty=="e"):
    computerGuess = random.randint(1,100)
elif(difficulty=="m"):
    computerGuess = random.randint(1,1000)
elif(difficulty=="h"):
    computerGuess = random.randint(1, 10000)
else:
    print("Please Enter Valid Character")
attemptCounter = 0
while(True):
    userInput = int(input("Enter The Number : "))
    if(computerGuess==userInput):
        attemptCounter += 1
        print("Correct Guess")
        break
    elif(userInput > computerGuess):
        attemptCounter += 1
        print("Your Number is Greater Than Expected. Please Enter Smaller Number")
    else:
        attemptCounter += 1
        print("Your Number is Smaller Than Expected. Please Enter Greater Number")
print(f"Number of Attempt : {attemptCounter}")
