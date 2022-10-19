#Задайте строку из набора чисел. Написать программу, 
#которя покажет > и < число. В качестве символа разделителя исп-ся пробел.
i = '1 2 3 4 5 6'
result = list(map(int, (i.split(' '))))
print(max(result), min(result))

nums = '2 54 6 78 89 56 5 3'
my_list = [int(num) for num in nums.split()]
print(min(my_list), max(my_list))