num = int(input("Length of Hailstones: "))
hail_count = 0
step_count = 0
nums = []
while hail_count != num:
    for i in range(1,num):
        if hail_count < num:
            if i % 2 == 0:
                i /= 2
                step_count += 1
                nums.append(int(i))
            else:
                i = 3*i + 1
                step_count += 1
                nums.append(int(i))
        if hail_count == step_count:
            break
        hail_count+=1
print(nums)