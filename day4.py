with open("input4.txt","r") as f:
    reader = f.read()
reader = reader.split("\n")
s = 0
for line in reader:
    data = line.split(",")
    dA = [int(x) for x in data[0].split("-")]
    dB = [int(x) for x in data[1].split("-")]
    
    A = set(range(dA[0],dA[1]+1))
    B = set(range(dB[0],dB[1]+1))
    
    if len(A & B) >= len(A) or len(A & B) >= len(B) :
        print(len(A&B),len(A),len(B))
        s += 1

print(s) 