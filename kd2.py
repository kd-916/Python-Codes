#print multiplication table

def table(a):
    for i in range(1,11):
        b=a*i
        print(a,"X",i,"=",b)

n=float(input("enter the number"))
table(n)
