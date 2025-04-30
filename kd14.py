#14)	Accept marks of three subjects. Print total and average along with whether a candidate has passed or fail. If student secures <= 39 marks in any subject, consider him as fail. Also assigned a subject wise grade based on the following table:
a=int(input("Enter '1' if you are absent in any test else '0'"))
if(a):
    print("GRADE ='NA'")
else:
    s1=float(input("Enter marks of physics out of 100 :"))
    s2=float(input("Enter marks of chemistry out of 100 :"))
    s3=float(input("Enter marks of mathametics out of 100 :"))
    sum=s1+s2+s3
    avg=sum/3
    print("total:",sum)
    print("average:",avg)
    if(avg>=0 and avg<=39):
        print("GRADE ='F'")
    elif(avg>39 and avg<=44):
        print("GRADE ='P'")
    elif(avg>44 and avg<=49):
        print("GRADE ='C'")
    elif(avg>49 and avg<=54):
        print("GRADE ='B'")
    elif(avg>54 and avg<=59):
        print("GRADE ='B+'")
    elif(avg>59 and avg<=69):
        print("GRADE ='A'")
    elif(avg>69 and avg<=79):
        print("GRADE ='A+'")
    elif(avg>79 and avg<=100):
        print("GRADE ='O'")