#1)	Generate N numbers of Fibonacci series.
n=int(input("Enter nth number of fibonaci series : "))
first =0
second = 1
next = first + second
for i in range(0,n):
    print(first)
    first=second
    second=next
    next = first + second