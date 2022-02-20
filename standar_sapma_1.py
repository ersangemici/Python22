örneklem = []
toplam = standart_sapma = varyans = 0

n = int(input("kaç tane sayi giriceksiniz\n"))
tmp = 1
while True :
    while tmp <= n :
            a = input("eklenicek sayiyi giriniz : \n")
            örneklem.append(a)
            toplam = toplam + float(a)
            tmp = tmp + 1
    i = 0
    tmp = 0
    print(toplam)
    while  i < n :
                 
                varyans +=  (float(örneklem[i])-  toplam/(n))**2 / (n - 1)
                i = i + 1
    print("varyans : ",varyans)    
    standart_sapma = pow(varyans,1/2)
    print("standart sapma : ",float(standart_sapma))
    break


