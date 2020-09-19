# yorum satiri 
print("hello dunya")


# degisken tanimlama kurallari
# 1) degiskenin ismi sayi ile baslayamaz 
#  2) degiske, iki ve ya fazla kelimeden fazla olusama, olusacak ise ornk,
# benim_kullaniciAdim = "kahramanmaraslimustafa" 
# 3) degisken tanimlamasi yapilirken, kesinlikle tanimli kelimeler kullanilamaz
# 4) degisken adinda lutfen rica ediyorum, turkce karakter kullanmayiniz

benim_adim = "murat vuranok"
mail_adresin = "murat.vuranok@bilgeadam.com"
adim = "murat"
soyadim = 'vuranok'     # " "   yada ' ' ile yazilabilir

#int, string, float

sayi = 5 # int tam sayi veri tipi ondalik deger almaz
print(sayi)

print(type(sayi)) # ile degiskenin turu gorulebilir

print(adim)
print(soyadim)

print(adim +" "+soyadim) #ciktisi murat vuranok olarak gelir
print(adim, soyadim)

fullname = adim + " " + soyadim 
print(fullname)

print("kullanicinin adi soyadi : ", fullname)

x = True
y = False

print(x)
print(y)
print(type(x))

# \n bir alt satira gec => new line
print(fullname + "\n"*5)
print(type(fullname))

print("""
bilge
adam
yazilim
kursu
""")

print("bilge adam \"besiktas\" yazilim dersleri istanbul\n\
    python kursu\
    test satiri")
    
