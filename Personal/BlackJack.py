def blackjack(a, b, c):
    if a + b + c >= 22:
        if a == 11:
            a = 1
            return a + b + c
        if b == 11:
            b = 1
            return a + b + c
        if c == 11:
            c = 1
            return a + b + c
        return 'BUST'
    else:
        return a + b + c


print(blackjack(7, 7, 10))
