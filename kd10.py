#10)given the length and breadth of a rectangle, write a program to find whether the area of the rectangle is greater than its perimeter.
l=float(input("enter length of rectagle"))
b=float(input("enter breath of rectangle"))
peri=2*(l+b)
area=l*b
if(area > peri):
    print("Area is greater than perimeter")
else:
    print("Perimeter is greater than area")