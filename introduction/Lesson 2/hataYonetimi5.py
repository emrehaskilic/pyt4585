try: 
    #db connection open
    sayi = int(input("Lutfen sayi giriniz:"))
    #connection error
    print("Tebrikler bro")
    #db connection close
except:
    print("vazgectim")    
    # db connection close
finally:
    print("her durumda bir defa tetiklenir")    
    