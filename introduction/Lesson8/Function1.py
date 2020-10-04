#  Yaptığımız işlemin sonunda oluşan değeri geriye teslim almak istiyorsak function kullanmalıyız

def Hesapla(x,y):
    toplam = x + y

    return toplam  #not : return anahtar kelimesinden sonra herhangi bir kod blogu calışmaz (SON ANAHTAR KELİMEDİR)

sonuc = Hesapla(10,3)    

print(sonuc)