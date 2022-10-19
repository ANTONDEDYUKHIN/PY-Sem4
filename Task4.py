# Задана натуральная степень k. Сформировать случайным
# образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
#Пример:- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
max=100
k = int(input('Input k:'))
koef=[randint(0,max) for i in range(k)]+[randint(1,max)]
polynomial=' + '.join([f'{(j,"")[j==1]}x*{i}' for i, j in enumerate(koef) if j][::-1])
polynomial=polynomial.replace('x*1 +', 'x +')
polynomial=polynomial.replace('x*0', '')
polynomial+=('','1')[polynomial[-1]==' + ']
polynomial=(polynomial, polynomial[:-2])[polynomial[-2:]=='*1']
print(polynomial)
f = open('file.txt','w')
f.write(str(polynomial))
