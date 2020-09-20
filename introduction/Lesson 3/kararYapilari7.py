
ürün = str(input("Urun adi giriniz: ")).lower().replace(" ","")

if len(ürün) > 1 :
    sonuc = "Aradiginiz {}, {} reyonundadir"
    if ürün == "domates" or ürün == "biber" or ürün == "patlican":
        sonuc = sonuc.format(ürün,"sebze")
    elif ürün == "sampuan" or ürün == "parfüm" or ürün == "deodorant":
        sonuc = sonuc.format(ürün,"kozmetik")
    elif ürün == "ceptelefonu" or ürün == "televizyon" or ürün == "bilgisayar" or ürün == "kulaklik":
        sonuc = sonuc.format(ürün,"teknoloji")
    else:
        sonuc = "gecersiz ürün adı"
    print(sonuc)    
else:
    print("Lutfen bir ürün adı giriniz")