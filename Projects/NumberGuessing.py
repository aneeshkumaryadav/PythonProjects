import random

print("E for Easy")
print("M for Medium")
print("H for Hard")
print("X for Expert")
print("G for God")

difficulty = input("Enter The Difficulty Range : ").lower()
if(difficulty=="e"):
    computerGuess = random.randint(1,100)
elif(difficulty=="m"):
    computerGuess = random.randint(1,1000)
elif(difficulty=="h"):
    computerGuess = random.randint(1, 10000)
elif(difficulty=="x"):
    computerGuess = float(f"{random.uniform(1.00, 100.00):.2f}")
elif(difficulty=="g"):
    computerGuess = float(f"{random.uniform(1.0000, 100.0000):.4f}")
else:
    print("Please Enter Valid Character")
attemptCounter = 0
while(True):
    attemptCounter += 1
    user = input("Enter The Number : ")
    if difficulty=="x":
        if "." in user and len(user.split(".")[1]) > 2:
            print("Please Enter Number With Maximum 2 Decimal Places")
            continue
    elif difficulty=="g":
        if "." in user and len(user.split(".")[1]) > 4:
            print("Please Enter Number With Maximum 4 Decimal Places")
            continue
    userInput = float(user)

    if(computerGuess==userInput):
        print("Correct Guess")
        break
    elif(userInput > computerGuess):
        print("Your Number is Greater Than Expected. Please Enter Smaller Number")
    else:
        print("Your Number is Smaller Than Expected. Please Enter Greater Number")
print(f"Number of Attempt : {attemptCounter}")
