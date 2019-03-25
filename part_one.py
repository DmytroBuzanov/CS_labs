f = open("D:/Lab1_CS/src/Lina.txt")
d = {}
k = 0
for line in f:
    for b in line.lower():
        if b in d:
            d[b] += 1
        else:
            d[b] = 1
        k += 1
print('Відносна частота появи символу:')
for i in d:
    print('{0} -> {1}'.format(i, d[i] / k))

print('Ентропія:')
from math import log2 as log

H = 0
for i in d:
    H += d[i] / k * log(k / d[i])

print('H -> {0}'.format(H))

print('Кількість інформації в тексті:')
print('H * k _> {0}'.format(H * k))



