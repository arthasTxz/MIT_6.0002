
class Items():
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
    
    def getWeight(self):
        return self.weight

    def getPrice(self):
        return self.price

    def getDensity(self):
        return self.price/self.weight

    def __str__(self):
        return self.name + ': <' + str(self.price)\
                 + ', ' + str(self.weight) + '>'


def build_bag(names, prices, weight):
    bag = [Items(names[x], prices[x], weights[x]) for x in range(len(prices))]
    return bag

def greedy(items, maxCost, keyFunction, descending):

    itemsCopy = sorted(items, key=keyFunction, reverse = descending)
    result = []
    totalValue, totalCost = 0.0 , 0.0
    for i in range(len(itemsCopy)):
        if (totalCost+itemsCopy[i].getWeight()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getWeight()
            totalValue += itemsCopy[i].getPrice()
    return (result, totalValue)

def testGreedy(items, constrain, keyFunction, descending=True):
    taken, val = greedy(items, constrain, keyFunction, descending)
    print('Total value of items taken =', val)
    for item in taken:
        print('   ', item)

def testGreedys(items, maxUnits):
    print("Algo")
    testGreedy(items, maxUnits, Items.getPrice)
    print("Algo 1")
    testGreedy(items, maxUnits, Items.getWeight, False)
    print("Algo 2")
    testGreedy(items, maxUnits, Items.getDensity)

names = ["clock", "picture", "radio", "vase", "book", "computer"]
prices = [175, 90, 20, 50, 10, 200]
weights = [10, 9, 4, 2, 1, 20]

items = build_bag(names, prices, weights)
testGreedys(items, 20)






