import pymongo

myClient = pymongo.MongoClient('mongodb://localhost:27017/')

myDb = myClient["PhoneBook"]
people = myDb["People"]
phones = myDb["Phones"]



person = {
    "firstname" : "murat",
    "lastname" : "vuranok",
    "phone" : "+901234567890",
    "mail" : "muratvuranok@bilgeadam.com"    

}

kisi_id = people.insert_one(person).inserted_id

phones_numbers = [
    {
        "name" : "work",
        "phone" : "+901234567890",
        "personID" : kisi_id

    },
    {
        "name" : "house",
        "phone" : "+901234567890",
        "personID" : kisi_id

    },
    {
        "name" : "cell",
        "phone" : "+901234567890",
        "personID" : kisi_id

    }

]

phones.insert_many(phones_numbers)

# myCollection.insert_one(person)
# print(myClient.list_database_name())



for x,y in people.find():
    print("_"*40)
    print()
    print(f"{x} : {y}")
    print()
    # telefon_numaralari = phones.find({"personId": : y._id})
    # for c,d in telefon_numaralari():
    #     print(f"{c} : {d}")
