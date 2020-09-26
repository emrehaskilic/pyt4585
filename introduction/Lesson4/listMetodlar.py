# dizi üzerinde islemler yapmak için o nesneye ait metodlar kullanılır

#.append() => dizi içerisine eleman eklemek için kullanılır (JavaScipttede geçerlidir)
#.appned() ekleme islemişni dizinin sonuna ekleyerek gerceklestirir
# 

sehirler = [] #boş dizi

sehirler.append("ankara")
sehirler.append("edirne")
sehirler.append("istanbul")
print(sehirler[:])

#---------------------------------------------
#.insert() => dizi içerisinde belirli bir alana veri eklemek için kullanılır

sehirler.insert(1,"bursa") # bu kodlar 1. indekse eleman eklenir yani ['ankara', 'bursa', 'edirne', 'istanbul'] yeni listemiz bu sekilde olur

print(sehirler)

#---------------------------------------------

# .pop() => dizi içerisinden eleman silme, parametre verilirse verilen index degerindeki elemanı siler
# parametre verilmezse dizinin en son elemanını siler
#pop() sildigi elemanı geriye teslimm eder
print(sehirler)

sehirler.pop(1)
print(sehirler)
sehirler.pop()
print(sehirler)
print(sehirler.pop())
#---------------------------------------------

arabalar =["mercedes","bmw","range rover","bugatti",
            "aston martin","tofaş","kartal","serce"]

# .remove() =Z dizi içerisinden eleman silmekle mükellef diğer bir metodumuzdur,, pop() metodundan farkı
# birisi index mekanizması üzeribdbe sşlme işlemi yaparken remove() object parametre alarak isleme devam eder
# 
# dizi icerisinde birden fazla aynı deger var ise soldan sağa ilk bulduğu elemanı siler
# remove metodu pop metodu gibi silinen elamnı gerşye teslim etmez void metodttur

print(arabalar[:])
print(arabalar.remove("tofaş"))
print(arabalar[:])

#-----------------------------------------------

# #.sort() => dizi icerisinde yer alan elemanları Adan Zye 0 dan 9 a sıralar
# print(arabalar)
# arabalar.sort()
# print(arabalar[:])

#------------------------------------------------

#reverse() => dizi içerisindeki elemanları sıralamadan tersine cevirir

print(arabalar)
arabalar.reverse()
print(arabalar)

#------------------------------------------------

#.len() => dizinin uzunluğunu teslim eder

print(len(arabalar))
del arabalar #sehirler dizisini tamamen silmiş olursunuz. bu satır derlendikten sonra alt satırlarda arabalar dizisine ulaşamayacaksınız
print(len(arabalar))
print(arabalar)