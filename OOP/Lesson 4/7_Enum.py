from enum import Enum, unique
@unique
class Icecek(Enum):
    Vanilya = 1
    Cikolata = 2
    Visne = 3
    Muzlu = 4
    # Kirazlı = 1
    Kirazli = 5

# ValueError: duplicate values found in <enum 'Icecek'>: Kirazlı -> Vanilya

for i in Icecek:
    print(i)    

for x,y in Icecek.__members__.items():
    print(x,y)    