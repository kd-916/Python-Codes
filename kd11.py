#11)Calculate sin(x); x is a radian value. The formula is as under:
x=int(input("Enter the value of degree from '0'-'90'"))
sinx1=0
sinx2=0
i1=1
i2=1
rad=x*3.14159/180

for i in range(1,16,4):

    for j in range(1,i+1):
        i1*=j
    
    sinx1+=(rad**i/i1)
    

for i in range(3,18,4):
    
    for j in range(1,i+1):
        i2*=j
        
    sinx2+=(rad**i/i2)
   

sinx=sinx1-sinx2
print("Value of SINX is : ",sinx)

    