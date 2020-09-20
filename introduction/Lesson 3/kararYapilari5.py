# MANTIKSAL OPERATORLAR

# and : sorguya katılan her bir kosulun saglanmasi durumu
# or : sorguya katılan herhangi bir kosulun saglanmasi durumu
# not : sorguya olumsuzluk katar, degil ise

username = input("Lutfen kullanici adinizi giriniz: ")

# if(username == "admin"):
#     password = input("Lutfen sifrenizi giriniz: ")
#     if password == "123456":
#         print("Giris yaptiniz")
#     else:
#         print("Kullanici sifrenizi kontrol ediniz")
        
# else:
#     print("Kullanici adinizi kontrol ediniz")    

username = input("Lutfen Kullanici Adinizi Giriniz: ")
password = input("Kullanici Sifrenizi giriniz: ")

if username == "admin" and password == "123":
    print("Tebrikler Giris Yaptiniz")
else:
    print("KULLANICI BILGILERINI KONTROL ET")




