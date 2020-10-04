#Kullanıcı input aracılığıyla uygulamaya sayi girecek

# ve kullanıcı dilediği kadar sayi girebilir :D şokk 

# her sayi girildiğinde kullanıcıya yeni bir sayi girecek misin diye sorulacak

#kullanıcı y tuşuna basarsa lütfen sayi giriniz deyip içeriye sayı alınacak n

# y harici bir tuşa basarsa içeride yer alan tek dsayıların en küçük ve en büyük sayısının birbirine olan farkını geriye dönsün




def FarkHesapla():
    go_on = "y"
    tek_sayilar = []
    while go_on == "y" or go_on == "Y":
        number = float(input("Sayi gir:"))
        if number % 2 != 0:
            tek_sayilar.append(number)
        go_on = input("yeni bir sayi eklemek istiyor musunuz?(Y/N)")
    return max(tek_sayilar) -min(tek_sayilar)

sonuc = FarkHesapla()
print("İşlem sonucu:",sonuc)



