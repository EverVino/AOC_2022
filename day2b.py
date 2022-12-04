p1 = "ABC"
p2 = "XYZ"

get_scoreb = {
    "A":{"X":3, "Y":1, "Z":2},
    "B":{"X":1, "Y":2, "Z":3},
    "C":{"X":2, "Y":3, "Z":1}
    }

# with open("input2.txt", "r") as f:
#     reader = f.readlines()

with open("test2.txt", "r") as f:
    reader = f.readlines()

s = 0
for line in reader:
    a, b = [x for x in line.split()]
    s = s + get_scoreb[a][b]+p2.index(b)*3

print(s)