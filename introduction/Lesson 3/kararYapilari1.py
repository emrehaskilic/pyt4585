# Karar yapilari
# Karsilastirma operatorleri

# == (esit estittir), soldaki degeri sagdakine esit olma durumu
# 1 == 1 => true - ıf
# 1 == 2 => false - else

# != (esit degildir) soldaki degerin sagdaki degere esit olmama durumu
# 1 != 1 => false - else
# 2 != 1 => true - if

# > buyuktur-- soldaki degerin sagdaki degerden buyuk olma durumu
# 2 > 1 => true - if
# 1 > 1 => false - else

# > soldaki degerin sagdaki degerden kucuk olma durumu
# 1 < 2 => true - if
# 2 < 1 => false - else 

# >= (buyuk ve ya esıt olma) vsoldaki degerin sagdaki degerden buyuk veya esit olma durumu
# 1 >= 1 => true - if
# 2 >= 1 => true - if
# 1 >= 2 => false - else

# <= (kucuk ve ya esit olma) soldaki degerin sagdaki degerden kucuk veya esit olma durumu
# 1 <= 1 => true - if
# 1 <= 5 => true - if
# 5 <= 1 => false - else
# 
username = input("Lutfen kullanici adini giriniz: ") 
username = username.lower\
.replace("ı","i")\
.replace("ç","c")\
.replace("ş","s")\
.replace("ö","o")\
.replace("ğ","g")\
.replace("ü","u")

print(username)

if(username == "ozguctigmac"):
    print("Tebrikler, giris yaptiniz")
else:
    print("Kullanici adiniz yanlis")     

    