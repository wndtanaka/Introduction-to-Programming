with open('menu.txt') as menu:
    while True:
        if menu.readline() == "":
            break
        print(menu.readline())
