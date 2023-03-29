import random

sum=0
oddlist=list(range(1,101,2))
print(oddlist)
k=0
for k in range(50):
    sum += oddlist[k]

print(sum)
