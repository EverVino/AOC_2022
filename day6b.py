with open("input6.txt", "r") as f:
    reader = f.read()

code = []
for index, letter in enumerate(reader):
    print(index,letter,letter in code)
    while letter in code:
        code.pop(0)
    code.append(letter)

    if len(code) == 14:
        break


print(index+1)
    