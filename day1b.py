with open("input.txt", "r") as f:
    reader = f.readlines()

s = 0
max_cal = 0
bag_elfs=[]
for line in reader:
    if line == "\n":
        bag_elfs.append(s)
        s = 0
    else:
        s += int(line.rstrip())
bag_elfs.sort(reverse=True)
top_three = sum(bag_elfs[:3])
print(top_three)        
        
    
