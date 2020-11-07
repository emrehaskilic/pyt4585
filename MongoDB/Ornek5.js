// Equality ==

// db.Products.find({"ProductID" : 77}) => ÜRÜN İD Sİ 77 OLAN ÜRÜNÜ GÖSTERİR


// Ctegory değeri 8 olan ürünleri listeleyiniz

db.Products.find({"CategoryID": 8})

// less than 
// fiyatı 50 dolardan az olan dürünlerin listelenmesi

db.Product.find({"UnitPrice": {$lt:50}})


// ürünlerin sıralanması

// 1. SIRALAMA ŞEKLİ
// Ascending *1 A'dan Z'ye 0'dan 9'a şeklinde sıralama yapar
// 2. SIRALAMA ŞEKLİ
// Descending -1 Z'den A'ya 9'dan 0'a şeklinde sıralama yapar.



db.Products.find().pretty().sort({"UnitPrice" : 1}) // ascending

db.Products.find().pretty().sort({"UnitPrice" : -1}) // descending


// less than equal >=

// fiyat 50 lira veya altı olacak ve küçükten büyüğe sıralanacak
db.Products.find({
    "UnitPrice" : {$lte : 50}
}).pretty().sort({
    "UnitPrice" : 1
})

// grather than >

// fiyatı 100 liradan büyük olan ürünleri listeleyiniz

db.Products.find({
    "UnitPrice": {$gt:50}
}).pretty().sort({
    "UnitPrice" : 1
})

// grather than equal <=

// fiyatı 60 ve 60 a eşit olan ürünleri Z'den A'ya sırala

db.Products.find({
    "UnitPrice": {$gte:60}
}).pretty().sort({
    "ProductName" : -1
})

// And ve Or kullanımı:

//  and kullanımı:
// fiyatı 30$ dan büyük stok adedi 100 den küçük olan ürünlerin listelenmesi

db.Products.find({
    $and:
    [
        {
            "UnitPrice" : {$gte : 30}
        },
        {
            "UnitsInStock" : {$lte : 100}
        }
    ]

                })

db.Products.find({})
db.Products.find({ $and: []})
db.Products.find({ $and: [{},{}]})
db.Products.find({ $and: [{"UnitPrice" : {$gte:30} },{}]})
db.Products.find({ $and: [{"UnitPrice" : {$gte:30} },{"UnitsInStock": {$lte : 100}}]})
                