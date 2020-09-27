# Telefon Rehberi

#Kullanici uygulamayı calıştırdığında seçecekler sunulacak

################ Telefon Rehberi ################ 
# Kayıt Eklemek için 1
# Kayıt Düzenlemek için 2
# Kayıt Silmek için 3
# Kayıt listesi için 4
# Arama için 5
#Lütfen bir deger giriniz: ()
# Adı              :   
# Soyadı           :
# Mail Adresi      :
# Telefon Numarasi :
# 
# Yeni bir işlem yapmak istiyor musunuz (Y/N):
# Düzenleme yaparken Örneğin İd yi İsmi Soyisimi Tel ve Maili düzenleyebilmemiz lazım
#  
##################################################
print("""
*******************************
*                             *
*******TELEFON REHBERİ*********  
*                             *
*******************************
!KAYIT EKLEMEK İÇİN 1'i
!KAYIT DÜZENLEMEK İÇİN 2'yi
!KAYIT SİLMEK İÇİN 3'ü
!KAYIT LİSTESİ İÇİN 4'ü
!REHBERDE ARAMA YAPMAK İÇİN 5'i
-------- tuşlayınız---------
""")



deger = input("Lütfen Yapmak İstediginiz islemi Seciniz:")

rehber = [
    {
        "id"   : "0" ,
        "isim" : "Emre" ,
        "soyisim": "Haskılıç" ,
        "mail": "emre.haskilic@gmail.com" ,
        "telefon" : "+905059796816",

    }

         ]




isim = input("İsim:")
soyisim = input("Soyisim:")
mail = input("Mail:")
telefon = input("Telefon No:")
id =len(rehber)


if deger == 1:
    

    rehber.append(
{ 
    "id":id,
    "isim":isim,
    "soyisim":soyisim,
    "mail":mail,
    "telefon":telefon
}
              )
    print("Kayıt Başarıyla eklendi")
    i = 0
    elif deger == 4:
        while i < len(rehber)
        print(rehber[i])
        i += 1




yn = input("Yeni Bir İşlem İstiyor musunuz?:(Y/N)")
yn = yn.lower

if yn == "n":
    print("Güle Güle")