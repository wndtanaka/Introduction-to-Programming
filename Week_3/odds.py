num = 1
while num in range(1, 100):
    if num != len(range(1, 100)):
        print(str(num) + ", ", end='')
    else:
        print(num)
    num += 2
