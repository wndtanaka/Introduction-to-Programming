import sys
file = sys.argv[1]
index = sys.argv[2]
for word in open(file):
    if word[0] == index:
        print(word)