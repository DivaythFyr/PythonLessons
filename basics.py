# Операторы в Python

# Базовые операторы
# +, -, *, /, //, %, **
# print(3 ** 4)

# // - деление без остатка
# print(2.5 // 2)

# % остаток от деления
# print(30 % 4)

# Только ** (возведение в степень) справа налево
# print(2**3**3)

# Переменная - Временная и именнуемая
# ячейка памяти
# Хранить под переменными можно практически все
# Список дел: подготовиться к соревнованием

# Для создания переменной пишем
#
# x = 2     #| int
#x = 2 * 3
#x = 3.0    #| float
#x = False    #| bool
#x = "Hello"  #| str

# Можно создавать переменные засчет других переменных
# Но они не будут взаимно меняться
# x = 2
# y = x
# print(x)
# print(y)
# x = 3
# print(y+2)

# Типы данных можно превращать друг
# в друга используя функции литералы
# int()
# float()
# str()
# bool()

#print(int(2.999))
#print(float(40))
#print(str(455)) #В строку можно превратить что угодно
#print(int('444'))
#print(int('aa44'))
#print(float('4'))


# Задание: создать две переменные,
# одна равняется True, другая False
# и превратить их в целые числа


# Задание: создать переменную,
# в которую записать строку
# '2' и превратить ее в число

# Задание: создать переменную,
# в которую записать строку 'fgfgf'
# и превратить ее в число
#print(int('fgfgf'))



# Задание: сделать две переменных,
# одна из них дробная (2.2)
# другая целое
# умножить эти две переменные
# и превратить в целое число их результат
x = 3
y = 2.2
#print(x*y)



# Python - язык динамического типизирования
# Значения переменных можно
# менять на любой другой тип данных
# y = 'fgfg'
# y = True


# Задание: создать две числовые переменные.
# Добавить ко второй переменной первую
# и записать в эту же переменную
f = 5
h = 6
h = h + f

f += h



# Задание: Создать две числовые переменные.
# Добавить ко второй переменной остаток деления
# первой переменной на два
# 3 % 2   выводит остаток деления первого на второе
# x = 4  y = 10   print(x) -> 4
# first_number = 4
# second_number = 7
# first_number += second_number % 2
# print(first_number)

# Задание: создать две числовые переменные,
# создать третью переменную, в которой выводится
# результат теоремы Пифагора
# двух начальных переменных
# гипотенуза равняется корню суммы квадратов
# катетов \\ Формула a^2 + b^2 = c^2
# **0.5 эквивалентно корню
a = 5
b = 7
c = (a**2+b**2)**0.5


# чтобы взаимодействовать с компьютером можно
# использовать функцию input()
# x = input()  #- в скобках пишем что компьютер
# скажет пользователю
# print(type(x))
# a = int(input('Введи первый катет '))
# b = int(input('Введи второй катет '))
# hypoth = a**2 + b**2
# print(hypoth**0.5)


# Задание: сделать два инпута,
# которые запрашивают числа.
# Вывести возведение в степень
# одного на другое


# Булевы операторы
# >    <    >=    <=
# == - оператор сравнения
# != проверка на неравенство

# print('a' != 'a')


# Отличия между двумя равно и одним
# Одно = для создания переменных
# Два == для сравнения двух элементов


# условные выражения
# if условие (булевый оператор)/ True/False:
#   что сделать если условие выполняется
# elif другое условие, если не выполняется первое:
#   что сделать
# else: пишем, если вообще ничего не выполняется
#  что сделать, если вообще ничего не выполняется
first_number = 150
second_number = 130
if first_number == second_number:
    print(True)
elif first_number > second_number:
    print('150 больше 140')
else:
    print('150 меньше 140')

#  x % 2 == 0  проверка на четность
# Задание: сделать один инпут
# Если число четное - вывести,
# print(' оно четное')
# Если нечетное, то вывести,
# что print('оно нечетное')


# # Проверка на тип данных type()
# x = 'dfdfd'
# print(type(x))


# if type(x) == int:
# Задание: создаете переменную. Проверить
# переменную на тип данных,
# если она - целое число, то складываем ее с 5


# Условное выражение можем писать
# внутри другого условного выражения
# if 30 * 4 > 100:
#     if 30 * 4 > 150:
#         print('Ура, хватит на 4 проезда!')
#     else:
#         print('Совсем чуть-чуть не хватило до 150!')
# else:
#     if 4 > 3:


# Задание: произвольная переменная.
# Если это число, то проверяем его на четность,
# если оно четное, то выводим 'Оно четное'
# если нет, то выводим 'нечетное'
# Если переменная - не число, то выводим - это не число,
# а {тип данных этого числа}
# print(f'Это не число' + type(x))
# print(f'Это не число, а {type(x)}')



# Чтобы проверить два условия, можно воспользоваться оператором and
# x = 'fgfgf'
# if type(x) == str and x.isdigit():
#     x += '2'


# Задание: сделать инпут, ввести число.
# Если число кратно 3, написать 'Fizz'
# Если кратно 5, то написать 'Buzz'
# Если и тому и другому, то FizzBuzz
# Если ни тому и ни другому, то NotFizzBuzz



