#dışarıdan girilen metin içerisinde yer alan sesli ve sssiz harflerin toplamını kullanıcıya bildiriniz


def SesliKontrol(param):
    sesli_harfler = ["a","e","ı","i","u","ü","o","ö"]
    liste = list(param)
    sesli = 0
    sessiz = 0
    for i in liste:
        if i in sesli_harfler:
            sesli += 1
        else:
            sessiz += 1
    print(f"\nMetin içerisinde yer alana sesli harflerin toplam sayısı:{sesli}\n\nMetin içerisinde yer alan sessiz harflerin toplam sayısı:{sessiz}")            
SesliKontrol("EmreHas")    