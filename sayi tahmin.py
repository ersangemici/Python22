import random
x = random.randint(1,100)
while True :
    sayi = int(input("tahmin ettiginiz sayiyi giriniz"))
    if x > sayi :
        print("tahmininiz :{} gerçek sayidan küçüktür\t",format(sayi))
    elif x < sayi :
        print("tahmininiz: {} gerçek sayidan büyüktür\t",format(sayi))
    elif x == sayi :
        print("tebrikler sayiyi dogru tahmin ettiniz : {}",format(sayi))
        break
