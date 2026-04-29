import string, random

chars = string.ascii_letters + string.digits + string.punctuation
password = ""
while(len(password) < 8):
    password += random.choice(chars)
print(password)