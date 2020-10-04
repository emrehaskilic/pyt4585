# dışarıdan girilen değerin tek ve ya çift olma durumunu kontrol ediniz

# girilen değer cift ise -1 degerini tek ise 1 degerini 0 ise 0 değerini teslim ede metod yazdınız


def tekciftkontrolu(sayi):
    result = 0
    if(sayi == 0):
        result = 0
    elif sayi % 2 == 0:
        result = -1
    else:
        result = 1
    return result

# def tekciftsayikontrolu(sayi1):
#     if(sayi == 0):
#         return 0
#     elif sayi % 2 == 0:
#         return -1
#     else:
#         return 1

result = tekciftkontrolu(int(input("Lütfen sayiyi giriniz:")))

print(result)
       
          
    


    
