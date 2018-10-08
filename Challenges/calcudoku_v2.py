import itertools

def permutations(numbers):
    perms = []
    for p in itertools.permutations(numbers):
        perms.append(p)
    return perms

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
    line = list_split(ls,6)
    for i in line:
        if sum(i) != 21:
            return False
    total_column = 0
    for row in range(0,6):
        for column in range(0,6):
            total_column += line[column][row]
        if total_column != 21:
            return False
        total_column = 0
    return ls

def calc(perms):
    result = []
    total = 0
    for perm in perms:
        if sum(perm) == 21 and len(result) < 6:
            result.append(perm)
    total_column = 0
    for row in range(0, 6):
        for column in range(0, 6):
            total_column += result[column][row]
        if total_column != 21:
            print(total_column)
            calc(result)
        total_column = 0
    return result

print(calc(permutations([1,2,3,4,5,6])))

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

