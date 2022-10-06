# Задайте натуральное число N. 
# Напишите программу, которая 
# составит список простых множителей числа N.
import math 
num = int(input('Input integer:'))

while num % 2 == 0: 
        print(2,) 
        num = num / 2 
 
for i in range(3, int(math.sqrt(num)) + 1, 2): 

        while num % i == 0: 
            print(i,) 
            num = num / i 
if num > 2: 
        print(num) 


