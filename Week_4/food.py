import sys

menu = sys.argv[1]
list = []
food_list = []
price_list = []
for food in open(menu):
    list.append(food.split())
for item in list:
    food_list.append(item[0])
    price_list.append(item[1])
for i in range(0,len(food_list)):
    print(food_list[i])
    print('\t' + price_list[i])