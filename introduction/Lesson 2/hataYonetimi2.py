
try: 
    sayi_bir = int(input("Lutfen 1. sayiyi giriniz: "))
    sayi_iki = int(input("Lutfen 2. sayiyi giriniz:"))

    toplam = sayi_bir + sayi_iki
    fark = sayi_bir - sayi_iki
    carpim = sayi_bir * sayi_iki
    bolum = sayi_bir / sayi_iki
    mod = sayi_bir % sayi_iki

    print(
        f"Sayilarin toplami : {toplam} \nSayilarin Farki: {fark}\nSayilarin Bolumu: {bolum}\n %%Sayilarin Bolum Farki : {mod}\nSayilarin Carpimi: {carpim}")

except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except FileExistsError:
    print("FileExistError")   
except:
    print("Tum hatalari kabul ediyorum")     
    
