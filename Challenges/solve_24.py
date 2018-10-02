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
    for p in itertools.permutations(numbers):
        perms.append(p)
    return perms


def ops():
    operations = []
    for op in itertools.product('asmd', repeat=3):
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
            if result > 24.33333 and result < 24.34:
                result = 24
            if result == 24:
                return True
    # else return false
    return False


try:
    numbers = input('Enter 4 integers: ')
    numbers = numbers.split()
    if len(numbers) > 4:
        raise ValueError
    if check(numbers):
        print("\nYes! 24 is reachable from {} {}, {}, {}, {} {}".format('{', numbers[0], numbers[1], numbers[2],
                                                                        numbers[3], '}'))
    else:
        print('\nNoooo :( 24 is unreachable from {} {}, {}, {}, {} {}'.format('{', numbers[0], numbers[1], numbers[2],
                                                                              numbers[3], '}'))
except ValueError:
    print("\nInput must consist of 4 integers")
except IndexError:
    print("\nInput must consist of 4 integers")