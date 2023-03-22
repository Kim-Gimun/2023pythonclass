import random
com = (random.randrange(0, 3))
user = int(input('가위 0 바위 1 보 2 선택 : '))
gcount = 0
print('user : %d    com : %d' % (user, com))


if((com == 0 and user == 1) or (com == 1 and user == 2) or (com == 2 and user == 0)) :
    gcount = gcount + 1
    print('you win')
elif((com == 0 and user == 0) or (com == 1 and user == 1) or (com == 2 and user == 2)) :
    gcount = gcount + 1
    print('draw')
elif((com == 0 and user == 2) or (com == 1 and user == 0) or (com == 2 and user == 1)) : 
    gcount = gcount + 1
    print('you lose')
else :
    print(gcount, '회 했습니다')