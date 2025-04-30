#12)Given the coordinates (x,y) of center of a circle and its radius, determine whether a point lies inside the circle, on the circle or outside the circle. (Hint: Use sqrt( ), pow( ) )
import math
x=0
y=0
r=3
x1=float(input("Enter coordinate x1"))
y1=float(input("Enter coordinate y1"))

l=math.sqrt((x-x1)**2 + (y-y1)**2)
if(l<r):
    print(x1,",",y1,"lies inside the  circle")
else:
    print(x1,",",y1,"lies outside the  circle")