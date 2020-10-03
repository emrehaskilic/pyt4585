print("""
*****************
*TELEFON REHBERİ*
*****************
------------------------------
- Kayıt Eklemek İçin    : 1 - 
- Kayıt Güncellemek İçin: 2 - 
- Kayıt Listelemek için : 3 -
- Kayıt Aramak için     : 4 -
- Kayıt Silmek için     : 5 -
------------------------------
Tuşlayınız...
""")

rehber = [
             {
                "Id":1,
                "İsim":"Emre",
                "Soyisim" :"Haskılıç",
                "Telefon" :"+905059796816",
                "Mail" : "emrehaskilic1@gmail.com"
            }
              
        
]

i = 1
while i == 1:  #KİŞİ EKLEME SEÇENEĞİ
    soru = input("Lütfen yapmak istediğiniz işlemi seçiniz:")

    if soru == "1":
        id = len(rehber)+1      
        isim = input("İsim:")
        soyisim = input("Soyisim:")
        telefon = input("Telefon:")
        mail = input("Mail:")
         
        rehber.append(
                    {
                        "Id":id,
                        "İsim" :isim ,
                        "Soyisim" :soyisim,
                        "Telefon": telefon,
                        "Mail": mail

                    }
            )

        evethayir = str(input("kayıt başarıyla eklendi.✓ \n Devam etmek istiyor musunuz?:(E/H)"))
        if evethayir.upper() == "H":
            print("""
            *************
            * Güle Güle *
            *************
                """) 
            break 

    elif soru == "3": #KİŞİ LİSTELEME SEÇENEĞİ
        for kisi in rehber:
            print("ID:",kisi["Id"])
            print("İsim:",kisi["İsim"])
            print("Soyisim:",kisi["Soyisim"])
            print("Telefon:",kisi["Telefon"])
            print("Mail:",kisi["Mail"])

        evethayir = str(input("Devam etmek istiyor musunuz?:(E/H)"))
        if evethayir.upper() == "H":
            print("""
            *************
            * Güle Güle *
            *************
                """)  
            break
    elif soru == "5": #KİŞİ SİLME SEÇENEĞİ
        for kisi in rehber:
            print("ID:",kisi["Id"])
            print("İsim:",kisi["İsim"])
            print("Soyisim:",kisi["Soyisim"])
            print("Telefon:",kisi["Telefon"])
            print("Mail:",kisi["Mail"])
        
            index = int(input("Silmek istediğiniz idyi seçiniz:"))
            
            id = index -1
            rehber.pop(id)
            print("Kayıt Basarıyla Silindi ✓")
            evethayir = str(input("\n Devam etmek istiyor musunuz?:(E/H)"))
            if evethayir.upper() == "H":
                print("""
            *************
            * Güle Güle *
            *************
                """)  
                break
    elif soru == "2":
        for kisi in rehber:
            print("ID:",kisi["Id"])
            print("İsim:",kisi["İsim"])
            print("Soyisim:",kisi["Soyisim"])
            print("Telefon:",kisi["Telefon"])
            print("Mail:",kisi["Mail"])
            index = int(input("Güncellemek istediğiniz idyi seçiniz:"))
            id = index -1


            
           
            
            isim = input(kisi["İsim"])
            soyisim = input( kisi["Soyisim"])
            telefon = input(kisi["Telefon"])
            mail = input(kisi["Mail"])
        
            kisi.update(
                    {
                        
                        "İsim" :isim,
                        "Soyisim" :soyisim,
                        "Telefon": telefon,
                        "Mail": mail

                    }
                    )
            evethayir = str(input("\n Devam etmek istiyor musunuz?:(E/H)"))
            if evethayir.upper() == "H":
                print("""
            *************
            * Güle Güle *
            *************
                """)   
            break
    elif soru == "4": #KİŞİ ARAMA SEÇENEĞİ
        for kisi in rehber:
            name= input("Aramak istediğiniz İsmi Giriniz:")
            if name in kisi["İsim"]:
                print("ID:",kisi["Id"])
                print("İsim:",kisi["İsim"])
                print("Soyisim:",kisi["Soyisim"])
                print("Telefon:",kisi["Telefon"])
                print("Mail:",kisi["Mail"])
                evethayir = str(input("\n Devam etmek istiyor musunuz?:(E/H)"))
                if evethayir.upper() == "H":
                    print("""
                    *************
                    * Güle Güle *
                    *************
                        """)
                else:
                    break
            else:
                print("Aradığınız Kayıt Bulunamadı")  
                break