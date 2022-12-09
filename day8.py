with open("input8.txt", "r") as f:
    reader = f.read()
reader = reader.split("\n")

grid = []
valid_row = []
valid_col = []
valid = []
for line in reader:
    row = [int(x) for x in line]
    grid.append(row)
    r_zero =[False for x in line]
    valid_row.append(r_zero)
    c_zero = [False for x in line]
    valid_col.append(c_zero)
    zeros = [False for x in line]
    valid.append(zeros)

for a in grid:
    print(a)

x = len(reader[0])
y = len(reader)

borderx = [0,x-1]
bordery = [0, y-1]

for j in range(x):
    valid_row[0][j] = True
    valid_row[x-1][j] = True
    valid_col[0][j] = True
    valid_col[x-1][j] = True

for i in range(y):
    valid_col[i][0] = True 
    valid_col[i][y-1] = True
    valid_row[i][0] = True 
    valid_row[i][y-1] = True  

print(x,y)
def check(i, j, step, valid):
    if valid[i][j]:
        return True
    ix, iy = i + step[0], j + step[1]
    if grid[i][j] > grid[ix][iy]:
        if check(ix, iy, step, valid):
            valid[i][j] = True
            return True
        else:
            while (iy not in bordery) and (ix not in borderx):
                ix, iy = ix + step[0], iy + step[1]
               
                if grid[i][j] <= grid[ix][iy]:
                    return False 
               
            valid[i][j] = True
            return True 
    return False 



def valid_in_rows():
    step_right = (0,1)
    step_left = (0,-1)
    for i in range(1,x-1):
        for j in range(1, y-1):
            check(i, j, step_left, valid_row)
            check(i, j, step_right, valid_row)

def valid_in_cols():
    step_up = (1,0)
    step_down = (-1,0)
    for i in range(1, x-1):
        for j in range(1, y-1):
            check(i, j, step_down, valid_col)
            check(i, j, step_up, valid_col)
            

valid_in_rows()
valid_in_cols()

for i in range(x):
    for j in range(y):
        if valid_col[i][j] or valid_row[i][j]:
            valid[i][j] = True 
            

s = 0
for line in valid:
    print(line)
    for e in line:
        if e:
            s += 1
print(s)

