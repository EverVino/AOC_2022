with open("input.txt", "r") as f:
    reader = f.readlines()

s = 0
max_cal = 0
for line in reader:
    if line == "\n":
        if s > max_cal:
            max_cal = s
        s = 0
    else:
        s += int(line.rstrip())

print(max_cal)        
        
    
