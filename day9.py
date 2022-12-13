class Tail:
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.passed = set()
        self.passed.add((self.x, self.y))
    
    def get_n(self, i, j):
        return [(x,y) for x in range(i-1,i+2) for y in range(j-1,j+2)]
    
    def add(self, P):
        self.passed.add(P)
    
    def followH(self, H):
        if (self.x, self.y) in self.get_n(H.x, H.y):
            return
        if self.x == H.x or self.y == H.y:
            self.y = round((H.y+self.y)/2)
            self.x = round((H.x+self.x)/2)
        else:
            x = round((H.x-self.x)/abs(H.x-self.x))
            y = round((H.y-self.y)/abs(H.y-self.y))
            self.x += x 
            self.y += y
        self.add((self.x, self.y))
    
    def __str__(self):
        return f"La posición de la cola es ({self.x},{self.y})"

class Head:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def moving(self, move):
        self.x += move[0]
        self.y += move[1]
    
    def __str__(self):
        return f"La posición de la cabeza es ({self.x},{self.y})"

T = Tail()
H = Head()
with open("input9.txt", "r") as f:
    reader = f.read()

reader = reader.split("\n")
key_move = {"R": (1,0), "L": (-1,0), "U": (0,1), "D": (0,-1)}
for line in reader:
    k, n = [x for x in line.split()]
    n = int(n)
    move = key_move[k]
    for _ in range(n):
        H.moving(move)
        T.followH(H)
print(T)
print(H)
print(T.passed, len(T.passed))