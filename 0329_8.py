import random as r
import time as t
num = int(input("슬롯을 몇번 돌리겠습니까"))
slot = [0]*3
for k in range(num):
    for k in range(3) :
        slot[k]=r.randrange(7, 10)                                     # 무작위 수 7, 8, 9 생성
        print('%d ' % slot[k], end = '')
        t.sleep(1)

    if sum(slot) == 21:
        print("잭팟")
        break
    else:
        print("꽝")