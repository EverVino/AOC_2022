with open("input3.txt", "r") as f:
    reader = f.read()
reader = reader.split("\n")

letters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = 0
ans = []
for line in reader:
    n = len(line)
    p1 = line[:n//2]
    p2 = line[n//2:]
    
    for p in p1:
        if p in p2:
            ans.append(p)
            break 
    
    s = s + letters.index(p)

print(s)
print(ans)


# print()
# print(chr(97))
# print(chr(122))
# print(chr(65))
# print(chr(90))
# a ==97,122