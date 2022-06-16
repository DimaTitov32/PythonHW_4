# Задача 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint
list = []
new = []
for i in range (10):                                
    list.append(randint(0,20))                     
   
print ('исходная последовательность:')
print (list)
list.sort()
for i in range(len(list)-1):
    if (list[i] != list[i+1]):
        new.append(list[i])
print (new)

