import sys

word = sys.argv[1]
start_point = int(sys.argv[2])
bounce_length = int(sys.argv[3])
letter_count = 0
word_length = len(word)

for i in range(start_point, word_length):
    print(word[i], end='')
    letter_count += 1
    if i == word_length - 1:
        print(word[-2::-1])
