
suNo, quizNo=map(int,input('합을 구할 데이터 수와 질문 갯수 입력 : ').split(' '))

numbers=list(map(int,input('데이터의 수만큼 숫자 입력 : ').split(' ')))

pSum=[0]
temp=0

for i in numbers:
    temp += i
    pSum.append(temp)

print(pSum)
for i in range(quizNo):
    s, e=map(int,input('몇번째부터 몇번째의 합? :').split(' '))
    print(pSum[e] - pSum[s-1])
