import itertools


def permutations(numbers):
    perm = []
    for p in itertools.permutations(numbers):
        perm.append(p)
    return perm


def list_split(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out


def check(ls):
    counter = 0
    for num in ls:
        ls[counter] = int(num)
        counter += 1
    line = list_split(ls, 6)
    for i in line:
        if sum(i) != 21:
            return False
    total_column = 0
    for row in range(0, 6):
        for column in range(0, 6):
            total_column += line[column][row]
        if total_column != 21:
            return False
        total_column = 0
    return ls


def validator(result, perm, possibility):
    if len(result) == 0:
        for key in possibility:
            result.append((possibility[0][2][0],possibility[0][2][1],3,1,6,2))
            #print(possibility[2][0])
    else:
        for i in result:
            if i[0] == perm[0]:
                return False
            if i[1] == perm[1]:
                return False
            if i[2] == perm[2]:
                return False
            if i[3] == perm[3]:
                return False
            if i[4] == perm[4]:
                return False
            if i[5] == perm[5]:
                return False
    return True


def ops(amount):
    operations = []
    for op in itertools.product('123456', repeat=amount):
        operations.append(op)
    return operations


def calc(perms, poss):
    result = []
    total = 0
    for perm in perms:
        if 0 < len(result) < 6:
            # print(result)
            if validator(result, perm,poss):
                result.append(perm)
        if sum(perm) == 21 and len(result) == 0:
            # result.append((5, 4, 3, 1, 6, 2))
            validator(result,perm,poss)
            pass
    total_column = 0
    # for row in range(0, 6):
    #     for column in range(0, 6):
    #         total_column += result[column][row]
    #     if total_column != 21:
    #         print(total_column)
    #         #calc(result)
    #     total_column = 0
    return result


# Scaffholder
oper = ['+', '-', '*', '/']
default_cells = {'line1': [0, 0, 1, 2, 2, 3], 'line2': [0, 4, 4, 5, 5, 3],
                 'line3': [6, 7, 8, 8, 9, 9], 'line4': [6, 6, 10, 10, 11, 11],
                 'line5': [12, 13, 13, 14, 14, 15], 'line6': [16, 16, 13, 14, 17, 15]}
cell_numbers = {'line1': [0, 0, 1, 2, 2, 3], 'line2': [0, 4, 4, 5, 5, 3],
                'line3': [6, 7, 8, 8, 9, 9], 'line4': [6, 6, 10, 10, 11, 11],
                'line5': [12, 13, 13, 14, 14, 15], 'line6': [16, 16, 13, 14, 17, 15]}
cell_labels = ['80*', '3', '5-', '2/', '11+', '1-', '9*', '2', '3-', '30*', '11+', '2/', '6', '8*', '13+', '8+', '10*',
               '1']

possibility = {}
total_labels = []
default_labels = []
# to count how many labels
label_count = []
for key in cell_numbers.values():
    for i in range(len(key)):
        total_labels.append(key[i])
        default_labels.append(key[i])

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
                    if operator == '/':
                        possibility[i] = [x]
                        possibility[i].append([x[1], x[0]])
                    else:
                        possibility[i] = [x]
                else:
                    if operator == '/':
                        possibility[i].append([x[1], x[0]])
                    possibility[i].append(x)
    else:
        num = int(cell_labels[i])
        if i not in possibility:
            possibility[i] = [num]

print(calc(permutations([1, 2, 3, 4, 5, 6]), possibility))
print(possibility)
