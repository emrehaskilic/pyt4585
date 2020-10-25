import datetime
now = datetime.datetime.now()

print(str(now)) #2020-10-25 15:41:43.298528

print(repr(now)) #2020-10-25 15:42:01.786708

class Personel:
    def __init__(self,isim):
        self.FirstName = isim

    def __repr__(self):
        return "Personel('{}',{})".format(self.FirstName, self.FirstName)

    def __str__(self):
        return "{}-{}".format(self.FirstName, self.FirstName)


per = Personel("Murat")

print(str(per))
print(per)
print(repr(per))

print(per.__str__()) # son kullanıcı için çıktı teslim eder
print(per.__repr__()) # developer için devam niteliğinde çıkktı teslim eder


