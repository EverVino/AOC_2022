import math
class Monkey:
    def __init__(self, items, operation, test_number, to_true, to_false ):
        self.operation = operation
        self.test_number = test_number
        self.items = items
        self.to_true = to_true
        self.to_false = to_false 
        self.count = 0
    
    def test(self, item):
        return item % self.test_number == 0
    
    def throw(self, monkeys, product):
        for item in self.items.copy():
            self.count += 1
            new = self.operation(item)
            new = new % product
            
            if self.test(new):
                self.items.remove(item)
                
                monkeys[self.to_true].items.append(new)
            else:
                self.items.remove(item)
                
                monkeys[self.to_false].items.append(new)
        

with open("input11.txt", "r") as f:
    reader = f.read()

reader = reader.split("\n\n")
fun = {
    "mul": lambda x: lambda y:x*y, 
    "suma": lambda x: lambda y:x+y,
    "cuad": lambda x: x*x }

monkeys = []

for block in reader:
    inst = block.split("\n")
    items = inst[1].split(":")[1].replace(",","")
    items = [int(x) for x in items.split()]
    if "* old" in inst[2]:
        operation=fun["cuad"]
    elif "old +" in inst[2]:
        number = int(inst[2].split()[-1])
        operation = fun["suma"](number)
    else:
        number = int(inst[2].split()[-1])
        operation = fun["mul"](number)

    number_test = int(inst[3].split()[-1])
    false_to = int(inst[5].split()[-1])
    true_to = int(inst[4].split()[-1])
    
    monkey = Monkey(items,operation,number_test,true_to,false_to)

    monkeys.append(monkey)
p = 1
for m in monkeys:
    p = p*m.test_number

for _ in range(10000):
    for m in monkeys:
        m.throw(monkeys, p)

monkey_counts = [x.count for x in monkeys]
monkey_counts = sorted(monkey_counts, reverse=True)
print(monkey_counts[0],monkey_counts[1])

print(monkey_counts[0]*monkey_counts[1])




