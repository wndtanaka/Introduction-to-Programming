num = int(input("One positive integer please: "))
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print("{} is a not prime!".format(num))
            break
        else:
            print("{} is a prime.".format(num))
            break