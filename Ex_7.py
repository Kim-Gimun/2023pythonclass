from random import randrange
from random import sample

#randrange() 함수와 집합을 이용, 중복을 제거

lottoList = []
i=0

mylotto = set()
while len(mylotto) != 6:
    mylotto.add(randrange(0, 41))
    
print("집합 : {}".format(mylotto))
print("집합 : {}".format(sorted(mylotto)))

print("\n sample로 번호리스트 만들기")
lotto = sample(range(1, 46), 6)
print("sample 함수 리스트 : {}".format(lotto))
print("sample 함수 정렬리스트 : {}".format(sorted(lotto)))