p1 = "ABC"
p2 = "XYZ"
winnerb = {1:3,2:1,3:2}


def get_score(a,b):
    a = p1.index(a)+1
    b = p2.index(b)+1
    print(a,b)
    if a == b:
        return 3
    if winnerb[b] == a:
        return 6
    else:
        return 0

with open("input2.txt", "r") as f:
    reader = f.readlines()

# with open("input2.txt", "r") as f:
#     reader = f.readlines()
s = 0
for line in reader:
    a, b = [x for x in line.split()]
    s = s + get_score(a,b)+p2.index(b)+1

print(s)