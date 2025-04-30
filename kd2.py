#largest and smallest out of three
def ls2():
    a=int(input("enter 1st number : "))
    b=int(input("enter 2nd number : "))
    c=int(input("enter 3rd number : "))

    if a>b:
        if a>c:
            print(a,"is largest")
            if b>c:
                print(c,"is smallest")
            else:
                print(b,"is smallest")
        else:
            print(c,"is largest")
            print("\n",b,"is smallest")
    elif b>c:
        print(b,"is largest")
        if a>c:
            print(c,"is smallest")
        else:
            print(a,"is smallest")
    else:
        print(c,"is largest")
        print("\n",a,"is smallest")
       
ls2()
ls2()
ls2()
            
               
