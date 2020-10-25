class Personel:
    def __init__(self,firstname,lastname):
        self.FirstName = firstname
        self.LastName = lastname
    @property
    def email(self):
        return f"{self.FirstName}.{self.LastName}@gmail.com".lower()
    @property # getter metodu => gerşye datayı teslim eder.
    def FullName(self):
        return f"{self.FirstName} {self.LastName}"    

    
    @FullName.setter
    def FullName(self,parametre):
        ad, soyad = parametre.split(" ") # dışarıdan girilen ayrık 2 kelimeyi ad ve soyad değişkenine atama yapacak kullanıcı "Emre Haskilic girerse" ad = Emre soyad= Haskilic 
        self.FirstName = ad
        self.LastName = soyad
    
    # datanın içerisini temizler    
    @FullName.deleter
    def FullName(self):  
        print("kişiye ait kayıt silindi")
        self.FirstName = None
        self.LastName = None


personel = Personel("Emre", "Haskılıc")

print(personel.FirstName)
print(personel.LastName)

print(personel.email)
# mail bir motot olduğundan direkt olarak personel.email şeklinde çağırırsanız sşze sınıfın özelliklerini teslim eder.
#<bound method Personel.email of <__main__.Personel object at 0x10b526e50>>

#eğer metod içerisinde ki değeri teslim almak istiyorsanız aşağıdaki gibi teslim etmeniz gerekir


#BİZ BUNU METODU PROPERTY GİBİ KULLANMAK İSTİYORSAK **DECORE** ETMEMİZ GEREKİR. O yüzden sınıfın içerisine bir tane mail metodu ekledik ve pro
#pert oalrak decore ettik print(personel.mail)

print(personel.FullName) #@property olarak tanımladığımız için böyle çıktı alırız

personel.FullName = "Ahmet Şahin"
print(personel.FirstName)
print(personel.LastName)
print(personel.email)


del personel.FullName
print(personel.FullName)