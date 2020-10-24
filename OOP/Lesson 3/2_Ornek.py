class  BasePhone():
    def __init__(self):
        # protected
        self._phoneType = "Ahizeli Telefon"
        self.connectionType = None
        self.brand = None
        self.phoneType = self._phoneType
    def __str__(self):
        return f"Telefonun bağlantı türü:{self.connectionType}\nTelefonun Markası:{self.brand}\nTelefonun Türü:{self._phoneType}"

basephone = BasePhone()

basephone.connectionType = "Kablolu Bağlantı"
basephone.brand = "Alcatel"
print(basephone)

class MobilPhone(BasePhone):
    def __init__(self):
        self.HasCamera = None
        self._phoneType = "Mobil Bağlantı"


mobil = MobilPhone()

mobil.HasCamera = True
mobil.brand = "Nokia"
mobil.connectionType = "Mobil connection available"

class SmartPhone(MobilPhone):
    def __init__(self):
        self.frontCamera = None
        self._phoneType = "Smart Phone"

smartphone = SmartPhone()

smartphone.brand = "Apple"
smartphone.connectionType = "5g"
smartphone.frontCamera = True
smartphone.HasCamera = True       
