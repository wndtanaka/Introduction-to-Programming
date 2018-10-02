import sys

enter = True
try:
    if len(sys.argv) > 2:
        raise IndexError
    length = int(sys.argv[1]) + 1
    list = [1]
    for i in range(length):
        print(' '.join(str(x) for x in list))
        holder_list = []
        holder_list.append(list[0])
        for i in range(len(list) - 1):
            holder_list.append(list[i] + list[i + 1])
        holder_list.append(list[-1])
        list = holder_list
except IndexError:
    if len(sys.argv) > 2:
        print("Too many arguments.")
    if len(sys.argv) < 2:
        print("Invalid argument.")
except ValueError:
    print("Invalid argument.")
