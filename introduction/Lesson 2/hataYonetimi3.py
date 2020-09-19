try:
    sayi = int(input("Lutfen sadece sayisal deger giriniz: "))
    print("gelen sayi:",sayi)
    sayi = sayi / 0
    print("islem sonucu")
except ValueError as ex:
    print("Lutfen Tekrar Deneyiniz")    
    print("Sistem mesajı:",ex)
except Exception as ex:
     print("islem hatasi") 
     print("Sistem Mesajı:", ex)  