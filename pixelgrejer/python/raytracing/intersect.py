import numpy as np

class line:
    def __init__(self, startingPoint, endPoint):
        self.startingPoint = startingPoint
        self.endPoint = endPoint
        self.b = (endPoint[1]-startingPoint[1]) / (endPoint[0]-startingPoint[0])
        self.m = startingPoint[1] - startingPoint[0]*self.b
        # return self
    startingPoint = [0,0]
    endPoint = [0,0]
    b = 0
    m = 0

    

# class line2:
#     def __init__(self, startingPoint, angle, length):
#         self.startingPoint = startingPoint
#         self.angle = angle
#         self.length = length
#     startingPoint = [0,0]
#     angle = 0
#     length = 0

def intersect(line1, line2):
    # line1.m + line1.b*x = line2.m + line2.b*x
    # line1.m - line2.m = (line2.b-line1.b)*x
    # print(line1.b)
    # print(line1.m)
    # print(line2.b)
    # print(line2.m)
    x = (line1.m-line2.m)/(line2.b-line1.b)
    y = line1.m + line1.b*x
    # print(x)
    # print(y)
    return (((y<line1.startingPoint[1] and y>line1.endPoint[1])
            or (y>line1.startingPoint[1] and y<line1.endPoint[1]))
            and ((y<line2.startingPoint[1] and y>line2.endPoint[1])
            or (y>line2.startingPoint[1] and y<line2.endPoint[1])))


first = line([1,4],[2,1])
second = line([7,6],[1,2])
print(intersect(first,second))