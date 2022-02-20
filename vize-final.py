not1=not2= 0
not1 = int(input("birinci sayiyi girniiz"))
not2 = int(input("ikinci sayiyi girniiz"))
ortalama = (not1 + not2)/int(2)
if 50 < ortalama  and ortalama <60  :
    print("geçtin")
elif 60<ortalama and ortalama <80 :
    print("iyi bir ortalama ile geçtin")
elif ortalama>80 :
    print("çok iyi bir ortalama ile geçtin")
elif ortalama<50 :
    print("kaldınız")