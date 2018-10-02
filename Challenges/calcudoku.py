import itertools


def calc(ns1, op, ns2):
    if op == 'a':
        return ns1 + ns2
    elif op == 's':
        return ns1 - ns2
    elif op == 'm':
        return ns1 * ns2
    elif op == 'd':
        return ns1 / ns2


def nums(numbers):
    perms = []
    for p in itertools.permutations(numbers,3):
        perms.append(p)
    return perms


def ops():
    operations = []
    for op in itertools.product('m', repeat=3):
        operations.append(op)
    return operations


def check(numbers):
    for ns in nums(numbers):
        for op in ops():
            if (op[0] == 'd' or op[1] == 'd' or op[2] == 'd') and (
                    int(ns[1]) == 0 or int(ns[2]) == 0 or int(ns[3]) == 0):
                continue
            result = int(ns[0])
            result = calc(result, op[0], int(ns[1]))
            result = calc(result, op[1], int(ns[2]))
            result = calc(result, op[2], int(ns[3]))
            if result == 40:
                return True
    # else return false
    return False

perms = (nums('123456'))
for i in perms:
    total = 1
    for j in i:
        total *= int(j)
    #print(total)
    if total == 40:
        print(i)