#A list containss names of boys and girls as its elements.boys name are stored as tuples.write a program to find out number of boys and girls
lst=[('krisil','devang','shrey','tirth'),'jensi','aarvi','dhyana',('krisil','devang','shrey','tirth')]
b=0
l=0
for e in lst:
    if isinstance(e,tuple):
        b+=len(e)

        l+=1
g=len(lst)-l

print("boys:",b)
print("girls:",g)
print(l)
print(len(lst))
