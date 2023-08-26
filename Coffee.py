from Beverage import Beverage

class Coffee(Beverage):

    def __init__(self, ounces=None, price=None, style=None):
        super().__init__(ounces, price)
        self.style = style

    def getInfo(self):
        s='{} Coffee, '.format(self.style)
        s += Beverage.getInfo(self)
        return s
    
        
