import os 

class Clear:
    def ClearScreen(self):
        os.system(self)
        print("Ekran Temizlendi")

    def ClearString(self):
        arg = self.lower().replace("ş","s")
        return arg    


class MathLibrary:
    def Topla(self,*arg):
        toplam = 0
        for i in arg:
            toplam += i
        return toplam
class Employee:

    FirstName = ""  
    LastName = "" 
    def CreateMail(self):
        self.Mail = Clear.ClearString(f"{self.FirstName}.{self.LastName}@gmail.com")
      

class EmployeeServices:
    def IseAll(self):
        pass