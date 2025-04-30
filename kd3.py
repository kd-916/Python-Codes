#count no. of alphabers and no. of digit in a given string
def count(st):
    alpha=0
    num=0
    for ch in st :
        if('a'<= ch <='z' or 'A'<=ch<='Z'):
           alpha+=1

        elif('0'<=ch<='9'):
            num+=1
    print("alphabet=",alpha, "and number =",num)

str=input("enter the string")
count(str)
