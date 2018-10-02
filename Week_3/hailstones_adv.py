def count(num):
    if num % 2 == 0:
        num /= 2
    else:
        num = (3 * num) + 1
    return int(num)


num = int(input("Starting Number: "))
nums_holder = []
new_nums = []
new_nums.append(num)
for i in range(1,num):
    while num != 1:
        num = count(num)
        new_nums.append(num)
        if len(new_nums) > len(nums_holder):
            nums_holder = new_nums
print(new_nums)
print(nums_holder)
