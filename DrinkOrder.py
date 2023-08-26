
class DrinkOrder:

    def __init__(self):
        self.drinks = []

    def addBeverage(self, beverage):
        self.drinks.append(beverage)

    def getTotalOrder(self):
        s = 'Order Items:\n'
        total = 0.0
        for beverages in self.drinks:
            s+="* " + beverages.getInfo() + "\n"
            total += beverages.price
            
        s += "Total Price: ${:.2f}".format(total)
        return s

    
