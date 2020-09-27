# kullanıcıların dışardan girdiği sayiların toplamını ekrana yazdıran bir uygulama yazınız
sayi = input("Lutfen bir sayi giriniz:")

i = 0
toplam = 0

while i < len(sayi):
    toplam = toplam + int(sayi[i])
    i = i + 1
print(f"Girilen sayi toplamı : {toplam}")






