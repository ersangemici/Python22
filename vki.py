def vucudKitleEndeksi  (boy,kilo) :
    tmp = kilo/(boy**2) 
    return tmp
a =float(input("boyunuz girniiz"))
b= float(input("kilonuzu giriniz"))
vki = vucudKitleEndeksi(a,b)
if vki<18.5 :
    print("Zayıfsın")
elif 18.5 < vki and vki <= 25 :
    print("Normalsin")
elif 25 < vki and vki <= 30 :
    print("Kilolusun")
elif 30 < vki :
    print("Obezsin")

