import random
katılımcılar = ["ali","mehmet","elif","uygar","melek","yusuf","ersan","mert","kaan","yiğit"]
kazanalar = []
i = 0
n= 9
while i<3 :
    x = random.randint(0,n)
    kazanalar.append(katılımcılar[x])
    katılımcılar.pop(x)#bence bu sayede aynı ismi 2 kere çekmesi önleniyor
    n=n-1
    i=i+1
print(kazanalar)