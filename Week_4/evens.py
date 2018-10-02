import sys

num = int(sys.argv[1])
start_point = int(sys.argv[2])
count = 0
even = 2
start_number = start_point * even
number_list = []
while True:
    start_number += 2
    number_list.append(start_number)
    count += 1
    if num == count:
        break
for i in number_list:
    print(i)