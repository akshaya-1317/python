#10. Print all combinations of 1, 2, and 3. Any number should be not be duplicated.


l = []
print("Enter 3 numbers: ")
for i in range (3):
   l.insert(i, int(input()))

for i in range(0,3):
    for j in range(0, 3):
        for k in range(0, 3):
            if(i!=j & j!=k & k!=i):
                print(l[i], l[j], l[k])

