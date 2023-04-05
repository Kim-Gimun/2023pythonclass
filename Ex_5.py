menu = ('기본햄버거', '치즈햄버거', '불고기버거', '와퍼킹버거')
price = (4000, 4500, 5000, 7000)

mdict_list = {}
for i in range (len(menu)):
    mdict_list[menu[i]] = price[i]

print(mdict_list)
print("-----------------------")
mdict_list["새우버거"] = 5500
print(mdict_list)
print("-----------------------")
del mdict_list["기본햄버거"]
print(mdict_list)