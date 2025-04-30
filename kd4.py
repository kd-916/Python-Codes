#check whether the given number is prime,is perfect,is armstrong,is palindrome,is automorphic

def prime(n):
    for i in range(2,n):
        if(n%i==0 and n!=2):
            return False
    return True

def perfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum+=i
    if(n==sum):
        return True
    return False

def armstrong(n):
    sum1=0
    rem=0
    b=n
    l=len(str(n))
    if(l>=3):
        while(n!=0):
            rem=n%10
            sum1=sum1 + rem**l
            n=n//10 #use // floor divison to tale n =int otherwise a will became float
    
        if(b==sum1):
            return True
    return False

def palindrome(n):
    rev=0
    rem=0
    c=n
    while(n!=0):
        rem=n%10
        rev=rev*10 + rem
        n=n//10

    if(c==rev):
        return True
    return False

def automorphic(n):
    rev=0
    rem=0
    d=n
    n=n*n
    while(n!=0):
        rem=n%10
        rev=rev*10 + rem
        if(d==rev):
            return True
        n=n//10

    
    return False
    

        
num=int(input("Enter number = "))
p=prime(num)
print("Prime =",p)

q=perfect(num)
print("Perfect =",q)

r=armstrong(num)
print("Armstrong =",r)

s=palindrome(num)
print("Palindrome =",s)

t=automorphic(num)
print("Automorphic =",t)
    
