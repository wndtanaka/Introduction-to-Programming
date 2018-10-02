t_num = 1  # the current triangular number to print out
step = 0  # the quantity added to `t_num`, to get the next triangular number

while True:
    if t_num % 2 == 0:
        print(t_num)
    if t_num % 5 == 0:
        print(t_num)
    if t_num >= 28:
        break
    t_num += step
    step += 1