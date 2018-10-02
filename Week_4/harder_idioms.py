import sys

command = sys.argv[1]

numbers = input("Enter some integers: ")
num_list = numbers.split(', ')
print("Your integers were {}".format(num_list))
if command == '-find8':
    print("The number 8 is at index {}".format(num_list.index('8')))
    if '8' not in num_list:
        print("The number 8 is at index -1")
if command == '-evens':
    even_list = []
    for item in num_list:
        if int(item) % 2 == 0:
            item = int(item) / 2
            even_list.append(int(item))
    print("Halfly even numbers: {}".format(even_list))
if command == '-factor8':
    factor8_list = []
    for item in num_list:
        if int(item) % 8 == 0:
            factor8_list.append(item)
    print("Multuples of 8 are: {}".format(factor8_list))