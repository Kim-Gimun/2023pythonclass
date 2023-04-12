file_path="C:\data\class_colon.txt"

data_dict = {}

with open (file_path, "r") as f :
    for line in f:
        id, *data = line.strip().split(":")
        data_dict[id] = tuple(data)

    for k in data_dict:
        print(k, data_dict[k])
snumList = []
smax = 0; midx = 0
for k in data_dict:
    if  int(data_dict[k][1]) > int(smax):
        smax = data_dict[k][1]
    


print('리스트 함수 이용 : 최대수강인원은 = ', smax)