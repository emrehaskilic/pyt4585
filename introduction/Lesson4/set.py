# .set() => c# dan gçrmediginiz hatta merak edip bakmayacagınız odev bile versem bahane bulacagınız nesnemiz :)
# içerisinde unique deger tutar yani turlce meali aynı elemandan 2 tane bulundurmaz

mySet = set()

print(mySet)

mySet.add(1)
mySet.add(2)
mySet.add(3)
print(len(mySet))
mySet.add(1)
mySet.add(2)
mySet.add(3)
print(len(mySet))

print(mySet)
