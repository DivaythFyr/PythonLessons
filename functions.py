# Функция - это часть кода, которая работает,
# только если ее вызвать.
# В функцию, как правило, вводят аргументы
# Функция способна возвращать данные

def my_function():
    print('Функция была вызвана')
# my_function() # Вызывать функцию нужно всегда со скобочками




name = 'Petr'
def Name(name):
    print(f'Hello {name}')
# Name('Igor')
# Name('Egor')
# Name('Natasha')



# Аргументы - переменные,
# на месте которых данные будут переданы в
# функцию и использованы

def PrintAnimal(animal, plant):
    print(f'{animal} and {plant}')
# PrintAnimal('lion', 'oak')


# Выводить аргументы можно не только
# в том порядке,
# в котором они были заданы

def My_Dogs(dog1, dog2, dog3):
    print('Мои песики, начиная с самого '
          'любимого: ' + dog2 + ', '
          + dog3 + ', ' + dog1)
# My_Dogs('Шарик', 'Фунтик', 'Вася')


# Каждому аргументу можно задать значение
# по умолчанию
def my_planet(planet = "The Earth"):
  print("I am from " + planet)

# my_planet()
# my_planet('Mars')


# В качестве аргументов может быть
# любой тип данных

def Printfruit(food):
  for x in food:
    print(x)
# Printfruit(["apple", "banana", "cherry"])
# Printfruit('apple banana cherry')


# Задача: преобразуйте данный код в функцию
name = input()
print('His name is ' + name)

def function(name):
    print('His name is ' + name)
# function('Ilya')


# Задача: преобразуйте данный код в функцию
# number_list = [1, 2, 2, 5, 6, 4]
# for i in range(len(number_list)):
#     number_list[i] += 1
# print(number_list)

def functIon(number_list):
    for i in range(len(number_list)):
        number_list[i] += 1
    print(number_list)
#functIon([3, 3, 3, 3, 4])


# Задача: преобразуйте данный код в функцию
# i = 100
# while i != 1:
#     i -= 1



# Задача: напишите функцию,
# которая берет список чисел
# и перемножает все эти числа


# Задача: напишите функцию,
# которая принимает строку
# и делает ее наоборот
# [::-1] - делает наоборот

def Reverse_String(string=''):
    string = string[::-1]
    list_from_str = string.split()
    print(''.join(list_from_str))
#Reverse_String('FFAA')



# Задача: функция принимает число,
# принимает диапазон range
# она должна проверить,
# находится ли число в диапазоне
# num in Range -> True/False

def checkRange(n, range):
    print(n in range)
# checkRange(4, range(10))


# Задача: Функция принимает
# два числа
# и печатает только
# нечетные числа между ними




# Задaча: Функция принимает число и список.
# Выводится результат сравнения длины списка и числа

def simple_function(x):
    return x
# print(simple_function(4))


# Задача: Функция принимает список чисел
# и возвращает только четные числа

def EvenList(number_list):
    even_numbers = []
    for i in range(len(number_list)):
        if number_list[i] % 2 == 0:
            even_numbers.append(number_list[i])
    return even_numbers
# print(EvenList([1, 2, 3, 4, 5, 6, 7, 8,9,10]))



# Задание: Функция принимает любой список и пустой
# список
#  Циклом for скопировать все элементы в пустой
#  список (методом append).  список.append(элемент)


# Задание: Функция принимает: Список строк, целых и дробных чисел.
# Если элемент - целое, меняем его на строку.
# Если дробное, меняем его на целое
# Если строка может превратиться в целое, меняем на целое
# Если нет, то меняем строку на длину ее символов len()
# Проверяем могут ли строки перейти в числа,
# если могут, то переводим
# if '4'.isdigit() == True: проверка можно ли перевести строку
# в целое число int(элемент)











#Задача: Функция принимает строку и
# возвращает True, если строка является
# палиндромом.
# Чтобы сделать строку наоборот, напишите string[::-1]

def checkPalindrome(string):
    if string[::-1] == string:
        return True
    else:
        return False

#checkPalindrome('AATTAAGGAATTAA')

# Задача: функция принимает строку,
# обозначающую последовательность ДНК и
# Возвращает эквивалентную ей РНК
# AATTGG -> UUAACC
# Опционально: проверить, если в строке что-то лишнее
# (не буквы снизу)
# A -> U
# T -> A
# G -> C
# C -> G


