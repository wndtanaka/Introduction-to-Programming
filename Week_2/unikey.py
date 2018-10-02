import random

name = input('Your full name: ').split()
first_name = name[0]
last_name = name[1]
unikey = first_name[0] + last_name[0:3] + str(random.randint(1000,9999))
print('Your UniKey is: {}'.format(unikey))