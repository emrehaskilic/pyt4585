# birden fazla elemala çalışacak isek tek tek değişken tanımlamak yerine dizi kullanuyoruz.
# Tanumlama şekli:

sehirler = ["istanbul","edirne","konya","rize",
            "ankara","eskişehir","adana","kayseri"]

# NOT: bir dizinin maksimum index degeri o dizinin eleman sayisi -1 dir
# 1 2 3 4 5 6 7 8 => eleman sayisi
# 0 1 2 3 4 5 6 7 => index

            #eleman sayısı => dizi içerisindeki toplam adet
            #indez degeri => dizi içerisinde yer alan herhangi bir elemana ulaşma sekli

print(sehirler[-1]) #sehirler dizisinin ilk elemanını yazdırdık  

# dizinin son elemanıın ekrana yazdırınız

index = len(sehirler)  # toplam eleman sayısının teslim eder

index = len(sehirler) -1 # 0 dizinin maksinin index degerinin temsil eder.

print(sehirler[index])

print(sehirler[2:7]) 
# birinci parametrede verilen index degeri(dahil) #
# 2. parametrede verilen indez degerinin bir alt degerimne kadar olan elemanları listeler.

# dizinin tüm elemanlarını ekrana yazırmak istersen

# print(sehirler[:])

# print("adana" in sehirler) #adana parametresi dizi içerisinde geçmektemidir? geçmemektemidir?

# #Kullanici disardan sehir adi girecek var ise bu sehir dizi içerisinde yer almaktadır yok ise bu dizi sehir içerinde yer almamaktadır.

# city = str(input("Lütfen bir sehir adi giriniz:"))

# sonuc = "Girmiş oldugunuz  sehri index içindedir " if city in sehirler else "girmiş olduğunuz  sehri index dışındadır " 
# print(sonuc)


myList1 = ["Sehirler dizisi"]
print(myList1)

myList2 = ["arabalar dizisi"]
print(myList2)

myList3 = ["renkler dizisi"]
print(myList3)

result = list(zip(myList1,myList2,myList3))
print(result)