# Задание: функция принимает диапазон (по дефолту от одного до 100),
# число, которое нужно найти (проверить, будет ли оно в диапазоне)
# цикл while запрашивает input числа.
# Если число отличается от заданного на 20 процентов
# то вывести - 'очень близко'
# так пока пользователь не отгадает

def findNumber(PC_number, Range=range(1, 101)):
    if PC_number not in Range:
        return "It's impossible to solve the task, the number is out of range"
    difference = int(len(Range) / 100 * 20)
    user_number = 0
    while user_number != PC_number:
        user_number = int(input('Type a number '))
        if user_number == PC_number:
            return 'That is the number!'
        elif abs(user_number - PC_number) <= difference:
            print('You are very close!')
        else:
            print('You are very far from the right choice')
#findNumber(4)





# *args позволяет послать в функцию
# бесконечное количество
# непозиционных аргументов
def PrintAnimals(*animals):
    print(*animals)
# PrintAnimals('Lion', 'Tiger', 'Puma', 'Otter', 'Sparrow')

def PrintAnimalsOneByOne(*animals):
    for animal in animals:
        print(animal)
# PrintAnimalsOneByOne('Lion', 'Tiger', 'Puma')


# Задание: функция принимает
# бесконечное множество чисел
# Выводится умножение первого на последнее

def mul(*args):
    print(args[0] * args[1])
#mul(2, 4, 5, 6)

# Задание: функция принимает бесконечное множество
# Имен и выводит : f"Hello, {name}!"
# f"fgfgf {variable}"

# Задание: функция принимает бесконечное множество имен
# Если оно начинается с большой буквы, то
# печатаем f' {name}, Ваше имя начинается с большой буквы, вы уважаете себя'
# Иначе: f' {name}, Кажется, вы не уважаете себя'
# Проверить первую букву на заглавную string[0].isupper()



# Взаимодействие функций
def multiplication(a):
    c = a**2
    return c

def subtraction(c):
    d = c - 2
    return d

# print(subtraction(multiplication(2)))

# Задание: первая функция примает диапазон
# и на его основе создает список чисел
# Вторая функция примает список и выводит сумму всех элементов.




# Задание: Одна функция создает список
# из бесконечного количества аргументов

# Другая функция меняет типы данных:
# Строки меняет в список строк из символов. string.split()
# Если видим число, то умножаем его на самую соседнюю строку слева
# theLastString = '' В эту переменную до цикла можем класть каждую
# новую попавшуюся строку
# Пример: ['aa', 2, 'bb', 2] -> [['a', 'a'], 'aaaa', ['b','b'], 'bbbb']

def CreateArgsList(*args):
    return [*args]

def ChangeData(List):
    theLastStr = ''
    for i, element in enumerate(List):
        if type(List[i]) == str:
            theLastStr = List[i]
            List[i] = List[i].split() # вернет список
        elif type(List[i]) == int:
            if type(theLastStr) == str:
                List[i] *= theLastStr
            elif type(theLastStr) == list:
                for j, symbol in enumerate(theLastStr):
                    theLastStr[j] *= List[i]
    return List
#print(ChangeData(CreateArgsList('hello', 4, 3, 'Hi', 'Thor')))





# Чтобы быстрее и лучше придумывать и писать решения любых задач:
# 1. Визуализировать у себя в голове все изначальные данные, которые будут приниматься функцией
# (какой тип данных/ какая структура данных, в каких переменных это хранится)
# 2. Осознать, что именно должна вернуть функция (помня, что функция выполнит только один return)
# 3. Представить, какие изменения должны произойти с изначальными данными,
#  чтобы из них получились конечные

# Советы:
# 1. Если нам нужно показать количество каких-то элементов,
# частоту чего угодно, сумму/умножение определенных элементов,
# то создаем переменную с нулевым значением, к которой будем прибавлять/умножать
# Пример: вычислить сумму всех четных чисел из списка
def SumEven(number_list):
    Sum = 0
    for i, number in enumerate(number_list):
        if number % 2 == 0:
            Sum += number
    return Sum


