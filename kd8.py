#8)	Check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard. A triangle is valid if the sum of all the three angles is equal to 180 degrees.
print("enter the angles of traingle")
a=int(input("Enter 1st angle"))
b=int(input("Enter 2nd angle"))
c=int(input("Enter 3rd angle"))

if(a+b+c==180):
    print("it is traingle")
else:
    print("it is not a traingle")

