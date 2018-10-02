import sys

num = None
num_list = []
command = sys.argv[1]

while num != 0:
    num = float(input("Number: "))
    if num != 0:
        num_list.append(num)
print("Your numbers were:")
for i in num_list:
    print(i)
if command == '-sum':
    print("The sum of those numbers is {}".format(sum(num_list)))
elif command == '-avg':
    print("The average of those number is {}".format(sum(num_list)/len(num_list)))
elif command == '-max':
    print("The maximum of those number is {}".format(max(num_list)))
elif command == '-min':
    print("The minimum of those number is {}".format(min(num_list)))