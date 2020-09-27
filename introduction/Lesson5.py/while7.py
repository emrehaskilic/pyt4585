#dizi içerisinde yer alan tek sayiları bir diziye çift sayilari ayrı bir diziye ekleyiniz 
#islem sonunda toplamda dizi içersinde kaç eleman var kullanıca bildirim veriniz

# orn tek sayiları adedei : 

sayilar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,10]
teksayilar = []
ciftsayilar = []
i = 0


while i < len(sayilar):
    
    if i % 2 == 0:
        ciftsayilar.append(sayilar[i])
    else:
        teksayilar.append(sayilar[i])   
    i += 1   
print(f"Tek sayilarin toplanı : {len(teksayilar)}\nÇift sayilarin toplanı : {len(ciftsayilar)}")
print(teksayilar)
print(ciftsayilar)
    
        
    

