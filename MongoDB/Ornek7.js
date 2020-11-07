db.Categories.aggregate({ // ana tabloyu çağırıyoruz

    $lookup :{
        from: "Products", // join yapılacak
        localField : "CategoryID", // ana tablo içerisinde yer alan primary key(birincil anahtar)
        foreignField: "CategoryID", // fOREİGNkey ikincil anahtar ürünler tablosunda kategoriyi temsil eden alan
        as : "Products" //sorgu sonucu kategoriye bağlı ürünler listelenirken verilecek olan isim, dilediğiniz ismi verebilirsiniz
    }    

})

db.Categories.aggregate(
    
    { 

    $lookup:{
        from: "Products", 
        localField : "CategoryID", 
        foreignField: "CategoryID", 
        as : "Products" 
    }    

}).pretty()
