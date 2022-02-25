
from cryptography.fernet import Fernet as ft


main_password = 123456  #input("main password ?\n")
söz1 = {}
while True :
    Password = input("sifrenizi giriniz :\n")
    key = ft.generate_key()


    fernet = ft(key)
    if int(Password) == int(main_password) : 
        while True :
            print("\n","1)Sifre ekle\n 2)Sifre Sil \n 3)Sifre görüntüle \n 4)Sifre degistir\n 5)cikis")
            islem = int(input())

            if islem == 1 :
                ekle = input("Sifrenin anahtar kelimesi :")
                sifre= str(input("anahtarin sifresini giriniz :"))
                #Alinan sifreyi encrypt ederek sozluge ekler
                encSifre = fernet.encrypt(sifre.encode())
                söz1[ekle] = encSifre 


            elif islem == 2 :
                print(söz1.keys())
                tmp = input("silmek istediginiz sifrenin ahtarini giriniz :")
                söz1.pop(tmp)


            elif islem == 3 :
                print(söz1.keys())
                tmp = input("Hangi sifreyi görmek istiyorsunuz :")
                print(söz1[tmp])
                tmp1 = int(input("Sifrenizin decrypt hali icin dogrulayiniz =\n"))
                if tmp1 == main_password :
                    #Alinan sifreyi decrypt ederek sozlukten okur
                
                    decSifre = fernet.decrypt(söz1[tmp])
                    print("decrypt sifre :",decSifre)
                else :
                    print("Dogrulama yapılamadi")


            elif islem == 4 :
                print(söz1.keys())
                tmp = input("Hangi sifreyi degistirmek istiyorsunuz :")
                tmp1 = input("Yeni sifreyi giriniz.... ")
                encSifre = fernet.encrypt(tmp1.encode())
                söz1[tmp] = encSifre 
                


            elif islem == 5 :
                print("cikis yapiliyor")
                break
            
            else : print("gecerli islem seciniz !!")
    break




            
