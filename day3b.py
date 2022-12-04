letters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
with open("input3.txt", "r") as f:
    reader = f.read()
reader = reader.split("\n")
n = len(reader)
def common(l1,l2,l3):
    for e1 in l1:
        if e1 in l2:
            if e1 in l3:
                return letters.index(e1)
    return None 
s = 0
for i in range(0,n,3):
    s += common(reader[i],reader[i+1],reader[i+2])

print(s)