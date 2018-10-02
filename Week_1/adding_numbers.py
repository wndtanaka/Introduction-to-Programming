import datetime

print("Hello")
print("I will add two numbers for you")
n1 = input("Enter the first number: ")
n1 = int(n1)
n2 = input("Enter the second number: ")
n2 = int(n2)
n3 = input("Enter the third number: ")
n3 = int(n3)
print("The sum of your number is ")
print(n1+n2+n3)

# Part 2
# It produces 23, because int function is casting the variables as an Integer
this_year = datetime.datetime.now().year
birth_year = int(input("On what year were you born? "))
age = this_year - birth_year
turning_age = input("Is your birthday already passed?[y/n]".format(age))
if turning_age[0] == 'y':
    print("You are {} years old".format(age))
elif turning_age[0] == 'n':
    age = this_year - birth_year - 1
    print("You are {} years old".format(age))
else:
    print("Your input is invalid.")