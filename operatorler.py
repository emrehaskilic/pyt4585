# Aritmetik operatorler

# +, -, /, *, %, **

sayi1 = 120

sayi2 = 50

toplam = sayi1 + sayi2

# *50 str ile kullanılırsa karakteri 50 defa yazar
print("islem sonucu" + " "*50 + str(toplam))

# ODEV
# Disardan aldığınız 2 sayisinin toplamı

# sayi3 = 10
# sayi4 = 20

# toplam = sayi3 + sayi4
# carpim = sayi3 * sayi4
# cikarma = sayi3 - sayi4
# bolme = sayi3 / sayi4
# us_alma = sayi3 ** sayi4
# mod = sayi3 % sayi4

# print(toplam)
# print(carpim)
# print(cikarma)
# print(bolme)
# print(us_alma)
# print(mod)

# ikinci bir ornek

sayi1 = float(input("Lutfen 1. sayiyi giriniz: "))
sayi2 = float(input("Lutfen 2. sayiyi giriniz: "))

toplam = sayi1 + sayi2
fark = sayi1 - sayi2
bolum = sayi1 / sayi2
mod = sayi1 % sayi2
carpim = sayi1 * sayi2
kuvvet = sayi1 ** sayi2

result = "Toplama islemi metodu: " + \
    str(toplam) + "\nCikarma islemi sonucu: " + \
    str(fark) + "\nBolme islemi sonucu:" + \
    str(bolum) + "\nMod islemi: " + \
    str(mod) + "\nCarpma islemi sonucu: " + \
    str(carpim) + "Kuvvet islemi sonucu: " +\
    str(kuvvet)
print(result)
