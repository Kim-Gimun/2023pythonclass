import random

print("몇으로 나누는 놀이를 할까요 : ")
num = int(input())
print("Start : %d로 나누어지는 가장 가까운 수로 답하기"%(num))

for k in range(5):
    call = int(input("Input Call Number"))
    r = call % num
    r2 = num - r
    if(r2 < r):
        ans = call + r2
    else:
        ans = call - r
    print("Answer is : %d"%(ans))