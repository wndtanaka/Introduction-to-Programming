import sys
first_number = int(sys.argv[1])
second_number =int(sys.argv[2])
result = first_number % second_number
print('After dividing {} by {}, the remainder is {}.'.format(first_number,second_number,result))