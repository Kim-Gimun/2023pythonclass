str1 = "행복한 오늘"
strList = ''
for k in range(0, len(str1)):
    strList += str1[len(str1) -(k + 1)]

print(strList)
