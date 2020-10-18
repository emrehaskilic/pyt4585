from Employee import Calisan

class Yonetici(Calisan): #yönetici sınıfına çalışan sınıfını miras veriyoruz
    def __init__(self,firstname, lastname, salary, department, age=18,employeeCount=0):
        self.FirstName = firstname
        self.LastName = lastname
        self.Salary = salary
        self.Department = department
        self.Age = age
        self.EmployeeCount = int(employeeCount)
    def BilgiGoster(self):
        # super() miras aldığınız sınıfın değerini teslim eder.
        # Calisan sınıfının içerisinde metodu çalıştırıp gelen değeri teslim alıyoruz
        info = super().BilgiGoster()
        return f"{info}\n Yöneticinin Toplam Çalışan Sayısı: {self.EmployeeCount}"
    def Print_Base(self):
        for base in self.__class__.__bases__:
            print("Bu sınıfın miras aldığını sınıf: ", base.__name__)
    def __str__(self):
        info = super().__str__()
        return f"{info} Yöneticidir"        


yonetici = Yonetici("Ahmet","Şahin",10000,"Yazılım",90,10)

info = yonetici.BilgiGoster()
print(info)
yonetici.BilgiGoster() # TypeError: __init__() missing 4 required positional arguments: 'firstname', 'lastname', 'salary', and 'department'
yonetici.Print_Base()
print(yonetici)