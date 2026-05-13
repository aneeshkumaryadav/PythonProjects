import string

message = input("Enter The Message : ").lower()
result = ""
for char in message:
    if(char == " "):
        continue
    indexing = string.ascii_lowercase.index(char)
    indexing = (indexing+3)%26
    result += string.ascii_lowercase[indexing]
print(result)