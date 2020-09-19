

#1 disaridan girilen 2 sayinin toplam ver farklarinin bolumundan kalan?

sayi1 = float(input("1. sayiyi gir: "))

sayi2 = float(input("2. sayiyi gir: "))

cevap1 = ((sayi1 + sayi2) % (sayi1-sayi2))

print(cevap1)

#2 disardan girilen 1 sayinin 10 eksiginin 20 fazlasinin 2 ye bolumunu bul?

sayi3 = float(input(" 3. sayiyi gir: "))

cevap2 = ((sayi3 - 10) + 20) / 2

print(cevap2)


#3 disardan girilen 2 sayinin karelerinin toplami ve farklarinin toplami?

sayi4 = float(input("4. sayiyi gir: "))
sayi5 = float(input("5.sayiyi gir : "))

cevap3 = (((sayi4**2) + (sayi5**2)) + ((sayi4**2) - (sayi5**2)))

print(cevap3)

#4 not vizenin %30 u ve finalin %70 inin ortalamasını alip notu veren bir formul?

vize = float(input(" vize notu: "))

final = float(input("final notu: "))

ders_notu = (((vize * 30) / 100) + ((final * 70) / 100)) / 2

print(ders_notu)

#5 isim ve soy isim girip isim.soyisim@hotmail.com yazdır?

isim = str(input("isim giriniz: "))

soyisim = str(input("soyisim giriniz: "))

uzanti = str("hotmail.com")


mail = (isim + "." + soyisim + "@" + uzanti)

print(mail)

# 5 icin diger yontem

isim1= input("isim1 gir: ")
soyisim1= input("soyisim1 gir: ")

email = "{}.{}@hotmail.com".format(isim1, soyisim1)

print(email)


