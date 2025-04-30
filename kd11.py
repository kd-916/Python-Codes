#11)	Given three points (x1,y1), (x2,y2) and (x3,y3), check if all the three points fall on one straight line.
x1=float(input("Enter point x1"))
y1=float(input("Enter point y1"))
x2=float(input("Enter point x2"))
y2=float(input("Enter point y2"))
x3=float(input("Enter point x3"))
y3=float(input("Enter point y3"))
m1=(y2-y1)/(x2-x1)
m2=(y3-y1)/(x3-x1)
m3=(y3-y2)/(x3-x2)

if(m1==m2 and m2==m3 and m1==m3):
    print("given three points are in a line")
else:
    print("not in a line")