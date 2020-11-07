// VAR OLAN BİR DATABASE İ SİLME

// use <databaseismi>
// db.dropDataBase()



// db ,çerisinde yer alan kayıtları listelemek için öncelikle database seçişlkmiş olması gerekir

// 1) Kayıtların Listelenmesi
//  1.1) use Theaters

// 2) Kolekiyon içerisinde yer alan tüm kayıtların listelenmesi
//  2.1) db.Games.find() => tüm kayıtları listeler
//  2.2) db.Games.find().pretty() => dizgün formatta listeler

// 3) Koleksiyon içerisinde yer alan kayıtların filtrelenerek listelenmesi
//  3.1) db.Games.find({"key":"value"})
// Ornek: db.Games.find({"Name":"FELATUN BEY İLE RAKIM EFENDİ"}).pretty()

// 4) Update işlemi bir kaydın belirli bir alanı ve ya tüm kayıtların belirli alanlarının değiştirilmesi işlemi
//  4.1) db.Games.update({"key":"value"},{$set:{"key":"value"}})
// 1.süslü parantez içeriği
//  {key filtreleme yaparken, neye göre yapacaksınız property adı : value => filtreleme yaparken verdiğiniz değer}
// 2. süslü parantez içeriği
//  {$set: => eşitle anlamına gelir {key : hangi alan değişecek : value => o alanın yeni değeri nedir?}}

// Ornek : db.Games.update({"Name":"FELATUN BEY İLE RAKIM EFENDİ"})

db.Games.update(
    {
        "Name":"FELATUN BEY İLE RAKIM EFENDİ"
    },
    {$set : {
        "ImageUrl" : "bilge adam"
    }}
    )
// güncellediğimiz kaydı listeliyoruz    
db.Games.find(
    {"Name":"FELATUN BEY İLE RAKIM EFENDİ"}
            ).pretty()



db.Games.update({"Id": 1},{$set : {"ImageUrl": "bilgeadam"}})
db.Games.update({"Id": 4},{$set : {"ImageUrl": "bilgeadam"}})
db.Games.update({"Id": 180},{$set : {"ImageUrl": "bilgeadam"}})
db.Games.update({"Id": 183},{$set : {"ImageUrl": "bilgeadam"}})


// db.Games.find({"ImageUrl":"bilgeadam"})


//Games içerisinde ımageurli bilge adam olan tüm kayıtların url kısmına www.bilgeadam.com

db.Games.update({"ImageUrl":"bilgeadam"},{$set: {"Url": "www.bilgeadam.com"}},{multi: true})

// ve ya

db.Games.updateMany(
    {
        "ImageUrl": "www.bilgeadam.com"
    },
    {
        $set : {"ImageUrl":"bilgeadam akademi"}
    }
)

db.Games.find({"ImageUrl":"bilgeadam akademi"}).pretty()

db.Games.find({"ImageUrl":"www.bilgeadam.com"}).pretty()


// var games = db.Games.find() = > oyun listesini değişkene atadık
// games.hasNext() => True dönüyorsa içeride okunacak değişken var anlamına gelirb