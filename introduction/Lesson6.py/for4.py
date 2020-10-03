# kullanıcı dışarıdan şifre gidecek girilen şifre 3 ile 8 aralığında ise şifremiz
# şifreniz: şifre olarak onaylandı
# kullanıcı 3 denemenin sonunda beceremezse, motive edici bir mesaj veriniz :)




for i in range(3): # bağlangıç değeri vermezseniz default olarak 0 dan başlayacaktır
    password = input("Lütfen 3 ile 8 aralığında bir sifre seçiniz: ")
    if i == 2:
        print("sifrenizi 3 defa yanlış girdiniz tekrar dene")
    elif not password:
        print("sifre olusturabilmen için klavyede tusa basman gerekli")
    elif len(password) in range(3,8):
        print(f"Şifreniz: {password} olarak belirlenmiştir")    
        break  # break anahtar kelimesi bağlı olduğu yapıyı sonlandırır



     