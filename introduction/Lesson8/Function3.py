# dışarıdan isim ve soyisim alan bir metod yazınız

#metod parametredeki kelimenin ilk 2 harfini büyük kalanını küçük alsın 

# 2. parametrenin hepsini küçük alıp a harflerini e ile değiştirip bize @hotmail.com mail olarak teslim etsin



def Mail(firstname,lastname):
    
    if len(firstname) <= 2:
        firstname = firstname.upper()
    else:
        firstname = f"{firstname[0:2].upper()}{firstname[2:].lower()}"
    
    lastname = lastname.lower() .replace("a","e")

    return f"{firstname}.{lastname}@hotmail.com"    
isim = input("Lütfen adınızı giriniz:") 
soyisim = input("Lütfen soyadınızı giriniz:")
mail = Mail(isim,soyisim)

print(mail)

    
    