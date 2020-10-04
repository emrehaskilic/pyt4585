# dışarıdan bir sayısal dizi alacak, metot parametredeki yer alan elemanların toplamım kareköünü geriye teslim etsin

def ToplamKok(sayi):
    toplam = 0
    for i in sayi:
        
        toplam = toplam + i
        kok = toplam ** (1/2)
    return kok
dizi = [1,2,3,4,5,6,7,8,9]    

result = ToplamKok(dizi)

print(result)

