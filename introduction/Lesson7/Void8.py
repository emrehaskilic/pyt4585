#dışarıdan aldığı değer göre içi dolu kare çiziniz





def kareVol1(x):
    index = 0
    while index < x:
        metin = ""
        for i in range(x):
            metin += "X"
        print(metin)
        index += 1


kareVol1(10)


def kareVol2(x):
    index = 0
    while index < x:
        print("X "*x)
        index += 1
kareVol2(10)        


def kareVol3(x):
    for i in range(x):
        print("X "*x)
    
kareVol3(10)    