def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            return a
        elif a > b:
            return b
    if a % 2 != 0 or b % 2 != 0:
        if a < b:
            return b
        elif a > b:
            return a


print(lesser_of_two_evens(2, 5))
