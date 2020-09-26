# dictionary() key value formatında dataları listelemek için kullanırılır
#Json formatında data tutar WebApi(servisler), JvScirpt,Angular,React(js-natice ), mongoDb gibi virçok platform desteklemektedir.

personeller = [
    {
"id" : 1,
"firstname" : "murat",
"lastname" : "vurakok",
"mail" : "muratvuranok@hotmail.com",
"phone" : "*905554443322",
"phones" : [
    {

        "no": "1234566",
        "title": "work",
        "description": ""

    }
          ]
    },
    {
        "id" : 2,
"firstname" : "mehmet",
"lastname" : "civelek",
"mail" : "mehmetcivelek@hotmail.com",
"phone" : "*905554443322"
    }
]
print(personeller[0])

#{'id': 1, 'firstname': 'murat', 'lastname': 'vurakok', 'mail': 'muratvuranok@hotmail.com', 'phone': '*905554443322', 'phones': [{'no': '1234566', 'title': 'work', 'description': ''}]}

print(personeller[0]["phones"][0])

#{'no': '1234566', 'title': 'work', 'description': ''}

print(personeller[0]["firstname"]) # 0. indexte olan personelin firstname ini verir

# dictionary listeden farklı olarak örneğin bir kullanıcının birden fazla bilgisini içinde nulundurur
kullanicilar = [
     {"username" : "admin"},
     {"username" : "ceo"},
     {"username" : "moderator"}
]

print(kullanicilar[0])
print(kullanicilar[0]["username"])

# dictionary içinde yer alan herhangi bir kaydı güncellemek isterseniz öncelikle

i = 0 # hangi eleman güncellenecek
key = "firstname"
value = "şahin"

oldRecord = personeller[i][key]

personeller[i][key] = value

newRecord = personeller[i][key]

print(oldRecord)
print(newRecord)


personeller.append(
    {
"id" : 3,
"firstname" : "Emre",
"lastname" : "Haskilic",
"mail" : "emrehaskilic1@gmail.com",
"phone" : "905059796816"
    }
)


print(personeller)

id = len(personeller)
indexNo = len(personeller) -1
firstname = input("Lütfen adınızı giriniz:")
lastname = input("Lütfen Soyadinizi giriniz:")
# mail = input("Lütfen Mail adresinizi giriniz:")
phone = input("Lütfen telefon no giriniz :")

personeller.append(

    {
        "id" : id,
        "indexNo" : indexNo,
        "firstname" : firstname,
        "lastname" : lastname,
        "mail" : f"{firstname}.{lastname}@gmail.com",
        "phone" : phone
    }
)




print(personeller)


print(personeller[len(personeller) -1])
