
import random 
from random import randrange

exList = []

for k in range(20):
    exList.append(randrange(0, 100))
exList.sort()
print(exList)
k = int(input("몇번쨰 데이터를 원하시나요 : "))
print(k, 'th data = ', exList[k-1])


count = 1
exList2 = []
while count < 20:
    randNum = randrange(0, 51)
    if randNum not in exList2:
        exList2.append(randNum)
        count += 1
exList2.sort()
print()
print("exList2 = ",exList2)

k=int(input('몇번쨰로 작은 수를 제거할까요 : '))

for d in range(k):
    mvalue = min(exList2)
    di = exList2.index(mvalue)
    del(exList2[di])

print(k, 'th data = ', mvalue)
print(exList2)







