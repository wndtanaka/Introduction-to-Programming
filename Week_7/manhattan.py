# YOUR CODE HERE
import sys

try:
    n = sys.argv[1]  # width of the map
    m = sys.argv[2]  # height of the map
    c = float(sys.argv[3])  # cost to travel between blocks
    x1 = int(sys.argv[4])
    y1 = int(sys.argv[5])
    x2 = int(sys.argv[6])
    y2 = int(sys.argv[7])

    distance_x = x2 - x1
    distance_y = y2 - y1
    total_distance = abs(distance_x + distance_y)
    total_cost = abs(total_distance * c)
    if x1 >= n and y1 >= m and c != 0.00:
        print("This trip will cost ${:.2f} and you will have travelled {} blocks".format(total_cost,total_distance))
    elif x1 < n and y1 < m:
        print("This place isn't on the map")
    elif c == 0.00:
        print("You got a free ride and you will have travelled {} blocks".format(total_distance))
except IndexError:
    pass