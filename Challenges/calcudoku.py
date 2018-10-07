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


def nums(numbers, amount):
    perms = []
    for p in itertools.permutations(numbers, amount):
        perms.append(p)
    return perms


def ops(amount):
    operations = []
    for op in itertools.product('123456', repeat=amount):
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


# perms = nums('123456')
# for i in perms:
#     total = 1
#     for j in i:
#         total *= int(j)
#     #print(total)
#     if total == 40:
#         print(i)
oper = ['+', '-', '*', '/']
default_cells = {'line1': [0, 0, 1, 2, 2, 3], 'line2': [0, 4, 4, 5, 5, 3],
                 'line3': [6, 7, 8, 8, 9, 9], 'line4': [6, 6, 10, 10, 11, 11],
                 'line5': [12, 13, 13, 14, 14, 15], 'line6': [16, 16, 13, 14, 17, 15]}
cell_numbers = {'line1': [0, 0, 1, 2, 2, 3], 'line2': [0, 4, 4, 5, 5, 3],
                'line3': [6, 7, 8, 8, 9, 9], 'line4': [6, 6, 10, 10, 11, 11],
                'line5': [12, 13, 13, 14, 14, 15], 'line6': [16, 16, 13, 14, 17, 15]}
cell_labels = ['80*', '3', '5-', '2/', '11+', '1-', '9*', '2', '3-', '30*', '11+', '2/', '6', '8*', '13+', '8+', '10*',
               '1']
line_counter = 0
possibility = {}
result = []

# to count total number of labels
total_labels = []
for key in cell_numbers.values():
    for i in range(len(key)):
        total_labels.append(key[i])

# while line_counter < 6:
#     label = input()
#     labels = label.split()
#     for num in labels:
#         line_labels.append(num)
#     line_counter += 1

for label in cell_labels:
    for x in range(len(cell_labels)):
        for key in cell_numbers.values():
            for i in range(len(key)):
                if key[i] == x:
                    key[i] = cell_labels[x]

# to count how many labels
label_count = []
for x in range(len(cell_labels)):
    label_count.append(total_labels.count(x))

# separate between numbers and operator
for i in range(len(cell_labels)):
    if cell_labels[i][-1] in oper:
        num = int(cell_labels[i][:-1])
        operator = cell_labels[i][-1]
        perms = ops(label_count[i])
        for x in perms:
            if operator == '*':
                total = 1
                for j in x:
                    total *= int(j)
            elif operator == '+':
                total = 0
                for j in x:
                    total += int(j)
            elif operator == '-':
                total = 0
                if label_count[i] == 2:
                    total = int(x[0]) - int(x[1])
                elif label_count[i] == 3:
                    total = int(x[0]) - int(x[1] - int(x[2]))
                elif label_count[i] == 4:
                    total = int(x[0]) - int(x[1] - int(x[2]) - int(x[3]))
            elif operator == '/':
                total = 0
                if label_count[i] == 2:
                    total = int(x[0]) / int(x[1])
                elif label_count[i] == 3:
                    total = int(x[0]) / int(x[1] / int(x[2]))
                elif label_count[i] == 4:
                    total = int(x[0]) / int(x[1] / int(x[2]) / int(x[3]))
            else:
                break
            if abs(total) == num:
                if i not in possibility:
                    possibility[i] = [x]
                else:
                    possibility[i].append(x)
    else:
        num = int(cell_labels[i])
        if i not in possibility:
            possibility[i] = num
#print(total_labels)
for key in possibility:
    counter = 0
    if type(possibility[key]) == int:
        for num in total_labels:
            if num == key:
                total_labels[total_labels.index(num)] = str(possibility[key])
for key in possibility:
    for num in total_labels:
        if num == key:
            iter1 = 0
            iter2 = 0
            while iter1 < label_count[key]:
                while iter2 < len(possibility[key][iter1]):
                    total_labels[total_labels.index(num)] = possibility[key][iter1][iter2]
                    iter2 += 1
                iter1 += 1
print(total_labels)