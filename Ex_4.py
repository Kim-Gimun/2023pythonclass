menu = ('기본햄버거', '치즈햄버거', '불고기버거', '와퍼킹버거')
price = (4000, 4500, 5000, 7000)

for k in range(len(menu)):
    print(k, " : ", menu[k], " : ", price[k])

menuList = list(menu)
priceList = list(price)
print("메뉴 : ", menuList)
print("가격 : ", priceList)
print("-----------------------------")
menuList.append('새우버거')
priceList.append(5500)
menu = tuple(menuList)
price = tuple(priceList)
print("메뉴 : ", menu)
print("가격 : ", price)

print("----------------------------")

for i in range(len(menu)):
    mdict_list = {menu[i] : price[i]}

print(mdict_list)