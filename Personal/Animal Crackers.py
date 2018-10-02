def animal_crackers(text):
    text = text.lower()
    text = text.split()
    if text[0][0] == text[1][0]:
        return True
    else:
        return False


print(animal_crackers('Crazy Kangaroo'))