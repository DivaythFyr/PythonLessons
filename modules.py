import math # Чтобы импортировать модули, пишете import,
# затем название модуля, который хотите импортировать.
# через запятую можно указывать несколько модулей,
# например, import math, sys


# Повторяющиеся названия переменных и методов
# не будут конфликтовать между собой, потому что
# для их использования нужно всегда указывать
# название модуля
import numpy.ma

pi = 3.14
import math
# print(math.pi) # Это две разные переменные
# print(pi)

# Если мы хотим импортировать не весь модуль,
# а только какую-либо его часть (например, метод),
# то нужно пользоваться
# конструкцией from названиеМодуля
# import Переменная/метод

#from math import e, pi

#print(math.pi)
#print(math.e)

# Если хочется назвать имя модуля как-то по-другому
# (например, короче), можно воспользоваться
# Ключевым словом as
# import numpy as np
# np.arange()

# from math import sqrt
# Задача: написать функцию,
# которая принимает число,
# берет из него квадратный корень


# math.pi * R**2
# Задача: написать функцию,
# которая возвращает площадь круга, принимает радиус

# Задача: написать функцию,
# которая принимает число и возвращает синус и косинус

# Задание: функция принимает список (int, str)
# сделать запись в файл: если число, то вывести косинус
# with open(r'') as f:
#  f.write(переменная)
# если строка превращается в число - то синус
# если не превращается, то прибавить к строке число пи

def ListFunction(list):
    str_1 = '' # Пустая строчка, которая затем и будет возвращена
    for i in range(len(list)):
        if type(list[i]) == int:
            str_1 += str(math.sin(int(list[i])))
        elif type(list[i]) == str and list[i].isnumeric() == True:
            str_1 += str(math.sin(int(list[i])))
        elif type(list[i]) == str:
            str_1 += str(list[i])
            str_1 += str(math.pi)

    with open(r'\\resproject.ru\share\FARM_USER_HOME\a.khakimova\Desktop\Учёба Амины\newfile.txt', 'wt') as f:
        f.write(str_1)

from fuzzywuzzy import fuzz

#print(fuzz.ratio("g", "green"))
#print(fuzz.partial_ratio("let’s compare strings", "strings"))
#print(fuzz.partial_ratio("let’s compare strings", "stings"))

# Задание: функция принимает две строки
# сравнивает fuzz.ratio и fuzz.partial_ratio
def CompareStrings(str1, str2):
    return max(fuzz.ratio(str1, str2),fuzz.partial_ratio(str1, str2))
#print(CompareStrings('Hello', 'Hel'))


# Задание:
#  импортировать википедию
# Попробовать что-нибудь поискать
import wikipedia
result = wikipedia.page("X")
#print(result.summary)


# С помощью этого модуля можно посмотреть работу
# написанной вашей функции под капотом
import dis

def test(number):
    return (str(number) + str(number))

def newFunc(string):
    print("Hello", string)

#dis.dis(test)

#dis.dis(newFunc)


# NumPy
# Позволяет проводить сложные математические расчеты
# На базовом уровне с помощью NumPy создают и манипулируют
# массивами значений одного типа
import numpy as np
a = np.arange(15).reshape(1, 15)
#print(a)
#print(a.shape)
#print(a.ndim)
#print(a.dtype.name)
b = np.array([2, 3, 4])
#print(b)


import matplotlib.pyplot as plt
x = np.arange(0,100)
y = x*2
z = x**2

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 2))

axes[0].plot(x, y, color="green", lw=3)
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')

axes[1].plot(x, z, color="blue", lw=2, ls='--')
axes[1].set_xlabel('x')
axes[1].set_ylabel('z')
#plt.show()



# clean-text позволяет быстро очищать текст от мусорных символов
# и приводить его в достойный вид
from cleantext import clean
# Sample text
text = """ Zürich, largest city of Switzerland and capital of the canton of 633Zürich. Located in an Al\u017eupine. (https://google.com). Currency is not ₹"""
# Cleaning the "text" with clean text
clean(text)
#print(text)


# Pillow
from PIL import Image
im = Image.open(r"C:\Users\aisin\Pictures\Saved Pictures\Wrist and forearm.tif")
#print(im.format, im.size, im.mode)
#im.show()


# arrow - пакет для работы с датами и временем
import arrow
arrow.get('2020-05-11T21:23:58.970460+07:00')

utc = arrow.utcnow()
#print(utc)

#print(utc.to('msk'))


