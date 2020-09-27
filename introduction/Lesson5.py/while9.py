from random import randint
import os
os.system("clear")

counter = int(input("Lütfen kolon adedini giriniz:"))
index = 0

while index < counter:
    sayilar = []
    i = 0
    while i < 6:
        sayi = str(randint(1, 49))
        if sayi in sayilar:
            continue
        else:
            nmr = str(sayi)
            if(len(sayi) == 1):
                sayilar.append("0"+sayi)
            else:
                 sayilar.append(sayi)
        i += 1

    
       
sayilar.sort()
print(f"{index +1}.kolon =", "-".join(sayilar))
index += 1





    






