import random
sum = 0
num = int(input('정수 하나를 입력해주세요 : '))
i = 0
for  i in range(0, num):
    i += 1
    if i % 2 == 0:
        sum += i
    



print('0 ~ %d까지의 짝수의 합은 %d 입니다'%(num, sum))