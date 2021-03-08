import math
import random


def standart_method():
    p = 0.1
    pk = p
    k = 1
    r = random.random()
    while (r > pk):
        k = k + 1
        pk = pk + p
    return k

def Geometric(p):
    k = 1
    Pg = p
    while(True):
        r = random.random()
        if (r <= Pg):
            break
        else:
            k = k + 1
            Pg = Pg + pow((1-p), k-1) * p
    return k

def Pascal(p, N):
    x = 0
    for i in range(N):
        x = x + Geometric(p)
    return x

def PascalNew(p, m):
    good = 0
    all = 0
    while (good < m):
        r = random.random()
        all = all + 1
        if (r <= p):
            good = good + 1
    return all
def PascalClassicRow(p, m):
    good = 0
    all = 0
    while (good < m):
        r = random.random()
        all = all + 1
        if (r <= p):
            good = good + 1
    return all

random.seed()
m = 5
p = 0.9
N = 10000
for i in range(m):
    standart_method()
print("---")
sum1 = 0 #сумма элементов
for i in range(N):
    result = Pascal(p, m)
    sum1 = sum1 + result
    print("распределение паскаля через геометрическое " + str(result))
sum2 = 0 #сумма элементов
for i in range(N):
    result = PascalNew(p, m)
    sum2 = sum2 + result
    print("новое распределение паскаля " + str(result))
Mx = m / p
print("Мат ожидание теоритическое " + str(Mx))
print("Мат ожидание фактическое для старого метода " + str(sum1/N))
print("Мат ожидание фактическое для нового метода " + str(sum2/N))
Dx = m * (1 - p) / (p * p)
print("Дисперсия " + str(Dx))



