with open("input10.txt", "r") as f:
    reader = f.read()

reader = reader.split("\n")
x = 1
X = []
s = 0

sprite = ["." for _ in range(40)]
sprite[0:3] = ["#", "#", "#"]
#print("".join(sprite))
index = 0
cadena = ""
for line in reader:

    if line == "noop":
        X.append(x)
        cadena += sprite[index]
        
        # print(cadena)
        index += 1
        if index == 40:
                index = 0
                # sprite = ["." for _ in range(40)]
                # sprite[0:3] = ["#", "#", "#"]
    else:
        i, n = [c for c in line.split()]
        n = int(n)
        nx = len(X)
        for _ in range(2):
           
            X.append(x)
            cadena += sprite[index]
            index += 1
            if index == 40:
                index = 0
                # sprite = ["." for _ in range(40)]
                # sprite[0:3] = ["#", "#", "#"]
        sprite = ["." for _ in range(40)]
        x += n
        sprite[x-1:x+2] = ["#", "#", "#"]
        # print("".join(sprite))
        # print(cadena)


pantalla = []
for i in range(6):
    linea = cadena[i*40:(i+1)*40]
    pantalla.append(linea)

for a in pantalla:
    print(a)
print(len(a))
