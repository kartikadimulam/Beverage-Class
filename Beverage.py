class Beverage:

    def __init__(self, ounces= None, price=None):
        self.ounces = ounces
        self.price = price

    def updateOunces(self, newOunces):
        self.ounces = newOunces

    def updatePrice(self, newPrice):
        self.price = newPrice

    def getOunces(self):
        return self.ounces

    def getPrice(self):
        return self.price

    def getInfo(self):
        return "{} oz, ${:.2f}".format(self.ounces, self.price)
        
