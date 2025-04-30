#7)	Print nCr and nPr.
n=int(input("enter value of n"))
r=int(input("enter value of r"))
n1=1
r1=1
l=n-r
l1=1
for i in range(1,n+1):
    n1*=i
for i in range(1,r+1):
    r1*=i
for i in range(1,l+1):
    l1*=i
c=n1/(r1*l1)
p=n1/r1
print("Combination = ",c)
print("Permutation = ",p)
