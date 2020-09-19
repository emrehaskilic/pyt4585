try:
    sayi1 = int(input("lutfen sayi giriniz:"))
    sayi2 = int(input("lütfen sayi giriniz:"))

    sonuc = sayi1 / sayi2

except ValueError as mahmud:
    print("islem hatasi")
else:
    try:
        print(sayi1/sayi2)
        print("islem sonucu")
    except ZeroDivisionError as mahmud:
        print(mahmud)        