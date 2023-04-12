pw = input("Input Password : ")
upp, low, dig, pct = 0, 0, 0, 0

if pw.isalnum() == False :
        pct = 1
for k in pw:
    
    
    if k.isupper()==True:
        upp = 1
    if k.islower() == True:
        low = 1
    if k.isdigit() == True:
        dig = 1


    

if(upp + low + dig + pct >= 3):
    print("사용가능")
else:
    print("사용불가능")