import socket
from datetime import datetime

hostname = socket.gethostname()
print(hostname)
ip = socket.gethostbyname("")

print(ip)

class CoreEntitiy():
    Id = 0
    def __init__(self):
        self.CreatedDate = datetime.now()
        self.CreatedComputerName = socket.gethostname()
        self.CreatedIP = socket.gethostbyname("")

class Category(CoreEntitiy):
    CategoryName = ""
    Description = ""

class Product(CoreEntitiy):
    ProductName = ""
    UnitPrice = 0
    UnitsInStock = 0

core = CoreEntitiy()      

product = Product()
product.Id = 1
product.ProductName = "Beverages"
product.UnitPrice = 12
product.UnitsInStock = 100


category = Category()
category.Id = 1
print(product.CreatedDate)
print(category.CreatedDate)


