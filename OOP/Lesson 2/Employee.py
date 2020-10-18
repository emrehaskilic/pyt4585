class Calisan:
    def __init__(self,firstname, lastname, salary, department, age=18):
        self.FirstName = firstname
        self.LastName = lastname
        self.Salary = salary
        self.Department = department
        self.Age = age

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"  

    def BilgiGoster(self):
        return f"Personelin Adı: {self.FirstName}\nPersonelin Soyadi: {self.LastName}\nPersonelin Maaşı: {self.Salary}\nPersonelin Departmanı: {self.Department}\nPersonelin Yaşı: {self.Age}"
    def ZamYap(self,yapilanZam):
        print("Çalışanın maaşına zam yapıldı")
        maas = self.Salary
        self.Salary += yapilanZam
        print(f"{self} Adlı personelin {maas} olan maaşı {self.Salary} olarak düzenlendi ")    

    def Oryantasyon(self,YeniDep):
        print("Personel Departmanı Değiştirildi")
        departman = self.Department
        yeni_departman = YeniDep
        print(f"{self} Adlı Personel {departman} departmanından {yeni_departman} departmanına transfer edilmiştir")    

personel = Calisan("Emre","Haskilic",123,"Yazilim",90)

print(personel)
print(personel.BilgiGoster())
personel.ZamYap(10000)
personel.Oryantasyon("İnsan Kaynakları")