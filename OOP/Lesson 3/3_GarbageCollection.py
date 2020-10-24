a = 40 # değeri 40 olan sayısal bir değişken tanımladık

print(type(a)) #<class 'int'>

b = a # b adında bir değişken tanımladık referansını a değişkeninden almasını sağladık


c = [b] #c değişkeni tanımlayıp b değerini eleman olarak atadık

print(type(c)) # list)

del a  #a değerini ram üzerinden sildik

# print(a) #NameError: name 'a' is not defined


print(b) #40 => a içerisinde yer alan veriyi b adındaki değilkene kopyaladığımızdan ram üzerinde b değişkeni için yeni bir alan oluşmuş olur

# o yüzden a değerini silsenizde b üzerindeki veriyi tutmaya devam eder.

b = 100 # b değişkeninin değerini 100 olarak değiştirdik


class Point():
    def __init__(self, x=0, y=0): #eğer sınıftanımlaması yapılırken değer verilmezse constructorda default değeri 0 dır
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name,"heap alan üzerinden silindi") 

point1 = Point()
point2 = point1
point3 = point1

print(id(point1),id(point2),id(point3))

c = 10

y = c # y değişkeninin c değişenine referans olarak verdiğimizden üzerinde sayısal tuttuğu değer ve referans adresini bize teslim eder.

print(id(c),id(y)) #4543720416 4543720416

y = 100 # y değişkenine yeni bir değer atadığından dolayı ram üzerinde yeni bir referans adresi oluşur.
print(id(y)) #4452484896


del point1

del point2

del point3