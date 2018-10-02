height = input("Enter height: ")
print()
if height.isalpha():
    print("Invalid height.")
elif 2 <= int(height) <= 20 and not height.isalpha():
    height = int(height)
    long_line = height * 2;
    char_count = 0
    current_line = 1;
    while current_line <= height:
        while char_count < long_line - 1 and current_line <= height:
            print(' ', end='')
            char_count += 1
        print('/', end='')
        while char_count - current_line < long_line - 2 and current_line % height == 0:
            print('_' * 2, end='')
            char_count += 1
        while char_count - current_line < long_line - 2 and current_line % height != 0:
            if char_count - current_line < long_line:
                print(' ' * 2, end='')
                char_count += 1
        char_count = 0
        print('\\', end='')
        print()
        char_count = 0 + current_line
        current_line += 1
    while current_line <= height * 2:
        while char_count < long_line - 1 and current_line <= height * 2:
            print(' ', end='')
            char_count += 1
        print('/', end='')
        while char_count - current_line < long_line / 2 - 2 and current_line % height * 2 == 0:
            print('_' * 2, end='')
            char_count += 1
        while char_count - current_line < long_line / 2 - 2 and current_line % height * 2 != 0:
            if char_count - current_line < long_line:
                print(' ' * 2, end='')
                char_count += 1
        print('\\', end='')
        char_count = 0 + current_line
        while char_count < long_line and current_line <= height * 2:
            print(' ' * 2, end='')
            char_count += 1
        print('/', end='')
        while char_count - current_line - 1 < long_line / 2 - 2 and current_line % height * 2 != 0:
            if char_count - current_line < long_line:
                print(' ' * 2, end='')
                char_count += 1
        while char_count - current_line - 1 < long_line / 2 - 2 and current_line % height * 2 == 0:
            print('_' * 2, end='')
            char_count += 1
        print('\\', end='')
        print()
        char_count = 0 + current_line
        current_line += 1
else:
    print("Invalid height.")