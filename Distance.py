import math


class point:
    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y


def distance(p1, p2):
    doSqrt = math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2)
    print doSqrt
    return math.sqrt(doSqrt)


point1 = point(10, 20)
point2 = point(10, 25)
print "distance is " + str(distance(point1, point2))
