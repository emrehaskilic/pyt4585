from abc import ABCMeta, abstractclassmethod,abstractmethod
class BasePhone(metaclass=ABCMeta):
    __metaclass__ = ABCMeta

    def __init__(self,marka,model,fiyat):
        self.Marka = marka
        self.Model = model
        self.Fiyat = fiyat
    @abstractmethod
    def Sound(self):
        return "TELEFON SESİ"    


class Samsung(BasePhone):
    def __init__(self,marka,model,fiyat,tedarikci):
        super().__init__(marka, model, fiyat)
        self.Tedarikci = tedarikci

    def Sound(self):
        return "ERİK DALI"    

class Apple(BasePhone):
    def __init__(self,marka,model,fiyat,garanti):
        super().__init__(marka, model, fiyat)
        self.Garanti = garanti

    def Sound(self):
        return "e 30 a biner"    


samsung = Samsung("Note","Note 20",15000,"Samsung")

print(f"Samsung telefon sesi {samsung.Sound()}")

apple = Apple("Iphone","Iphone 12 Pro Max",30000,1)
    
print(f"Apple telefon sesi {apple.Sound()}")