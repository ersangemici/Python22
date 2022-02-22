import random
kucukharf = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
buyukharf = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
sayi = ["0","1","2","3","4","5","6","7","8","9"]
#main1= [kucukharf,buyukharf,sayi]
passwordlist = []
sifre = ""
k=n= 0
while True :
    islem = int(input("islem seciniz :1) sifre olustur 2) sifreyi yazdır ::::"))
    if islem == 1 :
        j = int(input("kac haneli sifre olsun:"))
        while k<j :
            i = random.randint(0,2)
            if i == 0 :
                a = random.randint(0,25)
                passwordlist.append(kucukharf[a])
            elif i == 1 :
                a = random.randint(0,25)
                passwordlist.append(buyukharf[a])
            elif i == 2 :
                a = random.randint(0,9)
                passwordlist.append(sayi[a])
            k =k+1
    elif islem == 2 :
        while n<j :
            print(passwordlist[n],end="")
            n=n+1
        break





