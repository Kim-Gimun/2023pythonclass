import random
import sys

com = random.randrange(1,21)
user = 0

while True :
    user = int(input("1~20사이의 수 입력 : "))
    if com == user:
        print("맞췄습니다")
        sys.exit()
    elif com > user:
        print("더 큰 수입니다")
    elif com < user:
        print("더 작은 수입니다")
