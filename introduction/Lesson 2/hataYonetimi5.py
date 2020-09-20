try: 
    #db connection open
    sayi = int(input("Lutfen sayi giriniz:"))
    #connection error
    print("Tebrikler bro")
    #-db connection close-(finally sonrası gerek kalmaz)
except:
    print("vazgectim")    
    # -db connection close-(finally sonrası gerek kalmaz)
finally:
    print("her durumda bir defa tetiklenir")    
    # her iki durumda da yapılması gereken işlemleriniz var ise, bunu finally içersinde yazmanız kod tekrarını engelleyecekti
    