import pymongo
from bson import ObjectId

__DATABASE_NAME = "TelefonRehberi"
__COLLECTİON_NAME = "People"


def ConnectAtlas():

    return pymongo.MongoClient("mongodb+srv://emrehas:159357@cluster0.bhegq.mongodb.net/TelefonRehberi?retryWrites=true&w=majority", ssl_cert_reqs='CERT_NONE')
    

# python3 -m pip install dnspython

def Add(person):
    myClient = ConnectAtlas()
    myDb = myClient[__DATABASE_NAME]
    myCollection = myDb[__COLLECTİON_NAME]
    myCollection.insert_one(person.__dict__)

def Delete(param):
    myClient = ConnectAtlas()
    myDb = myClient[__DATABASE_NAME]
    myCollection = myDb[__COLLECTİON_NAME]
    query = {"_id": ObjectId(param)}
    myCollection.delete_one(query)

def List():
    myClient = ConnectAtlas()
    myDb = myClient[__DATABASE_NAME]
    myCollection = myDb[__COLLECTİON_NAME]
    c = myCollection.find()
    print(f"{'_id':30}{'Firstname':30}{'Lastname':30}{'Phone':30}{'Mail':30}")
    print("_"*150,"\n")
    for x in myCollection.find():
        body = ""
        for key, value in x.items():
            body += f"{str(value):30}"
        print(body)
           
            
    
