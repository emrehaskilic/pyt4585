from enum import Enum, unique, auto

@unique # sınıf içerisinde aynı indeks değerine sahip ikinci bir eleman yer alamaz
class Icecek(Enum):
    Vanilya = auto()
    Cikolata = 2
    Visne = auto()
    Muzlu = 4
    # Kirazlı = 1
    Kirazli = 75
    Cilekli = auto()


liste = list(Icecek)

print(liste)