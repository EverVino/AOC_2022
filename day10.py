with open("input10.txt", "r") as f:
    reader = f.read()

reader = reader.split("\n")
x = 1
X = []
s = 0
for line in reader:
    
    if line == "noop":
        X.append(x)
    else:
        i, n = [c for c in line.split()]
        n = int(n)
        nx = len(X)
        for _ in range(2):
            X.append(x)
        x += n 

V = [20, 60, 100, 140, 180, 220]

for v in V:
    s = s + v*X[v-1]
    print(v, X[v-1])
#print(X)
print(s)
    
