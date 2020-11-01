# soyut sınıf

from abc import ABCMeta, abstractclassmethod

class CoreEntity(metaclass=ABCMeta):
    __metaclass__ = ABCMeta
    @abstractclassmethod
    def Insert(self):
        print("Personelin Kaydı Eklendi")






class Personel(CoreEntity):
    def Insert(self):   # .ıktı personel ınsert metodu override etmek üst sınıftan gelen değeri ezerek bizim ihtiyacımız olan şekliyle değiştiriyoruz
        print("Personel Insert Metodu")

class Kategori(CoreEntity):
    def Insert(self):
        print("Kategori Ekleme metodu")




personel = Personel()
personel.Insert() # CoreEntity sınıf içerisinde yer alan metod

kategori = Kategori()

kategori.Insert() # CoreEntity sınıf içerisinde yer alan metod


#ÖNEMLİ => abstract metoduyla tanımladığınız bir fınksitonu başka bir classa miray verdiğinizde o fonsiyonu değiştirmek zorundasınız