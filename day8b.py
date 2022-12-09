with open("input8.txt", "r") as f:
    reader = f.read()
reader = reader.split("\n")

grid = []

for line in reader:
    row = [int(x) for x in line]
    grid.append(row)
   
x, y = len(reader[0]), len(reader)

borderx = [0, x-1]
bordery = [0, y-1]

def sum_rc(i, j, step):
    ix, iy = i, j 
    s = 0
    while ix not in borderx and iy not in bordery:
        ix, iy = ix + step[0], iy + step[1]
        if grid[i][j] <= grid[ix][iy]:
            s += 1
            break 
        s += 1
    return s 

def get_score(i, j, grid):
    p = 1
    steps = [(0,1), (0,-1), (1,0), (-1,0)]
    for step in steps:
        p = sum_rc(i,j,step)*p 
    return p
score = 0
for i in range(1, x-1):
    for j in range(1, y-1):
        new_score = get_score(i,j, grid)
        if new_score > score:
            score = new_score 
print(score)   