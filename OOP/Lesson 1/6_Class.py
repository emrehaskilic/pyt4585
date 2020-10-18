from Helpers import *

Clear.ClearScreen("clear")

result = MathLibrary.Topla("",1,2,3,4,5,6)

print(result)

mail = "EMREHAŞKİLİŞ@HOŞMAİL.COM"

mail = Clear.ClearString(mail)
print(mail)


emp = Employee()

emp.FirstName = "Emre"
emp.LastName = "Haskilic"
emp.CreateMail()


print(emp.Mail)