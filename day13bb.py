from functools import cmp_to_key


def result(left, right):
    if left < right:
        return -1
    elif left > right:
        return 1
    return 0


def is_ordered(left, right):
    a = (left,right)
    match a:
        case (int(), int()):
            return result(left, right)
        case (list(), int()):
            return is_ordered(left, [right])
        case (int(), list()):
            return is_ordered([left], right)
        case (list(), list()):
            for l, r in zip(left, right):
                if is_ordered(l, r) != 0:
                    return is_ordered(l, r)

            return result(len(left), len(right))


def part_1(pairs: list[str]):
    res = 0
    for i, pair in enumerate(pairs):
        left, right = pair.split("\n")

        if is_ordered(eval(left), eval(right)) == -1:
            res += i + 1

    return res

def part_2(pairs: list[str]):
    packets = [[[2]], [[6]]]

    for pair in pairs:
        left, right = pair.split("\n")
        packets.append(eval(left))
        packets.append(eval(right))

    key = cmp_to_key(is_ordered)
    packets.sort(key=key)

    div1, div2 = packets.index([[2]])+1, packets.index([[6]])+1

    return div1 * div2


with open("input13.txt", "r") as file:
    d = file.read().split("\n\n")

print(part_1(d))
print(part_2(d))
