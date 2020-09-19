# Programcı Hataları
# Program Kusurları
# İstisnai Hatalar
# Mantiksal Hatalar (en zor hatalar mantıksal hatalardır.)

try:
    telefonNo = int(input("Lutfen telefon numaranizi giriniz: "))
    print("Tebrikler")
except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")    

except:
    print("İslem hatasi")