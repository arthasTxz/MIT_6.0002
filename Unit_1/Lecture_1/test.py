items = ["A", "B", "C"]

def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


for i in powerSet(items):
   
    print(i)


def yieldAllCombos(items):
    
    num = len(items)
    for i in range(2*(2**num) + 1 ):
        combo1 = []
        combo2 = []
        for j in range(num):
            # print((i >> j) % 3)
            if (i >> j) % 3 == 1:
                combo1.append(items[j])
            elif (i >> j) % 3 == 2:
                combo2.append(items[j])

        yield (combo1, combo2)


print("============================")
for x in yieldAllCombos(items):
    print(x)

for x in range(3):
    print(x)


def nose(items):
    numero = len(items)
    combo = []
    for i in range(2**numero):
        for j in range(numero):
            if (i >> j) % 2 == 1:
                combo.append(str(items[j]))
        if i % 2 == 1 and len(combo) > 1:
            yield tuple(combo)
            combo= []

for x in nose(items):
    print(x)