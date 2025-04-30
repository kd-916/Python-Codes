#5)	Generate all Pythagorean Triplets with side length <= 30.
for i in range(0,31):
    for j in range(0,31):
        for k in range(0,31):
            if (i**2 + j**2 == k**2):
                print(i,j,k)