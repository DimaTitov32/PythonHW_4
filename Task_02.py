# Задача 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

num = int (input ('введите натуральное число: '))
list_num = []
i = 2
while num !=1:
    if (num % i == 0):
        list_num.append(i)
        num = num / i
    else: 
        i += 1
print (list_num)

while i <= num:
    if (i % i == 0 ):
        print (i)
        i += 1


