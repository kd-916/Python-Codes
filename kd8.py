#8)	Print factorial of a given number.
n=int(input("enter number : "))
n1=1
for i in range(1,n+1):
    n1*=i
print("Factorial of ",n,"=",n1)
