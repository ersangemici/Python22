while True :
    islem = input("Islem yapmak icin (1) ; cikis yapmak icin (2)  ")
    if islem == '1' :
        x = float(input("birinci sayiyi giriniz\n"))
        y = float(input("ikinci sayiyi giriniz\n"))
        print((x+y)/2)# ortalama = (x+y)/2 
        #print(ortalama)
    elif islem == '2' :
        print("cikis yapiliyor")
        break
    else  :
        print("gecerli islem seciniz")
        break
    

