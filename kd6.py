#6)	Accept a number from the user. And print number of digits in it.
n=int(input("Enter the number"))
if(n>=0 and n<=9):
    print("1 Digit")
elif(n<=99):
    print("2 Digit")
elif(n<=999):
    print("3 Digit")
elif(n<=9999):
    print("4 Digit")
elif(n<=99999):
    print("5 Digit")
elif(n<=999999):
    print("6 Digit")
elif(n<=9999999):
    print("7 Digit")
else:
    print("Invalid input")