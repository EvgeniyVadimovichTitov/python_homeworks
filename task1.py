# Вычислить число c заданной точностью d

# Пример:

# - при d = 0.001, π = 3.141
# Ввод: 0.01
# Вывод: 3.14

# Ввод: 0.001
# Вывод: 3.141

import math

k_round = len(input('введите кол-во знаков после запятой в формате 0,01: '))-2

print(round(math.pi, k_round))
