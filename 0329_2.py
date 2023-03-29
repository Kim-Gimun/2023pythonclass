import random

score = 0
print("두자릿수 덧셈을 풀어보세요")
for k in range(5):
    tnum = 0
    correct = False
    num1 = random.randrange(10, 99)
    num2 = random.randrange(10, 99)
    while tnum < 3 and not correct :
        print('%d + %d = '% (num1, num2),end = '')
        ans = int(input("문제를 풀어보세요"))
        if ans == num1+num2:
            print("correct! : %d번만에 맞췄습니다"% (tnum+1))
            correct = True
            score += (20 - tnum*3)
        else:
            print("Try again")    
        tnum += 1
    if tnum == 3:
        print("정답 = ", num1+num2)
print("%d점입니다"%(score))