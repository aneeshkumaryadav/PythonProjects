import string, random
def passwordValidator(password : str):
    upperCase = lowerCase = digit = special = 0
    for char in password:
        if(char.isupper()): upperCase+=1
        elif(char.islower()): lowerCase+=1
        elif(char.isdecimal()): digit+=1
        else: special+=1
    if(((upperCase>=1 and lowerCase>=1) and (digit>=1 and special>=1)) and len(password) >= 8):
        return f"Strong"
    else:
        return f"Weak"
# print(passwordValidator("eLm@18&Bs"))
chars = string.ascii_letters + string.digits + string.punctuation
password = ""
size = int(input("Enter The Size of Password : "))
while(len(password) < size):
    password += random.choice(chars)
print(password)
print(passwordValidator(password))