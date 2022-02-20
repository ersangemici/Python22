


main_password = 123456  #input("main password ?\n")
söz1 = {}
while True :
    Password = input("sifrenizi giriniz :\n")
    if int(Password) == int(main_password) :
        while True :
            print("Sifreyi dogru girdiniz\n","1)Sifre ekle\n 2)Sifre Sil \n 3)Sifre görüntüle \n 4)Sifre degistir\n 5)cikis")
            islem = int(input())
            if islem == 1 :
                ekle = input("Sifrenin anahtar kelimesi :")
                sifre= input("anahtarin sifresini giriniz :")
                söz1[ekle] = sifre
            elif islem == 2 :
                print(söz1.keys())
                tmp = input("silmek istediginiz sifrenin ahtarini giriniz :")
                söz1.pop(tmp)
            elif islem == 3 :
                print(söz1.keys())
                tmp = input("Hangi sifreyi görmek istiyorsunuz :")
                print(söz1[tmp])
            elif islem == 4 :
                print(söz1.keys())
                tmp = input("Hangi sifreyi degistirmek istiyorsunuz :")
                tmp1 = input("Yeni sifreyi giriniz.... ")
                söz1[tmp] = tmp1
            elif islem == 5 :
                print("cikis yapiliyor")
                break
            else : print("gecerli islem seciniz !!")
    break




            