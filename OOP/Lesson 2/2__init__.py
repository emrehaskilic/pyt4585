# __init__ constructor sınıfı bir örnek alığınızda yapılmas gereken konfigürasyon vs var ise __init__ içerisinde tanımlayabilirsiniz


class Personel:
    Adi = ""
    Soyadi = ""
    Telefon= ""
    Mail = ""
    CreatedDate = ""


    def __str__(self):
        return f"{self.Adi}{self.Soyadi}\n Oluşturma Tarihi: {self.CreatedDate}"

    def __init__(self,isim,soyisim,telefon,mail):
        self.Adi = isim
        self.Soyadi = soyisim
        self.Telefon = telefon
        self.Mail = mail
        print("__init__ metodu çalıştı")  

    def GetInfo(self):
        return f"Adi : {self.Adi} \nSoyadi : {self.Soyadi}"      


# init metoduna parametre verdiğinizden dolayı artık buradaki gibi atama işlemi yapamasınız
# personel = Personel()
# personel.Adi = "Emre"
# personel.Soyadi = "Haskilic"
# personel.Mail = f"{personel.Adi}.{personel.Soyadi}@gmail.com"
# personel.Telefon = "+905059796816"

personel = Personel("emre","haskilic","12345678","emrehaskilic@gmail.com")
print(personel)

print(personel.GetInfo())