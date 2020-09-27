# dışarıdan girilen metin içerisinde yer alan sesli ve sessiz harfleri ayrıştırınız ve 
#kullanıcıya bu elemanları gösteriniz

metin = input("Lütfen bir metin giriniz:")

sesliharfler = []
sessizharfler = []
sesli = ["a","e","i","u","o"]
i = 0


while i < len(metin):
    if metin[i] in sesli:
        sesliharfler.append(metin[i])
    else:
        sessizharfler.append(metin[i]) 
    i += 1       
print(f"Metin içerisindeki toplam sesli harf sayisi : {len(sesliharfler)}\n Metin içerisindeki sessiz harf sayisi: {len(sessizharfler)}")
   
