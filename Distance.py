# Gets the x,y coordinates between 2 cities and outputs the distance between both
import math
x1,y1=map(int,input("Enter first city coordinaes\n").split())
x2,y2=map(int,input("Enter second city coordinaes\n").split())
dist=math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
print("Distance is %.2f : "%dist)
