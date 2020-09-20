#Örnek: Disardan kullanici not girişi saglanacak
# 0 - 30 => FF
# 31-50 => DD
# 51- 70 => CC
# 71- 84 => BB
# 85 - 100 =>AA Uyarisini veriniz
try:
    puan = int(input("Lutfen not girinizi: "))
    sonuc = "Girilen {} notun karsiligi olsn harf notunuz: {}"

    if puan >= 0 and puan <= 30:
        print(sonuc.format(puan,"FF"))
    elif puan > 30 and puan <= 50:
        print(sonuc.format(puan,"DD"))
    elif puan > 50 and puan <= 70 :
        print(sonuc.format(puan,"CC"))
    elif puan > 70 and puan <= 84 :   
        print(sonuc.format(puan,"BB"))
    elif puan > 85 and puan <= 100 :
        print(sonuc.format(puan,"AA"))
    else:
        sonuc = "Lütfen 0 ile 100 arasinda bir not girisi yapiniz"
        print(sonuc)    
except ValueError as aa:
    print(aa)

