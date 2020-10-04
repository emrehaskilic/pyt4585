# dışarıdan kullanıcının adını ve soy adını alan bir metod yazınız.
# metod aldığı bu değerleri kullanarak bize mail aresi oluştursun

def Mail(isim,soyisim):
    
    mail =(f"{isim}.{soyisim}@hotmail.com").lower()
    print(mail)
adi = input("Lütfen İsmi giriniz:")
soyadi= input("Lütfen Soyismi giriniz:")    

Mail(adi,soyadi)

def MailAdres(isim,soyisim=None):
    if soyisim is None:
        mail = f"{isim}@hotmail.com"
    else:
        mail =(f"{isim}.{soyisim}@hotmail.com").lower()
    print(mail)
MailAdres("emre")    