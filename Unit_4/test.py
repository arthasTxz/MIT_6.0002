import random

def test(ntrials, prob):
    return [1 if random.random() <= prob else 0 for x in range(ntrials) ]


resultado = test(1000, 0.2)

positive_result = resultado.count(1)
total_result = len(resultado)
print(positive_result)
print(total_result)
print(positive_result / total_result)

matriz_irregular = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9, 4]
]

for x in matriz_irregular:
    y = len(x)
    for j in range(y):
        print(x[j])

def prueba(populations, n):
    total_pop = 0
    total_pop_n = 0
    for i in populations:
        column = len(i)
        for j in range(column):
            if j == n:
                total_pop_n += 1
            total_pop += 1
    return total_pop_n / total_pop

print(prueba(matriz_irregular, 2))