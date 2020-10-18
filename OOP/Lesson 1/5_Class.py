from datetime import datetime # tarih belirtir
from datetime import timedelta # belirtilen tarihten girilen gün kadar öncesini yada sonrasını hesaplar

class Employee:
    FirstName = ""
    LastName = ""
    Mail = ""
    Phone = ""
    #sistem tarafından otomatrik verilecek
    HireDate = f"{datetime.now().day}/{datetime.now().month}/{datetime.now().year} {datetime.now().hour}:{datetime.now().minute}" 
    FireDays = 0
    Adress = ""

    def IseAl(self):
        fireDate = 0
        if(self.FireDays > 0):
            time = (datetime.now() + timedelta(days=self.FireDays))
            fireDate = f"{time.day}/{time.month}/{time.year} {time.hour}:{time.minute}"
        else:
            fireDate = "Gün Sayısı belirtilmediğinden çıkış taraihi hesaplanamadı"    
        print("\n","-"*50)
        print(f"Personelin Adı : {self.FirstName}\nPersonelin Soyadı: {self.LastName}\n Personel Mail: {self.Mail}\nPersonel Telefon : {self.Phone}\nPersonelin Adresi: {self.Adress}\nPersonelin İşe Giriş Tarihi: {self.HireDate}\nPersonelin Sözleşme Bitis Tarihi: {fireDate}\nPersonelin işe girişi yapıldı")
        print("\n","-"*50)
    def Update(self):
        # db içerisinden personeli güncelle
        pass
    def Fire(self):
        # personelin db içerisindeki durumunun değiştirilmesi
        # 1 = Aktif, 2=Pasif, 3=Delete, 4=Kovuldu, 5=İşten Çıkarıldı
        pass
personel = Employee()
personel.FirstName = "Emre"
personel.LastName = "Haskilic"
personel.Mail ="emrehaskilic@gmail.com"
personel.Phone = "+905059796816"
personel.Adress = "İstanbul/Beşiktaş"
personel.FireDays = 365


personel.IseAl()

