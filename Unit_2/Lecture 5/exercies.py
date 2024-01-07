import random

def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    number = random.randint(0, 100)
    while number % 2 != 0:
        number = random.randint(0, 100)
    return number
     

# for x in range(1000):
#     print(genEven())

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    # Your code here
    numbers = [x for x in range(9, 22) if x % 2 == 0]
    return random.choice(numbers)

# deterministicNumber()

def dist3():
    return int(random.random() * 10)

def dist4():
    return random.randrange(0, 10)


for x in range(1000):
    print(dist4())