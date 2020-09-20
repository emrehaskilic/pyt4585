# Kullanici disardan not degeerini girecek ve girilen not 0 dan kucukse 0 dan kucuk not giremezsiniz uyarisi. 100 den büyükse 100 den buyuk not giremezsiniz uyarisi, girilen not 0a veya 100 e
# esit ve kucukse kullanıcıya girdigi notu gosteriniz.
try:

    ders_not = int(input("Lutfen notu giriniz: "))


    if(ders_not  < 0):
        print("0'dan kucuk deger giremezsiniz")
    elif(ders_not > 100):
        print("100'den buyuk deger giremezsiniz")
    else:
        print("Notunuz:",(ders_not))    
except:
        print("sadece not gireceksin ne kadar zor alabilir")

    

        


