import math
import random
items = ["jarro", "rama", "pan"]


def algo(items):
    numero = len(items)
    print(numero)

    for i in range(2**numero):
        combo = []
        for j in range(numero):
            algo = i >> j
            print(math.floor(algo))
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


def lista(si):
    numero = len(si)
    general = []
    for i in range(2**numero):
        combo = []
        for j in range(numero):
            # algo = i / (2**j)
            # print(math.floor(algo))
            if (i >> j) % 2 == 1:
                combo.append(str(items[j]))
        general.append(combo)
        # print("Este es: ", i)
        if i % 2 == 1 :
            yield (general[0], general[1])
            general= []


def combo(items):
    N = len(items)
    # Enumerate the 3**N possible combinations   
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            if (i // (3 ** j)) % 3 == 1:
                bag1.append(str(items[j]))
            elif (i // (3 ** j)) % 3 == 2:
                bag2.append(str(items[j]))
        yield (bag1, bag2)
      

class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        return '<' + self.name + ', ' + str(self.value) + ', '\
                     + str(self.weight) + '>'
    
def buildItems():
    return [Item(n,v,w) for n,v,w in (('clock', 175, 10),
                                      ('painting', 90, 9),
                                      ('radio', 20, 4),
                                      ('vase', 50, 2),
                                      ('book', 10, 1),
                                      ('computer', 200, 20))]


def buildRandomItems(n):
    return [Item(str(i),10*random.randint(1,10),random.randint(1,10))
            for i in range(n)]


items = buildItems()
algo = combo(items)
for x in algo:
    print(x)

