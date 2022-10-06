# Вычислить число c заданной точностью d. Пример:
# при d = 0.001,π = 3.141             10^(-1)≤d≤10^(-10)

from math import pi

d =  int(input("Input integer:\n"))
print(f'a number with a given precision {d} = {round(pi, d)}')