# Задание: создать функцию,
# которая принимает число,
# возвращает список из:
# квадрата этого числа,
# затем сконкатенированного на само себя, например, 2 -> 22, 11 -> 1111
# И это число умноженное на два
def NumListCreator(number):
    number_list = [number**2, int(str(number)*2), number*2]
    return number_list

# Функция принимает этот список (из предыдущей задачи) и строку
# Проверяем, длину самого большого элемента предыдущей
# функции и длину текста
# Если в тексте столько же или больше слов, чем у max (самого большого), то
# Находим символы по индексам  и выводим новую строку из них
# Новая Строка содержит 3 элемента
# [0, 1, 2], 'abcde' -> 'abc'
def SubString(string,number_list):
    if max(number_list) > len(string) - 1:
        return "Not able to execute"
    return '' + string[number_list[0]] + string[number_list[1]] + string[number_list[2]]
#print(SubString('ddfdfdfdfdfdfdfdfdfdfdffdfd', NumListCreator(2)))



# Функция принимает число, создает список,
# Внутрь созданного списка помещает количество списков,
# которое указано в аргументе
# 3 -> [[], [], []]
# List.append() - добавить элемент в список (список тоже можно добавить)
def List_of_lists(number_of_lists):
    List = []
    for i in range(number_of_lists):
        List.append([])
    return List
#print(List_of_lists(number_of_lists=4))


# Функция принимает строку и список из списков
# В каждый список добавляет эту строку
# List[i] = string, List[i].append(string)
def AddString(string, list_of_lists):
    for i, list in enumerate(list_of_lists):
        list.append(string)
    return list_of_lists
#print(AddString('Hello', List_of_lists(4)))


def factors(n):
    for k in range(1,n+1):
        if n % k == 0:
            yield k
# print(factors(10))



# Пример когда одна функция пользуется другой в качестве аргумента
def add(x, y):
    return x + y

def mean(x, y):
    return (x + y) / 2

# mean(add(4, 4), add(5, 5))


# Задание: первая функция вычитает один аргумент от другого
# Вторая функция возводит в квадрат число
# Во вторую функцию в качестве аргумента передать первую.
# def unsum(one,two):
#     return one-two
# def squart(one):
#     return one**2
# print(squart(unsum(30,28)))


# Первая функция принимает число. Создает список из пустых строк
# количество элементов равно числу, которое принимается в функцию
# Вторая функция принимает список и строку. Каждый элемент списка
# меняет на строку
# Вторая функция вызывает первую в качестве первого аргумента

def empty_list(str_num):
    L = []
    for i in range(str_num):
        L.append('')
    return L

def list_of_str(L, str):
   for i in range(len(L)):
       L[i] = str
   return L
# print(list_of_str(empty_list(8), 'Hello'))


# Задание: первая функция принимает список чисел,
# каждое второе число превращает в строку
# Другая функция принимает список, каждый третий элемент
# превращает в строку
# Первая функция вызывает вторую, Вторая функция вызывает первую.


# Задание: первая функция принимает строку и просто возвращает
# Вторая функция принимает строку и число. Каждый символ умножается на
# это число


# def func1(word):
#     return word
# def func2(word, number):
#     Word = ''
#     for i in range(len(word)):
#         Word += word[i] * number
#     return word
# print(func2(func1('Hello'), 2))




# "09:10:01" -> "09:10:01"
# "11:70:10" -> "12:10:10"
# "19:99:99" -> "20:40:39"
# "24:01:01" -> "00:01:01"


def ST(string):
    hour_minute_sec = string.split(':')
    hour, minute, second = hour_minute_sec

    if second[0] == '0':
        second = int(second[1])
    else:
        second = int(second)

    if minute[0] == '0':
        minute = int(minute[1])
    else:
        minute = int(minute)

    if hour[0] == '0':
        hour = int(hour[1])
    else:
        hour = int(hour)

    while second > 59:
        second -= 60
        minute += 1

    while minute > 59:
        minute -= 60
        hour += 1

    while hour > 23:

        hour -= 24

    result = ''
    if hour < 10:
        result += f'0{hour}:'
    else:
        result += f'{hour}:'

    if minute < 10:
        result += f'0{minute}:'
    else:
        result += f'{minute}:'

    if second < 10:
        result += f'0{second}'
    else:
        result += f'{second}'

    return result


# print(ST("19:99:99"))




















