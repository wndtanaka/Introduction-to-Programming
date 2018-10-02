people = [
    ('Alice', 32),  # one tuple
    ('Bob', 51),  # another tuple
    ('Carol', 15),
    ('Dylan', 5),
    ('Erin', 25),
    ('Frank', 48)
]
ages = []
for i in people:
    ages.append(i[1])
for i in people:
    if i[1] == min(ages):
        print("Youngest person: {}, {} years old.".format(i[0], i[1]))
        break
