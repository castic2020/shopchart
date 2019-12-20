import time
Type=1
Weight=1
UnitPrice=2
def getGoodsType():
    print("I'm going to identify the type of goods.")
    return(Type)
def getWeight():
    print("I will weigh the goods.")
    return(Weight)
def getUnitPrice():
    print("I will check the unit price of this product")
    return(UnitPrice)
def calculation():
    TotalPrice =UnitPrice**Weight
    print("TotalPrice",TotalPrice)


while True:
    getGoodsType()
    getUnitPrice()
    getWeight()
    calculation()
    time.sleep(1)