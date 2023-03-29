n=int(input("몇개의 데이터 처리 : "))
listex = []


print('%d개의 데이터 입력 : ' % n)
for k in range(n):
    listex.append(int(input())) 

print("sum : %d\navg : %.2f\nmax : %d\nmin : %d"%(sum(listex), sum(listex)/len(listex), max(listex), min(listex)))