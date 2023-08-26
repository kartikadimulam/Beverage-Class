from Beverage import Beverage

class FruitJuice(Beverage):

    def __init__(self, ounces=None, price=None, fruits=None):
        super().__init__(ounces,price)
        self.fruits = fruits

    def getInfo(self):
        s=''
        for name in self.fruits[:-1]:
            s+=name+'/'
        s+= self.fruits[-1]
        s+= ' Juice, '
        s+=Beverage.getInfo(self)
        return s
            
