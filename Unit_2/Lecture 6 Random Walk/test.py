import random
import pylab
random.seed(0)

# for x in range(random.randint(1, 10)):
#     print(x)

# for x in range(random.randint(1, 10)):
#     print(x)

# for x in range(random.randint(1, 10)):
#     print(x)

# for x in range(random.randint(1, 10)):
#     print(x)

class Test(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = {(x, y): False for x in range(self.width) for y in range(self.height) }

    def showTiles(self):
        print(self.tiles)

    def changeTile(self, pos):
        self.tiles[pos] = True

    def isTileCleaned(self, m, n):
        return self.tiles[(m, n)]

    def getRandomPosition(self):
        return random.choice(list(self.tiles.keys()))


# t = Test(5, 5)
# t.changeTile((2,2))
# print(t.isTileCleaned(2, 2))
# print(t.isTileCleaned(4, 4))
# print("random choice:" , t.getRandomPosition())
# t.showTiles()
lista1 = [random.randint(1, 100) for x in range(50)]
lista2 = [ x * random.randint(1, 3) for x in lista1]
print(lista1)
pylab.plot(lista1, lista2)
pylab.show()
