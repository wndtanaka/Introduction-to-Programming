nums = 0
input_count = 0
while True:
    num = int(input("Input a number, input 0 to exit the program. "))
    if num == 0:
        break
    nums += num
    input_count += 1
average = nums / input_count
print("The average of those numbers is {:.2f}.".format(average))
