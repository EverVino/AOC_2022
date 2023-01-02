from math import inf

def get_n(v, grid):
    i, j = v
    nei = set()
    nx, ny = len(grid), len(grid[0])
    posible = [(i,j+1), (i,j-1), (i+1,j), (i-1,j)]
    
    for x, y in posible:
        if x not in [-1, nx] and y not in [-1, ny]:
            r = grid[x][y] - grid[i][j]
            if  r <2:
                nei.add((x,y))
    
    return nei


def min_path(start, grid, end_value):
    
    queue = [start]
    explored = {start}
    d = dict()
    d[start] = 0
    while queue:
        v = queue.pop(0)
        for w in get_n(v,grid):
            x,y = w
            
            if w not in explored:
                explored.add(w)
                queue.append(w)
                d[w] = d[v]+1
            if grid[x][y] == end_value:
                print(d[w])
                return True

    return False       
    
with open("input12.txt", "r") as f:
    reader =  f.read()


reader = reader.split("\n")
letras = "SabcdefghijklmnopqrstuvwxyzE"
mapa = []

for index, line in enumerate(reader):
    row = []
    for x in line:
        n = letras.index(x)
        if n == 0:
            start = (index, len(row))
        if n == 27:
            end_line =(index, len(row))
        row.append(n)
    mapa.append(row)

# for a in mapa:
#     print(a)
print(start)
print(end_line)

ans = min_path(start, mapa, 27)
print(ans)

# test = [(0,0), (1,0), (3,0), (2,2), (4,3), (4,4), (3,7),]

# for x0, y0 in test:
#     lista = get_n(x0,y0, mapa)
#     print(mapa[x0][y0], lista)

# ordered = sorted(min_paths,key=lambda x: len(x))

# print(len(ordered[0]))
# nx, ny = len(mapa), len(mapa[0])

# pantalla = [[0 for _i in range(ny)] for _j in range(nx)]

# c = 0
# for x,y in ordered[0]:
#     pantalla[x][y] = c
#     c += 1

# for a in pantalla:
#     print(a)
