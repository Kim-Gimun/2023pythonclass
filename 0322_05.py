import random

gcount = 0


while True : 
    com = random.randrange(3)
    user = int(input('가위 0 바위 1 보 2 선택 : '))
    

    if(user == 0 or user == 1 or user ==2) :
        print('user : %d    com : %d' % (user, com))
        gcount = gcount + 1
        if (com == 0 and user == 1) or (com == 1 and user == 2) or (com == 2 and user == 0) :
            print('you win')
        elif user == com :
            print('draw')
        else:
            print('you lose')

    else :
        print('가위바위보를 %d회 했습니다.' % gcount)
        break

