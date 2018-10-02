import sys

args_num = len(sys.argv[1:len(sys.argv)])
cup_numbers = int(len(sys.argv[1:len(sys.argv)]) / 2)
jug_numbers = int(len(sys.argv[1:len(sys.argv)]) / 2)
cups = sys.argv[1:cup_numbers + 1]
jugs = sys.argv[jug_numbers+1: jug_numbers * 2 + 1]

cup_volume = 1
jug_volume = 1

for x in range(0,len(cups)):
    cup_volume *= int(cups[x])
for y in range(0,len(jugs)):
    jug_volume *= int(jugs[y])
cups_filled = int(round(jug_volume / cup_volume))
print(cup_volume)
print(jug_volume)
print("Number of cups that can be filled using the jug: {}".format(cups_filled))

#cup = [float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])]
#jug = [float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6])]
#cup_volume = cup[0] * cup[1] * cup[2]
#jug_volume = jug[0] * jug[1] * jug[2]
#cups_filled = int(round(jug_volume / cup_volume))

#print("""Cup dimensions: {} x {} x {}
#Jug dimensions: {} x {} x {}
#Number of cups that can be filled using the jug: {}""".format(cup[0], cup[1], cup[2], jug[0], jug[1], jug[2], cups_filled))
