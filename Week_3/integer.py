num = int(input("Integer: "))

if (num % 2 == 0 and num in range(20,100) or (num % 2 == 1 and num <0)):
    print("{} passes the test!".format(num))
elif num == 0:
    print("Bye!")
else:
    print("{} fails the test :(".format(num))
