import math
t1, g1 = map(float,input().split())
t2, g2 = map(float,input().split())
# from degrees to radians
t1 = t1*3.14/180
g1 = g1*3.14/180
t2 = t2*3.14/180
g2 = g2*3.14/180
distance=6371.01*math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
print(distance)