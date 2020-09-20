# kullanicinin disardan girdiği sayinin tek ve ya cift olma durumunu kontrol et,
#sayi tek ise sayi tektir uyarisi cift ise sayi cifttir.

sayi = int(input("Lutfen bir sayi giriniz: "))
mod = sayi % 2

if(mod == 0):
    print("Sayi cifttir",(sayi))
else:
    print("Sayi tektir",(sayi))
    