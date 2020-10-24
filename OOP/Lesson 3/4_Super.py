class Personel:
    baslangic_maas = 4000

    def __init__(self,ad,soyad,telefon):
        self.Ad = ad
        self.Soyad = soyad
        self.Telefon = telefon

    def FullName(self):
        return f"{self.Ad} {self.Soyad}"
    def Phone(self):
        return f"+90{self.Telefon}"

    def __str__(self):
        return f"{self.Ad} {self.Soyad} {self.Telefon} {self.baslangic_maas}"


per = Personel("Emre","Haskilic","5059796816")

print(per)

print(per.Phone())

class Developer(Personel):
    _baslangic_maas = 7000

    def __init__(self,ad,soyad,telefon,yazilimdili):
        super().__init__(ad, soyad, telefon)
        self.YazilimDili = yazilimdili
    def __str__(self):
        return f"{super().__str__()} {self.YazilimDili}"    

dev = Developer("Emre","Haskilic","5059796816","python")

print(dev)

print(issubclass(Personel,Developer)) # personel developerın alt sınıfı mıdır False

print(issubclass(Developer,Personel)) # developer personelin alt sınıfı mıdır True