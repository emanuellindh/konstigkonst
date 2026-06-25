import numpy as np

class line:
    def __init__(self, startingPoint, endPoint):
        self.startingPoint = startingPoint
        self.endPoint = endPoint
        if endPoint[0]==startingPoint[0]:
            self.b = np.inf
            self.m = np.inf
        else:
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

# def intersect(line1, line2):
#     # line1.m + line1.b*x = line2.m + line2.b*x
#     # line1.m - line2.m = (line2.b-line1.b)*x
#     # print(line1.b)
#     # print(line1.m)
#     # print(line2.b)
#     # print(line2.m)
#     # if line1.b==np.inf or 
#     if line2.b==line1.b:
#         if line2.m==line1.m and line2.m!=np.inf:
#             return True
#         else:
#             return False
#     else:
#         x = (line1.m-line2.m)/(line2.b-line1.b)
#         y = line1.m + line1.b*x
#         # print(x)
#         # print(y)

#         point = [x,y]
#         v1 = np.subtract(line1.endPoint,line1.startingPoint)
#         u1 = np.subtract(point,line1.startingPoint)
#         v2 = np.subtract(line2.endPoint,line2.startingPoint)
#         u2 = np.subtract(point,line2.startingPoint)
#         t1 = (np.dot(u1,v1))/(np.dot(v1,v1))
#         t2 = (np.dot(u2,v2))/(np.dot(v2,v2))
#         return t1 >= 0 and t1 <= 1 and t2 >= 0 and t2 <= 1

#         # return ((((y<=line1.startingPoint[1] and y>=line1.endPoint[1])
#         #         or (y>=line1.startingPoint[1] and y<=line1.endPoint[1]))
#         #         and ((y<=line2.startingPoint[1] and y>=line2.endPoint[1])
#         #         or (y>=line2.startingPoint[1] and y<=line2.endPoint[1])))
#         #         or (((x<=line1.startingPoint[0] and x>=line1.endPoint[0])
#         #         or (x>=line1.startingPoint[0] and x<=line1.endPoint[0]))
#         #         and ((x<=line2.startingPoint[0] and x>=line2.endPoint[0])
#         #         or (x>=line2.startingPoint[0] and x<=line2.endPoint[0]))))

def intersect(line1, line2):

    x = (line1.m-line2.m)/(line2.b-line1.b)
    y = line1.m + line1.b*x
    # print(x)
    # print(y)

    point = [x,y]
    v1 = np.subtract(line1.endPoint,line1.startingPoint)
    u1 = np.subtract(point,line1.startingPoint)
    v2 = np.subtract(line2.endPoint,line2.startingPoint)
    u2 = np.subtract(point,line2.startingPoint)
    t1 = (np.dot(u1,v1))/(np.dot(v1,v1))
    t2 = (np.dot(u2,v2))/(np.dot(v2,v2))
    return t1 >= 0 and t1 <= 1 and t2 >= 0 and t2 <= 1


# first = line([1,4],[2,1])
# second = line([7,6],[1,2])
# # print(intersect(first,second))
# point = [1.5,25]
# print(np.subtract([1,4],[1,2]))
# v = np.subtract(first.endPoint,first.startingPoint)
# u = np.subtract(point,first.startingPoint)

# t = (np.dot(u,v))/(np.dot(v,v))
# print(t)
