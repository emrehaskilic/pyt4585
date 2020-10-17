class Ogrenci:
    """
    bu alan zorunlu değildir. sadece document metodunu print ettiğinizde size bu sınıf hakkında bu alana ne yazdıysanız onu teslim eder
    """
    Adi = ""
    def NotVer(self,arg):
        print(self.Adi, f"Adlı öğrenciye {arg} notu verildi")

    def CezaVer(self,arg):
        print(self.Adi,f"Adlı öğrenciye {arg} cezası verildi")

    def YoklamaGirisi(self,arg):
        print(self.Adi,f"Adlı öğrenci derse {arg}")

ogrenci = Ogrenci()
ogrenci.Adi = "murat vuranok"
ogrenci.CezaVer("Disiplin") 
ogrenci.NotVer(100)
ogrenci.YoklamaGirisi("girdi")       
