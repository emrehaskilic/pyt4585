print("""
***********************************
*                                 *                                  
*      EMRE BOOKS & COFFEE         *
*                                 *
***********************************

""")
sayi = int(input("""
                                 >
  ////////////////////////       >  >
  /Siparis Sayisi giriniz/ ====>>>  >  > :
  ////////////////////////       >  >
                                 >
"""))
birim_fiyat = 5

fiyat = sayi * birim_fiyat

son = ("""
     -------------------------------
     -- Verilen Sipariş Adedi: {} 
     -- Birim Fiyat          : {} 
     -- indirimsiz Fiyat     : {} 
     -- İndirimli Fiyat      : {} 
     -- Toplam Kazancınız    : {}
     -------------------------------
& BİZİ TERCİH ETTİĞİNİZ İÇİN TEŞEKKÜRLER &
""")

if sayi <= 0:
    print("siparisi kontrol ediniz")
elif sayi > 1 or sayi <= 20:
   son1 = (fiyat * 0.95)
   kazanc1 = fiyat - son1
   print(son.format(sayi,birim_fiyat,fiyat,son1,kazanc1))
    
elif sayi > 21 or sayi <=50:
    son2 = fiyat * 0.90
    kazanc2 = fiyat - son2
    print(son.format(sayi,birim_fiyat,fiyat,son2,kazanc2))
elif sayi > 51 or sayi <= 80:
    son3 =  (fiyat * 0.85)
    kazanc3 = fiyat - son3
    print(son.format(sayi,birim_fiyat,fiyat,son3,kazanc3))
elif sayi > 81 or sayi <= 100:
    son4 = (fiyat * 0.80)
    kazanc4 = fiyat - son4
    print(son.format(sayi,birim_fiyat,fiyat,son4,kazanc4))
elif sayi > 100 :
    son5 = (fiyat * 0.75)
    kazanc5 = fiyat - son5
    print(son.format(sayi,birim_fiyat,fiyat,son5,kazanc5))     
    



