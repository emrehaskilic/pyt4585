// db oluşturmak
use TelefonRehberi

db.Kisiler.insertMany([

    {
        "firstname" : "murat",
        "lastname" : "vuranok",
    },
    {
        "firstname" : "ahmet",
        "lastname" : "şahin",

    }
])

/*
{
	"_id" : ObjectId("5fa693d04613541edf93ccbb"),
	"firstname" : "murat",
	"lastname" : "vuranok"
}
{
	"_id" : ObjectId("5fa693d04613541edf93ccbc"),
	"firstname" : "ahmet",
	"lastname" : "şahin"
}
8*/


db.Telefonlar.insertMany([

    {
        "name": "work",
        "number" : "+901234567898",
        "personId" : ObjectId("5fa693d04613541edf93ccbc")
    },
    {
        "name": "home",
        "number" : "+901234567898",
        "personId" : ObjectId("5fa693d04613541edf93ccbc")
        
    },
    {
        "name": "cell",
        "number" : "+901234567898",
        "personId" : ObjectId("5fa693d04613541edf93ccbc")
    }

])

/*
{
	"_id" : ObjectId("5fa696534613541edf93ccbd"),
	"name" : "work",
	"number" : "+901234567898",
	"personId" : "5fa693d04613541edf93ccbb"
}
{
	"_id" : ObjectId("5fa696534613541edf93ccbe"),
	"name" : "home",
	"number" : "+901234567898",
	"personId" : "5fa693d04613541edf93ccbb"
}
{
	"_id" : ObjectId("5fa696534613541edf93ccbf"),
	"name" : "cell",
	"number" : "+901234567898",
	"personId" : "5fa693d04613541edf93ccbb"
}

*/

db.Kisiler.aggregate(
    
    { 

    $lookup:{
        from: "Telefonlar", 
        localField : "_id", 
        foreignField: "personId", 
        as : "TelefonNumaralari" 
    }    

}).pretty()
