class Cup1:
    def __init__(self):
        self.color = None # public variable
        self.content = None # public variable
    def fill(self,beverage):
        self.content = beverage

    def empyt(self):
        self.content = None

    def __str__(self):
        return self.color + " " + self.content
cup1 = Cup1()
cup1.color= "Red"
cup1.content = "Tea"

print(cup1)
print(cup1)

cup1.empyt()
cup1.content = "coffee"


class Cup2():
    def __init__(self):
        self.color = None # public variable
        self._content = None #protected variable
    def __str__(self):
        return f"{self.color}  {self._content} "    





cup2 = Cup2()

cup2.color = "Yellow"
print(cup2)
# yanlış kullanım şeklidir
cup2._content = "tea" # _ ile işaretlenmişsse korumalı olarak işaretlenmiş anlamına gelir kullanım gereği instance aldıktan sonra değer ataması yapmamanız gerekmektedir.
# eğer dışarıdan değer ataması yapacaksanız constructor içerisinden gönderebilirsiniz.

# _ bir alt ire ile işaretlişse protected anlamına gelir ve bu değere sınıf üzerinden değil miras verilen sınıf üzerinden erişim sağlanır.
print(cup2)


class Cup3:
    def __init__(self):
        self._color = None # korumalı (protected) variable
        self.__content = None # gizli [private] variable

    def __str__(self):
        return f"{self._color}  {self.__content}"

cup3 = Cup3()
cup3._color = "Red"


print(cup3)  # çıktısı => Red  None

print(cup3.__content)  # AttributeError: 'Cup3' object has no attribute '__content'
