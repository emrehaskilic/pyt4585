class Personel:
    Adi = ""
    Soyadi = ""
    Telefon = ""
    Mail = ""
    Yas = 0
# 2)self metodu direkt olarak sınıfın adını ve ram üzerindeki adresini teslim ederken __str__ metodunu override işlemi yaparsanız sizin geriye döndüğünüz ekranda görünür
    def __str__(self):
        return f"{self.Adi}{self.Soyadi}"

personel = Personel()

personel.Adi = "Emre"
personel.Soyadi = "Haskilic"
personel.Telefon = "1234567"
personel.Yas = 100
personel.Mail = "emre.haskilic@gmail.com"

print(personel)   #1)sınıftan aldığınız örneği direkt olarak print ederseniz size ram üzerinde tuttuğu adresi teslim eder# <__main__.Personel object at 0x107b73eb0> 
