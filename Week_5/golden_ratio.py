try:
    nums = input("Enter two numbers: ")
    print()

    nums = nums.split()
    b = float(nums[0])
    a = float(nums[1])

    if a < b:
        a, b = b, a

    first_res = (a + b) / a
    second_res = a / b

    if round(first_res, 3) == round(second_res, 3):
        print("Golden ratio!")
    else:
        print("Maybe next time.")
except:
    print("Invalid input.")
