import time as t

st1 = input("문자열 입력: ")
count = len(st1)
outStr = ''
for k in range(count-1, -1, -1):
    outStr += st1[k]

print("거꾸로 출력 -> %s"%outStr)