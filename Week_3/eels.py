import sys

eel_count = 0

num_args = sys.argv[1:]
for i in num_args:
    if i != num_args[len(num_args) - 1]:
        print(i+ ', ',end = "")
    else:
        print(num_args[len(num_args) - 1])
for i in num_args:
    if 'eel' == i:
        eel_count += 1
if eel_count == len(num_args):
    print("Wow, there are so many eels here!")
if 0 < eel_count < len(num_args):
    print("There are a few eels here.")
if eel_count == 0:
    print("Where are the eels?")
