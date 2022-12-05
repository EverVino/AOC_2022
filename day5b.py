class Stack:
    def __init__(self):
        self.elems = []
    
    def pop(self):
        return self.elems.pop()
    
    def add(self, e):
        self.elems = [e]+ self.elems
    
    def adds(self, crate):
        self.elems = self.elems + crate

class Tower:
    def __init__(self):
        self.cols = []

    def move(self, ne, src, dest):
        #print("before", self.cols[src].elems, self.cols[dest].elems)
        crate = self.cols[src].elems[-ne:]
        #print(ne,src,dest, crate)
        self.cols[dest].adds(crate)
        self.cols[src].elems = self.cols[src].elems[:-ne]
        #print("after", self.cols[src].elems, self.cols[dest].elems)
    
    def add(self, e):
        self.cols.append(e)

with open("input5.txt", "r") as f:
    reader = f.read()

reader =  reader.split("\n")

for line in reader:
    if line[1] in "1234567890":
        break 
headers = line.split()
tower = Tower()
for e in headers:
    col = Stack()
    tower.add(col)
# 1 1  2 5  3 9  4 13
f = lambda x: x//4
n = len(reader[0])


for line in reader:
    if line[1] in "123456789":
        break
    for i in range(1,n,4):
        if line[i] != " ":
            tower.cols[f(i)].add(line[i])
            

for line in reader:
    if not line:
        continue
    if line[0] != "m":
        continue
    q, src, dest = [int(x) for x in line.split() if x.isnumeric()]
    tower.move(q,src-1,dest-1)

ans = ""
for e in tower.cols:
    a = e.elems.pop()
    ans += a 
print(ans)

