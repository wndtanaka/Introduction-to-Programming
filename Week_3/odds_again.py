import sys

if sys.argv[1] == '-a':
    num = 1
    while num in range(1,100):
        print(num)
        num += 2
elif sys.argv[1] == '-d':
    num = 100
    while num in range (100,0,-1):
        if num % 2 != 0:
            print(num)
        num -= 1
else:
    print("Usage: python3 odds_again.py (-a|-d)")