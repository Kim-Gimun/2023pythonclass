import random

taro= ['자유', '시작', '갈등', '풍요', '성공', '자립', '연예', '전진',
        '극복', '회피', '선택', '안정', '희생', '불행', '인내', '유혹',
        '파괴', '균형', '불안', '행복', '결단', '성취']
print('전체 타로카드')
print(taro)
k=0
for k in range(5):
    getTaro = taro[random.randrange(22)]
    print("%d번쨰 타로 : "% (k+1), getTaro)