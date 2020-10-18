class ParentClass():
    def send_message(self,message):
        print("parent class mesaj servisine hoş geldiniz: ",message)

class BaseClass(ParentClass):
    def send_message(self,message):
# override var olan bir nesneti yeniden dizenlemek aynı isimde bu sınıf içerisinde tanımlamanız yeterlidir. Eğer miraas aldığınız sınıf içerisinde gelen değerede ihtiyacubuz varsa super()
# metodnu kullanarak o değeri elde edebilirsiniz.        
        super().send_message("Birönceki sınıfın mesaj metdounu tetikledik")
        print(message)


parent = ParentClass()
parent.send_message("Parent sınıfı içerisindeki mesaj yazılmaktadır")    

base = BaseClass()
base.send_message("Base sınıfından gönderilen mesaj")