import string, random
def passwordValidator(password : str) -> str:
    upperCase = lowerCase = digit = special = 0
    for char in password:
        if(char.isupper()): upperCase+=1
        elif(char.islower()): lowerCase+=1
        elif(char.isdecimal()): digit+=1
        else: special+=1

    if(((upperCase<=2 or lowerCase<=2) and (digit>=2 or special>=2)) and (len(password) < 12 and len(password) >= 8)):
        return f"Medium"

    if(((upperCase>3 or lowerCase>3) or (digit>2 and special>3)) and len(password) >= 12):
        return f"Strong"
    
    else:
        return f"Weak"

def autoInput():
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ""
    size = int(input("Enter The Size of Password : "))
    while(len(password) < size):
        password += random.choice(chars)
    print(password)
    print(passwordValidator(password))

userpass = input("Enter The Password : ")
if userpass == "":
    autoInput()
else:
    print(passwordValidator(userpass))