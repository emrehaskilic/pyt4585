from enum import Enum, auto, Flag


# flag olarak işaretlediğinizde yine enumdır fakat index numaralı benzersiz ve birden fazla enum değerinin toplamı içerdeki bir enum deperine karşılık gelmemelidir
# + bir enum değerine birden fazla enum deperi yükleyebilirsiniz


class Renkler(Flag):      #enum           #flag
    Kirmizi = auto()      #1              #1
    Sari = auto()         #2               #2      
    Mavi = auto()         #3               #4
    Pembe = auto()        #4               #8
    Yesil = auto()        #5               #16
    Beyaz = auto()        #6               #32
    Turuncu = auto()      #7               #64
    GokKusagi = Kirmizi | Mavi | Turuncu | Pembe # indeks değeri 77 dir
#[<Renkler.Kirmizi: 1>, <Renkler.Sari: 2>, <Renkler.Mavi: 3>, <Renkler.Pembe: 4>, <Renkler.Yesil: 5>, <Renkler.Beyaz: 6>, <Renkler.Turuncu: 7>]
liste = list(Renkler)

print(liste)