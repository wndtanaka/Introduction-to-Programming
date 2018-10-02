punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

line = input("Enter line: ")
anagram = input("Enter anagram: ")
print()
line = line.lower()
anagram = anagram.lower()

line_no = ''
anagram_no = ''
for char in line:
    if char not in punctuations:
        line_no += char
for char in anagram:
    if char not in punctuations:
        anagram_no += char
line_no = line_no.split()
anagram_no = anagram_no.split()
line2 = ''
anagram2 = ''
for word in line_no:
    line2 += word
for word in anagram_no:
    anagram2 += word

x = []
y = []
res = []
for letter in line2:
    x.append(letter)
for letter in anagram2:
    y.append(letter)
for letter in x:
    if letter in y:
        y.remove(letter)
        res.append(letter)

if x == res:
    print("Anagram!")
else:
    print("Not an anagram.")
