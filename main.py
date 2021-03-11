import math
import random
random.seed()
list_elements1 = list()
list_elements2 = list()
list_elements3 = list()
map_objects1 = dict()
map_objects2 = dict()
map_objects3 = dict()
sum1 = 0 #сумма элементов
sum2 = 0 #сумма элементов
sum3 = 0 #сумма элементов
m = 10
p = 0.9
N = 100
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
def PascalClassicRow(p, m, w):
    q = 1 - p
    k = m - 1
    n = w - 1
    C = math.factorial(n) / (math.factorial(n-k) * math.factorial(k))
    result = C * pow(p,m) * pow(q, w - m)
    return result
def disper(list_elements, mat_ojidanie):
    result = 0
    for i in list_elements:
        result += pow(i - mat_ojidanie, 2)
    result =  result/(N - 1)
    return result

for i in range(N):
    result = Pascal(p, m)
    sum1 = sum1 + result
    try:
        map_objects1[result] = map_objects1[result] + 1
    except:
        map_objects1[result] = 1
    list_elements1.append(result)
    print("Распределение паскаля через геометрическое " + str(result))

for i in range(N):
    result = PascalNew(p, m)
    sum2 = sum2 + result
    try:
        map_objects2[result] = map_objects2[result] + 1
    except:
        map_objects2[result] = 1
    list_elements2.append(result)
    print("Новое распределение Паскаля " + str(result))

for i in range(N):
    w = m
    pg = PascalClassicRow(p, m, w)
    r = random.random()
    while( pg < r ):
        w = w + 1
        pg = PascalClassicRow(p,m,w) + pg
        r = random.random()
    sum3 = sum3 + w
    try:
        map_objects3[w] = map_objects3[w] + 1
    except:
        map_objects3[w] = 1
    list_elements3.append(w)
    print("Стандартный метод генерации:" + str(w))

Mx = m / p
print("Мат ожидание теоретическое " + str(Mx))
print("Мат ожидание фактическое для старого метода " + str(sum1/N))
print("Мат ожидание фактическое для нового метода " + str(sum2/N))
print("Мат ожидание фактическое для стандартного метода " + str(sum3/N))

Dx = m * (1 - p) / (p * p)
print("Дисперсия теоретическая " + str(Dx))
print("Дисперсия фактическая для старого метода " + str(disper(list_elements1, sum1/N)))
print("Дисперсия фактическая для нового метода " + str(disper(list_elements2, sum2/N)))
print("Дисперсия фактическая для стандартного метода " + str(disper(list_elements3, sum3/N)))

print("Ряд распределения для старого метода : ", map_objects1)
print("Ряд распределения для нового метода : ", map_objects2)
print("Ряд распределения для стандартного метода : ", map_objects3)
sum = 0
ideal1 = N / len(map_objects1)#*на вероятность появления этого числа
ideal2 = N / len(map_objects2)
ideal3 = N / len(map_objects3)
result1 = 0
result2 = 0
result3 = 0
for i in map_objects1:
    ideal1 = N * PascalClassicRow(p, m,i)
    result1 += math.pow(map_objects1[i] - ideal1, 2) / ideal1
print("Кол-во степеней свободы для старого метода : ", len(map_objects1))
print("Хи квадрат для старого метода : ", result1)
for i in map_objects2:
    ideal2 = N * PascalClassicRow(p, m, i)
    result2 += math.pow(map_objects2[i] - ideal2, 2) / ideal2
print("Кол-во степеней свободы для нового метода : ", len(map_objects2))
print("Хи квадрат для нового метода : ", result2)
for i in map_objects3:
    ideal3 = N * PascalClassicRow(p, m, i)
    result3 += math.pow(map_objects3[i] - ideal3, 2) / ideal3
print("Кол-во степеней свободы для стандартного метода : ", len(map_objects3))
print("Хи квадрат для стандартного метода : ", result3)






