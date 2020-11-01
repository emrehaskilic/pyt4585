/*

1) show dbs           : server içerisinde yer alan database leri görüntüler
2) use <database adı> : çalışmak itediğiniz database in adını vermeniz yeterlidir. Not: küçük
büyük harf duyarlılığı vardır.
3) show collections   : database içerisinde yer alan koleksiyonları(table) gösterir.


*/

// user kisiler => kisiler database'ini secili hale getirdik

// 1) use TelefonRehberi => telefon rehberi adında bir db oluşturduk
/* 2) 

    db.Kisiler.insert({
        "firstname" : "emre",
        "lastname" : "haskilic",
        "mail" : "emrehaskilic@gmail.com",
        "phone" : "+9050597996816",
        "phones" : [

            {   
                "name" : "is",
                "phone" : "*50846554663"

            },
            {
                "name" : "ev",
                "phone" : "+90544056452"

            },
            {
                "name" : "okul",
                "phone" : "+90505124578"
            }
        ]

})

*/

// 3) db.Kisiler.find()
// 4) db.Kisiler.find().pretty()