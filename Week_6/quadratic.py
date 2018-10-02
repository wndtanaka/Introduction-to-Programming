import sys
import math


def quadratic(a, b, c):
    try:
        # the square root of the discriminant
        disc = math.sqrt(b**2 - 4*a*c)
        if disc == 0:
            # what's the type of this?
            return -b / (2*a),
        else:
            # what's the type of this?
            return -b+disc / (2*a), -b-disc / (2*a)
    except:
        print("Can not taking square root of a negative number")


a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
try:
    x_1, x_2 = quadratic(a, b, c)  # unpack the returned tuple

    print('The equation {}x^2 + {}x + {} = 0 has these solutions:'.format(a, b, c))
    print('x={:.2f} and x={:.2f}'.format(x_1, x_2))
except:
    pass