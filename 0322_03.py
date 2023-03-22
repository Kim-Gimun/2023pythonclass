import random

print('어디로 여행을 갈까요')
vote = int(random.randrange(0, 4))
if(vote == 0) :
    print('제주도 ㄱㄱ')
elif(vote == 1) :
    print('사이판 ㄱㄱ')
else :
    print('하와이 ㄱㄱ')


