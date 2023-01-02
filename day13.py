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

    while True:
        if len(left)==0:
            return True 
        if len(right) == 0:
            return False 
        a, b = left.pop(0), right.pop(0)
        if a == b:
            continue 
        return check_order(a,b)

c = 1
s = 0
for a,b in lista:
    left = eval(a)
    right = eval(b)
    if check_order(left,right):
        s = s + c
    c = c+1
print(s)
#print(check_order([1,1,3,1,1],[1,1,5,1,1]))
