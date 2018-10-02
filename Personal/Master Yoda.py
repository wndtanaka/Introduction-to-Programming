def master_yoda(text):
    word_list = text.split()
    return "{} {} {}".format(word_list[2], word_list[1], word_list[0])


print(master_yoda('i am home'))
