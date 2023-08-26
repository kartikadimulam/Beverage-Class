


from Beverage import Beverage
from DrinkOrder import DrinkOrder
from FruitJuice import FruitJuice
from Coffee import Coffee


def test_beverage_updateOunces():
    bev = Beverage(10, 2.5)
    bev.updateOunces(15)
    assert bev.getOunces() == 15

def test_beverage_updatePrice():
    bev = Beverage(10, 2.5)
    bev.updatePrice(3.0)
    assert bev.getPrice() == 3.0

def test_beverage_getInfo():
    bev = Beverage(12, 1.75)
    assert bev.getInfo() == "12 oz, $1.75"

def test_writeup_drinkorder():
    c1 = Coffee(8, 3.0, "Espresso")
    juice = FruitJuice(16, 4.5, ["Apple", "Guava"])
    order = DrinkOrder()
    order.addBeverage(c1)
    order.addBeverage(juice)
    assert order.getTotalOrder() == '''Order Items:
* Espresso Coffee, 8 oz, $3.00
* Apple/Guava Juice, 16 oz, $4.50
Total Price: $7.50'''
    
