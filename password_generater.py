import random
kucukharf = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
buyukharf = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
sayi = ["0","1","2","3","4","5","6","7","8","9"]
main = [kucukharf,buyukharf,sayi]
sifre = ""
k=i=0
while True :
    islem = int(input("islem seciniz :1) sifre olustur 2) sifreyi yazdır 3)tekrar sifre olustur  4) cikis yap ::::"))
    if islem == 1 :
        j = int(input("kac haneli sifre olsun:"))
        while k<j :
            i = random.randint(0,2)
            b =random.randint(0,len(main[i])-1)
            sifre = sifre + main[i][b]
            k=k+1
    elif islem == 2 :
        print(f"{sifre}")
    elif islem == 3 :
        i=b=k=0
        sifre=""
    elif islem == 4 :
        break
