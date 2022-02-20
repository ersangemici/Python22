while True :
    islem=int(input("Yapmak istediğiniz işlemi seçiniz \n1-Toplama\|2-çikarma\|3-bölme\|4-carpma|5-cikis\n"))
    if islem == 1 :
        sayi1 = int(input("birinici sayiyi giriniz :"))
        sayi2 = int(input("ikinci sayiyi giriniz :"))
        sonuc= sayi1+sayi2
        print("cevap :",sonuc)
    elif islem == 2 :
        sayi1 = int(input("birinici sayiyi giriniz :"))
        sayi2 = int(input("ikinci sayiyi giriniz :"))
        sonuc= sayi1-sayi2
        print("cevap :",sonuc)
    elif islem == 3 :
        sayi1 = int(input("birinici sayiyi giriniz :"))
        sayi2 = int(input("ikinci sayiyi giriniz :"))
        sonuc= sayi1/sayi2
        print("cevap :",sonuc)
    elif islem == 4 :
        sayi1 = int(input("birinici sayiyi giriniz :"))
        sayi2 = int(input("ikinci sayiyi giriniz :"))
        sonuc= sayi1*sayi2
        print("cevap :",sonuc)
    elif islem == 5 :
        print("cikis yapiliyor")
        break        
