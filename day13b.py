with open("input13.txt", "r") as f:
    reader = f.read()

reader = reader.split("\n\n")
lista = [block.strip().split("\n") for block in reader]

def check_order(left, right):
    if type(left) == int and type(right) == int:
        return left<right
    if type(left) == int:
        left = [left]
    if type(right) == int:
        right = [right]
    left = left[:]
    right = right[:]
    while True:
        if len(left)==0:
            return True 
        if len(right) == 0:
            return False 
        a, b = left.pop(0), right.pop(0)
        if a == b:
            continue 
        return check_order(a,b)
def partition(A,l,r):
    p = A[l]
    i = l+1
    for j in range(l+1,r+1):
        #$if A[j]<p:
        if check_order(A[j].copy(),p.copy()):
            A[j], A[i] = A[i], A[j]
            i = i+1
    A[l], A[i-1] = A[i-1], A[l]
    return i-1
def sorting(A,l,r):
    if l>r:
        return
    i = 0
    j = partition(A,l,r)
    sorting(A,l,j-1)
    sorting(A,j+1,r)

un = []
for a, b in lista:
    left = eval(a)
    right = eval(b)
    un.append(left)
    un.append(right)
un.append([[2]])
un.append([[6]])
sorting(un, l=0, r=len(un)-1)
p=1
for i, e in enumerate(un):
    if e == [[2]]:
        print(i)
        p = p*(i+1)
    if e == [[6]]:
        p = p*(i+1)
        print(i)
        break
for i, a in enumerate(un):
    print(i, a)

