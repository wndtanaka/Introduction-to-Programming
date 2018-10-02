def paper_doll(text):
    word = ""
    for i in range(0, len(text)):
        word += text[i] * 3
    return word


print(paper_doll('Mississippi'))
