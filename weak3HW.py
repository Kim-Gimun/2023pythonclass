import time
import sys
i = 0
print("10초동안 매초 현재시간을 출력합니다.")
res = int(input("실행하시겠습니까? (1/0)"))
while (res):
    while i in range(10):
        kortime = time.asctime()
        print(kortime)
        time.sleep(1)
        i = i + 1
    print("---10초 경과---")
    res = int(input("다시 실행하시겠습니까? (1/0)"))
    if(res == 0):
        sys.exit()
    elif(res == 1):
        i = 0
