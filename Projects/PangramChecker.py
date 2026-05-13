import string

def checkPangram(sentence : str) -> str:
    for char in sentence:
        if(char == " "):
            continue
        if(char not in alphabets):
            return f"Not Pangram"
        else:
            return f"Pangram"
        
alphabets = set(string.ascii_lowercase)
sentence = input("Enter The Sentence : ").lower()
sentence = set(sentence)
print(checkPangram(sentence))