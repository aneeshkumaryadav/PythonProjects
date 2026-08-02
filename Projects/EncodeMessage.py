import string
import random

def encoder(message: str, number: int) -> str:
    result = ""
    for char in message:
        if(char == " "):
            continue
        indexing = string.ascii_lowercase.index(char)
        indexing = (indexing+number)%26
        result += string.ascii_lowercase[indexing]

    return result

def decoder(message: str, number: int) -> str:
    result = ""
    for char in message:
        if(char == " "):
            continue
        indexing = string.ascii_lowercase.index(char)
        indexing = (indexing-number)%26
        result += string.ascii_lowercase[indexing]

    return result


message = input("Enter The Message : ").lower()
number = random.randint(1,26)

encodedMessage = encoder(message, number)
print(f"{encodedMessage}")
print(f"{decoder(encodedMessage, number)}")