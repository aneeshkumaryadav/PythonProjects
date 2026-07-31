import string, random

def passwordGenerator():
    asciiLetters = string.ascii_letters
    digits = string.digits
    punctuations = string.punctuation
    chars = asciiLetters + digits + punctuations
    password = ""
    while(len(password) < 8):
        password += random.choice(chars)

    return password

print(passwordGenerator())