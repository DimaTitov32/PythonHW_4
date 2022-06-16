# Задача 4. Задана натуральная степень n. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени пример записи в файл при n=3 ==> 33x^3 + 8x^2 + 64x + 85 = 0 при n=2 ==> 27x^2 + 95x + 79 = 0.')

from random import randint as rnd

num = int (input ('введите степень: '))
def polynomial (n):
    equation = ''
    for i in range(n, 1, -1):
        k = rnd(0,100)
        if k != 0:
            equation += str(k) + 'x^' + str(i) + ' + '
        else:
            equation += ''
    equation += str(rnd(0,100)) + 'x' + ' + ' + str(rnd(0,100)) + ' = ' + '0'
    return equation
print (polynomial (num))

with open ('file1.txt', 'w') as data:
    data.write( polynomial (num))