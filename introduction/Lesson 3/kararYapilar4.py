# Disaridan girilen kelimenin uzunlugu, 8 karaktere esit veya uzunsa parola onaylandı, kisa ise daha uzun bir sifre seciniz uarisi verdiriniz
kelime = input("Kelime giriniz: ")
uzunluk = len(kelime)

if(uzunluk < 8):
    print("daha uzun bir sifre seciniz")
else:
    print("Parola Onaylandi")
