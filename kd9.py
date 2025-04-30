#9)	Print N natural nos. in reverse
n=int(input("enter nth natural number"))
for i in range(0,n+1):
    if (n-i == 0):
        break
    print(n-i)
    