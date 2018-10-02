def n_force(height, rows):
    print()
    line_counter = 1
    row_counter = 1
    for i in range(rows * height):
        print(' ' * (rows * height - i - 1), end='')
        if line_counter == 1:
            if line_counter % height == 0:
                print('/' + ' ' * 0 * 2 + '\\')
            elif line_counter % height != 0:
                i = 0
                while i < row_counter:
                    print('/', end='')
                    print(' ' * 0 * 2, end='')
                    print('\\', end='')
                    if i != row_counter - 1:
                        print(' ' * (height * 2 - 2), end='')
                    i += 1
                print()
        else:
            if height == 1:
                print(('/' + '\\') * (row_counter + 1))
                row_counter += 1
            elif line_counter % height == 0 and height == 2:
                print(('/' + '_' * line_counter + '\\') * row_counter)
                line_counter = 0
                row_counter += 1
            elif line_counter % height == 0 and height > 2:
                print(('/' + '_' * (line_counter * 2 - 2) + '\\') * row_counter)
                line_counter = 0
                row_counter += 1
            if line_counter % height != 0 and row_counter > 1:
                i = 0
                while i < row_counter:
                    print('/', end='')
                    print(' ' * (line_counter * 2 - 2), end='')
                    print('\\', end='')
                    if i != row_counter - 1:
                        print(' ' * (height * 2 - line_counter * 2), end='')
                    i += 1
                print()
            elif line_counter % height != 0:
                print(('/' + ' ' * (line_counter * 2 - 2) + '\\'))
        line_counter += 1

try:
    height = input('Enter height: ')
    if height.isalpha() or height == '' or height in range(1,21):
        raise ValueError("\nInvalid height.")
    else:
        row = input('Enter number of rows: ')
        if row.isalpha() or row == '' or row in range(1,21):
            raise ValueError("\nInvalid number of rows.")
        else:
            n_force(int(height),int(row))
except ValueError as err:
    print(err.args[0])