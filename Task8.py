#Напишите программу, которая найдет 
# Наименьшее Общее Кратное 2х чисел
a, b = 6, 8
nok = max(a, b)
while not (nok % a ==0 and nok % b==0):
    nok += max(a, b)
print (nok)
