character = 0

with open('file.txt', 'r') as f:
    contents = f.read()
    for char in contents:
        character +=1

print(character)


