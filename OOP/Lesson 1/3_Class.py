class Student:
    """
    self: Sınıf içerisinde yer alan metodların diğerlerinden farkı hangi sınıf içerisinde çalıştığını belirtmesidir. 
    Self anahtar kelimesini vererek metodun bu sınıf içeriinde çalıştığını belirtmiş oluruz.
    Tanımlama yapılırken eklenir fakat kullanım sırasında python bunu bizim için kendisi yapacaktır.
    """

    FirstName = ""

    def GiveNot(self, student):
        print(student, "Adlı öğrenciye not girişi yapıldı")

    def GivePunish(self,student):
        print(student,"Adlı öğrenciye ceza verildi")

    def Check(self,student):
        print(student,"Adlu öğrencinin yoklaması girildi")

student = Student()

student.FirstName = "Murat"


student.GiveNot(student.FirstName)