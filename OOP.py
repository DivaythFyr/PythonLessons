# Классы - сущности, свойства которых зависят от наследования
# или преемственности от других классов

# Для начала разберем на примере того, как реализуется стек.
# Стек - это объект с двумя методами: push и pop.
# Элементы попадают туда как монеты в стопку - каждый по очереди. Если
# Если в стопку попала последняя монета
# и нам нужно вытащить монету,
# то последние монеты будут первыми изыматься

stack = []

def push(val):
    stack.append(val)

def pop():
    val = stack[-1]
    del stack[-1]
    return val

# Объектно-ориентированный подход
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        val = self.stack[-1]
        del self.stack[-1]
        return val

stackObject = Stack() # Чтобы создать объект
# с определенным классом - пользуемся такой конструкцией.
#print(stackObject.stack)
#stackObject.push(3)
#print(stackObject.pop())

# Функцию - мы пишем сами, метод - это функция,
# которая прописана в классе
# объект.метод()
# Примеры встроенные в Python: int()/str()/bool() функция, L.append() метод

# Каждый класс должен начинаться с функции __init__,
# у нее обязательно должен быть параметр self.
# Благодаря self внутри init задаются свойства и методы,
# которыми смогут пользоваться другие функции класса,
# а также классы, унаследованные от него


class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self.customer = customer
        self.bank = bank
        self.account = acnt
        self.limit = limit
        self.balance = 0

    def raiseBalance(self):
        return self.balance + 100

V017 = CreditCard('Alex', 'Sber', '01657', 0)
# print(V017.raiseBalance())



# Задание: создать класс Number,
# который в init принимает два числа,
# метод, который выдает сумму этих чисел
# метод, который умножает эти числа

class Number:
  def __init__(self, number1, number2):
    self.number1 = number1
    self.number2 = number2

  def Sum(self):
    return self.number1 + self.number2

  def Mult(self):
    return self.number1 * self.number2

FF = Number(17, 50)
# print(FF.Sum())
# print(FF.Mult())

# Задание: класс Person, принимает имя,
# фамилия, дату рождения и страну
# Создать метод, который выводит строчку,
# где перечисляются все эти параметры





# Задание: класс Employee, который принимает имя, фамилию, зарплату и номер телефона
# Метод для вывода информации об Employee
# Метод, который увеличивает зарплату на 100.
# Добавить try и except, где возможно



class Employee():
    def __init__(self, name, last_name, salary, number):
        self.name = name
        self.last_name = last_name
        self.salary = salary
        self.number = number

    def SumSalary(self):
        try:
            #assert type(self.salary) == int
            self.salary += 100
            print(f'{self.name} {self.last_name}, зарплата: {self.salary}, номер телефона: {self.number}')
        except TypeError:
            print('Зарплата не является числом')

# Joe = Employee('Joe', 'X', 200, '89130000000')
# Joe.SumSalary()


# Чтобы унаследовать от класса, нужно при объявлении потомка
# в круглых скобках указать имя родителя
# В функции init, перед еще одним init написать имя класса родителя
# Если мы пользуемся похожими методами от класса родителя
# - то пишем имя родителя, точку,
# метод родителя, задаем аргументы

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

    def getSum(self):
        return self.__sum

stack1Object = AddingStack()

# for i in range(5):
#     stack1Object.push(i)
# print(stack1Object.getSum())
#
# for i in range(5):
#     print(stack1Object.pop())

# Задание: класс Math, принимает два числа.
# Есть метод вычитания и метод деления.
# Сделать try except для метода деления


# Задание: класс принимает список.
# метод выводит тип каждого элемента
# метод добавляет в список значение
# метод находит все строки и выводит самую большую
# метод находит все числа и выводит самое большое

class LL:
    def __init__(self, L):
        self.L = L

    def print_type(self):
        for i, element in enumerate(self.L):
            print(f'{element} has type {type(element)}')

    def add_to_list(self, element):
        self.L.append(element)
        return self.L

    def maxStr(self):
        max = ''
        for element in self.L:
            if type(element) == str and len(element) > max:
                max = element
        return max







# Создать класс Time:
# час (0–23), минуты (0–59), секунды (0–59).
# Проверить if что время посылается правильное
# Два метода печати по шаблонам: «16 часов 18 минут 3
# секунды» и «4 p.m. 18 минут 3 секунды».

# class Time:
#     def __init__(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#         try:
#             self.hours in range(0, 24) and self.minutes in range(0, 60) and self.seconds in range(0, 60)
#         except:
#             print('Неверные значения')
#     def Template_1(self):
#         return f'{self.hours} часов {self.minutes} минут {self.seconds} секунд'
#     def Template_2(self):
#         return f'{self.hours} p.m. {self.minutes} минут {self.seconds} секунд'
# Values = Time(18, 39, 8)
# print(Values.Template_1())
# print(Values.Template_2())


# Задание: сделать класс Worker, он принимает личные данные:
# имя, фамилия, email, зарплату
# Сделать два класса конкретных профессий. Они должны наследоваться от Worker
# У них должны быть свои уникальные начальные данные
# Создать объект от класса-профессии и вывести его имя, фамилию, почту, зп
# Worker(name, surname, email, salary). Smith() -> выводит имя, фамилию, почту

class Worker:
    def __init__(self, name, surname, email, salary):
        self.name = name
        self.surname = surname
        self.email = email
        self.salary = salary

    def PData(self):
        return f'{self.name} {self.surname} {self.email} {self.salary}'

class Policeman(Worker):
    def __init__(self, name, surname, email, salary, weapon = True):
        Worker.__init__(self, name, surname, email, salary)
        self.weapon = weapon

    def isWeapon(self):
        return f' Есть ли оружие? Ответ: {self.weapon}'

Policeman1 = Policeman(name ='Bob', surname= 'Dylan',
                       email = 'asdasd@gmail.com', salary = 1200, weapon = True)
# print(Policeman1.PData())
# print(Policeman1.isWeapon())














# Задание: класс Note, принимает в себя любую текстовую информацию
# (три строки),
# Создает в init список строк

# Класс ToDoList наследует от Note. К каждой строке в этом
# списке метод добавляет порядковый номер.
# Например: ['Wash the car', 'Call back'] -> ['1. Wash the car',
# '2. Call back']



class Note:
    def __init__(self, str_1, str_2, str_3):
        self.list = [str_1, str_2, str_3]

class ToDoList(Note):
    def __init__(self, str_1, str_2, str_3):
        Note.__init__(self, str_1, str_2, str_3)

    def add_number(self):
        for i, element in enumerate(self.list):
            self.list[i] = f'{i+1}. {element}'
        return self.list

fgf = ToDoList('11', '22', '33')
# print(fgf.add_number())





# help() Показывает базовую информацию о классе
# print(help(AddingStack))


class Bookmaker:
    raise_amt = 1.06

    def __init__(self, Sum):
        self.Sum = Sum

    def lottery(self):
        return self.Sum * self.raise_amt

class OneXBet(Bookmaker):
    raise_amt = 1.02

# print(OneXBet.raise_amt)
# print(Bookmaker.raise_amt)


# У каждого объекта, унаследованного от класса,
# может быть свой собственный набор дополнительных свойств
# Либо какое-либо из свойств может не применяться

class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def setSecond(self, val):
        self.second = val

exampleObject = ExampleClass(4)
exampleObject.x = 4 # Задали свойство, которого не было у класса

# print(exampleObject.__dict__)


class ListOfNumbers:
    def __init__(self):
        self.list = []

    def push(self, val):
        self.list.append(val)


#OneZero = ListOfNumbers()
#OneZero.push(6)
#print(OneZero.list)


# Есть базовые методы для всех классов.
# Они называются 'магическими' или dunder
# Подчеркиваются двумя underscore __
# Например: __init__


# Функция init дает указанные нами свойства и методы
# объекту при его инициализации. Если создать переменную вне
# конструктора init, то он будет характерен для всего класса
# и абсолютно всегда будет наследоваться объектам.
class Example_Class:
    a = 1 # Переменная класса характерна и для класса и для объекта
    def __init__(self, val):
        self.b = val

ExampleObject = Example_Class(2)
# print(hasattr(ExampleObject, 'b'))
# print(hasattr(ExampleObject, 'a'))
# print(hasattr(Example_Class, 'b'))
# print(hasattr(Example_Class, 'a'))


# Если попытаться распечатать объект, то мы получим следующее
class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy
sun = Star("The Sun", "Milky Way")
# print(sun)


# Чтобы выводить информацию об объекте,
# нужно пользоваться конструктором __str__
# В конструкторе __str__ мы пишем return и указываем,
# что возвращаем.
# При использовании print на объект, с этого момента,
# Будет показываться
class Planet:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return self.name + ' is in ' + self.galaxy

Mars = Planet('Mars', 'Milky Way')
# print(Mars)




# Задание: класс Document,
# инициализирует размер текста и назначение
# при печатании выводит эти параметры

# __dict__ Выводит информацию о параметрах объекта
# print(Mars.__dict__)

# Методы сравнений __eq__, __ne__, __lt__, __gt__ и
# другие
# __eq__() – для равенства ==
# __ne__() – для неравенства !=
# __lt__() – для оператора меньше <
# __le__() – для оператора меньше или равно <=
# __gt__() – для оператора больше >
# __ge__() – для оператора больше или равно >=


# Например ge позволит напрямую
# сравнивать объекты между собой по определенному принципу
# в функции мы прописываем, что именно мы хотим проверить
# на нестрогое больше
class distance:
    def __init__(self, x=None, y=None):
        self.ft = x
        self.inch = y

    def __ge__(self, anotherObj):
        val1 = self.ft * 12 + self.inch
        val2 = anotherObj.ft * 12 + anotherObj.inch
        if val1 >= val2:
            return True
        else:
            return False
D1 = distance(2, 3)
D2 = distance(2, 5)
# print(D1 >= D2)


# Задание: расписать метод eq для этого же класса


# Задание: класс принимает год, месяц, день
# Если у двух объектов одинаковый год,
# то возвращается True (__eq__)


# Задание: класс Human принимает имя, возраст, адрес.
# метод set_info позволяет изменить значения этих параметров инпутами
# Создать объект, изменить его значение, распечатать


# Задание: класс Staff наследует от Human,
# получает новые параметры: подразделение и должность
# Выводите метод set_info для Staff

class Human:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def set_info(self):
        self.age = int(input('Введите возраст: '))
        self.name = input('Введите имя: ')
        self.address = input('Введите адрес: ')
    def __str__(self):
        return f'Человека зовут {self.name} его возраст - {self.age}, его адрес - {self.address}'
Ivan = Human('Ivan', 23, 'Lenina')
# Ivan.set_info()
# print(Ivan)

class Staff(Human):
    def __init__(self, name, age, address, job='Fireman'):
        Human.__init__(self, name, age, address)
        self.job = job
Job = Staff(name='Dima',age=21,address='Cherepovets',job='Fireman')
# Job.set_info()


# Задание: класс Mark принимает оценку
# dunder метод сравниваем эти числа (__eq__)






# pip install numpy
# import numpy as np
# Задание: класс Matrix принимает два числа,
# создает в init матрицу из нулей (np.zeros(2, 2))
# метод создает матрицу из рандомных чисел np.random.randint(число, size=число)
# метод позволяет изменить параметры матрицы -> Сделать заново нулевую
# (принимает как и init два числа и создает матрицу из нулей)
import numpy as np
class Matrix:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.x = np.zeros((self.num1, self.num2), dtype=int)

    def Ran(self):
        return np.random.randint(self.num1, size=self.num2)

    def reinitZ(self):
        self.x = np.zeros(self.num1, self.num2)
ObjectMatrix = Matrix(2, 4)
# print(ObjectMatrix.Ran())



# Статические методы не имеют доступа
# ни к атрибутам его экземпляров, ни к атрибутам класса
# Абсолютно изолированные и независимые функции
# Они могут обращаться к атрибутам класса,
# но не к свойствам экземпляров
# @staticmethod
import datetime
class Calendar:

    @staticmethod
    def is_weekend(weekday_date):
        if weekday_date > 5:
            print('Выходной')
c = Calendar()
# c.is_weekend(6)




# Задание: сделать класс To_Do_List,
# у него есть параметры количество дел

# Есть метод, благодаря которому можно
# сделать список из дел (кол-во дел как в init)
# (цикл for и input)

# Сделать статический метод, который принимает аргумент date
# Если date равен 31 декабря, то выводим:
# 'No todos, today is the New Year!'


# Задание: класс History_Event принимает аргументы event и date
# статический метод изменяет все / в дате на \
# ''.replace('/', '-')


# Задание: класс содержит статический метод,
# другой класс является дочерним
# Посмотреть, как наследуются
# статические методы (вызвать стат метод в дочернем классе)


class ToDoList:
    x = 7
    def __init__(self, item):
        self.item = item

    def todo_function(self):
        list = []

        for i in range(self.item):
            list.append(input('Write todo:'))
        return list

    @staticmethod
    def is_newyearday(data):
        if data == '31.12':
            return 'No todos, today is the New Year'


Note1 = ToDoList(5)
# print(Note1.todo_function())


# Задание: любой класс с любыми начальными параметрами.
# свободную переменную вне init.
# Статический метод выводит эту переменную






class RTyrttr:
    f = 0
    def __init__(self):
        RTyrttr.f = 9


class G:
    c = 0
    def __init__(self):
        self.x = 1
        G.c += 1

    @staticmethod
    def Count():
        return G.c

# X = G()
# N = G()
# M = G()
# print(G.Count())


# Класс имеет статические методы для: перевода
# кельвинов в цельсии, цельсии в кельвины
# Класс имеет статические методы для перевода
# килограммов в граммы и наоборот.






# Декораторы
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return f'{self.first} {self.last}'

emp1 = Employee('Jake', 'Stone')
emp1.first = 'John'
# Если мы меняем имя, то email не меняется
# print(emp1.first)
# print(emp1.email)
# print(emp1.fullname())

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    # Мы можем сделать отдельный метод для изменения значения email
    # Однако его придется вызывать всегда, как только меняю first, это крайне неудобно
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
emp1 = Employee('Jake', 'Stone')
emp1.first = 'John'
# print(emp1.first)
# print(emp1.email())
# print(emp1.fullname())


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # Благодаря этому декоратору email будет менять свое значение,
    # как только меняется first или last
    # Теперь без нашего участия
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp1 = Employee('Jake', 'Stone')
emp1.first = 'John'

# print(emp1.first)
# print(emp1.email)
# print(emp1.fullname)

# Однако напрямую все еще не могу изменить значения моих property

# emp1.fullname = 'George Washington'
# print(emp1.fullname)


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # Благодаря setter мы можем изменять значения наших property вручную
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

# Теперь все заработает
emp1 = Employee('Jake', 'Stone')
emp1.first = 'John'
emp1.fullname = 'George Washington'
# print(emp1.first)
# print(emp1.email)
# print(emp1.fullname)

# Задание: класс обозначает Книгу
# Принимает название, автора.
# Сделать property, который выводит полное название книги
# Например: "Hyperfocus by Chris Bailey"
# сделать ему setter

# print('fgfgfgf dfgfgf'.split())





# Задание: класс Army принимает численность войск (int),
# основной тип вооружения (str),
# второстепенный тип вооружения (str),
# очки атаки (float) и очки защиты (float).
# Метод: Исходя из численности, очков атаки и
# защиты выводится эффективность
# = все перемножается и делится на 3
# Добавить __str__ для вывода типа вооружения и основного типа
# Добавить декоратор: property для этого метода.





class student:
    def __init__(self, name, birth_year, age):
        self.name = name
        self.birth_year = birth_year
        self.age = age

    @property
    def email(self):
        if self.name == None:
            return "Member not found"
        return str(self.name) + "." + str(self.birth_year) + "@gmail.com"

    @email.setter
    def email(self, clg_email):
        name, birth_year = clg_email.split("@")[0].split(".")
        self.name = name
        self.birth_year = birth_year

    @email.deleter
    def email(self):
        self.name = None
        self.birth_year = None
        self.age = None

Max = student("max", 2001, 20)
# print(Max.email)
# del Max.email
# print(Max.email)
# print(Max.name)





import functools
import time
# Декораторы в общем виде пишутся таким образом
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
# function(*args, **kwargs) -> function(1, 2, 3,
# iris = 6.5, yarrow = 4.3, sunflower = 7.8)
        # Сделать что-то до
        value = func(*args, **kwargs)
        # Сделать что-то после
        return value
    return wrapper_decorator

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter() # засекаем начало
        value = func(*args, **kwargs)
        end_time = time.perf_counter() # засекаем конец работы
        run_time = end_time - start_time
        print(f'Finished in {run_time} secs')
        return value
    return wrapper_timer

@timer
def F():
    print('Hello')
# F()

# Задание 1
# Создайте функцию, возвращающую список со всеми
# простыми числами от 0 до 1000.
# Используя механизм декораторов посчитайте сколько
# секунд, потребовалось для вычисления всех простых чисел.
# Отобразите на экран количество секунд и простые числа.

# @timer
# def prime(num1, num2):
#     L = []
#     for i in range(num1, num2+1):
#         for j in range(2, i):
#             if i == 2 or i == 3:
#                 L.append(i)
#             elif i % j == 0:
#                 break
#             else:
#                 L.append(i)
#     return L
# print(prime(1, 10))



# @timer
# def points(num1, num2):
#     for i in range(num1, num2 + 1):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             print(i)
# points(1, 10)






# Задание 2
# Добавьте к первому заданию возможность передавать
# границы диапазона для поиска всех простых чисел.


#
# import functools
# import time
#
#
# def timer(func):
#     @functools.wraps(func)
#     def wrapper_timer(*args):
#         start_time = time.perf_counter()
#         value = func(*args)
#         end_time = time.perf_counter()
#         run_time = end_time - start_time
#         print(f"Функция выполнена за {run_time:.4f} с")
#         return value
#
#     return wrapper_timer
#
# @timer
# def primeNumber(num_1, num_2):
#     for number in range(num_1, num_2 + 1):
#         for i in range(2, number):
#             if (number % i) == 0:
#                 break
#         else:
#             print(number)

# primeNumber(2, 24)




# classmethods
# Классовые методы относятся к самому классу, а не к его экземплярам.
# Отличия от статических методов:
# 1. Статические методы вообще не знают ничего о классе
# 2. Классовые методы работают с самим классом



# Представим ситуацию, что у нас есть строка и мы хотим сделать
# из нее параметры для создания объекта
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

emp_str_1 = 'Harn-Thorne'
emp_str_2 = 'Nate-Diaz'
first, last = emp_str_1.split('-')
new_emp_1 = Employee(first, last)  # cls(first, last)

# Таким образом можно сделать процесс более автоматизированным
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @classmethod
    def from_string(cls, emp_str):
        first, last = emp_str.split('-')
        return cls(first, last)

new_emp = Employee.from_string('Nate-Diaz')



# Таким образом методы класса позволяют нам создавать экземпляры альтернативным путем

# Задание: класс Time принимает в init день
# (str), месяц (str), год (str)
# Классовый метод позволяет создавать объект
# из строки 'год-месяц-день'


class Time:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, time_str):
        day, month, year = time_str.split('-')
        return cls(day, month, year)
t1 = Time.from_string('12-05-2023')
# print(t1.year)

#     @classmethod
#     def from_list(cls, time_lst):
#         try:
#             assert len(time_lst) == 3 and int(time_lst[0]) in range(0, 30) and int(time_lst[1]) in range(0, 12)
#         except TypeError:
#             print('Введена некорректная дата')
#         else:
#             return cls(str(time_lst[0]), str(time_lst[1], str(time_lst[2])))



# Задание: классовый метод позволяет
# создавать объект Time из списка чисел
# TryExcept проверяют: в списке должно быть
# ровно три числа int.
# Первое не должно быть больше 30,
# второе больше 12, третье может быть любым






# Задание: класс LetterFilter строку
# разрешенных букв (str)
# Метод принимает текст и фильтрует его, убирая буквы,
# которых нет в разрешенных
# Классовый метод позволяет сделать объект
# из списка разрешенных букв, а не строки

class LetterFilter:
    def __init__(self, filter_str):
        self.filter_str = filter_str

    def text_filter(self, txt):
        filtered_str = ''
        for symbol in txt:
            if symbol in self.filter_str:
                filtered_str += symbol
        return filtered_str

    @classmethod
    def from_list(cls, L):
        filter_str = ''.join(L)
        return cls(filter_str)



# Задание: функция принимает список параметров LetterFilter
# try except проверяет, как лучше создать объект:
# через init или классовым методом
# Если аргументы совсем не подходят, то выводим ошибку TypeError

def LetterFilterCreator(value):
    if isinstance(value, str):
        obj = LetterFilter(value)
    elif isinstance(value, list):
        obj = LetterFilter.from_list(value)
    else:
        print("TypeError")
    return obj
A = LetterFilterCreator(['a', 'c'])
# print(A.filter_str)







# Классовые методы позволяют манипулировать переменными класса
class Artist:
    favorite_color = 'black'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_fav_color(cls, color):
        Artist.favorite_color = color


# Если унаследованному классу не указать __init__,
# то он будет наследовать __init__ родителя автоматически
class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h

class DeskTable(Table):
    def square(self):
        return self.width * self.length

t1 = Table(1.5, 1.8, 0.75)
t2 = DeskTable(0.8, 0.6, 0.7)
# print(t2.square())

# Если написать у потомка метод, который звучит также,
# как у родителя,
# то при его вызове будет вызываться именно метод потомка
class ComputerTable(DeskTable):
    def square(self, monitor=0.0):
        return self.width * self.length - monitor

t3 = ComputerTable(0.8, 0.6, 0.3)
# print(t3.square(0.3))


# Чтобы проверить, является ли один из классов
# унаследованным от другого,
# можно воспользоваться методом issubclass()

class Two():
    pass

class TwentyTwo(Two):
    pass

class TwoHundredTwentyTwo(TwentyTwo):
    pass
# print(issubclass(Two, TwentyTwo))
# print(issubclass(TwoHundredTwentyTwo, Two))


# чтобы проверить, сделан ли объект по определенному классу,
# можно воспользоваться методом isinstance()
TwoSuns = Two()

# print(isinstance(TwoSuns, Two))

# Super
# Представим наследование от какого-нибудь класса
# В классе-потомке задаем init
class ContactData:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class PersonContact(ContactData):
    def __init__(self, name, email):
        ContactData.__init__(self, name, email)

P = PersonContact('fgfgf', 'fgfgf')
# print(P.email)

# Однако если мы захотим добавить еще какие-нибудь свойства родительскому классу, то
# нам придется в init постоянно прописывать новые аргументы
# class ContactData:
#     def __init__(self, name, email, person):
#         self.name = name
#         self.email = email
#         self.person = person
#
# class PersonContact(ContactData):
#     def __init__(self, name, email, person):
#         ContactData.__init__(self, name, email, person)
# P = PersonContact('fgfgf', 'fgfgf', 'fgfgf')
# print(P.email)

# А еще название родительского класса может измениться.
# Или может появиться новое звено наследования


# Если мы хотим потомку дать свойства его суперкласса,
# то мы можем воспользоваться такой записью
# В super можно задавать конкретное значение свойств родителя,
# которое будет характерно для объекта
class ContactData:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class Friend(ContactData):
    def __init__(self, name, email, phone, number_of_friends):
        super().__init__(name, email, phone)
        self.number_of_friends = number_of_friends
# F = Friend('Alex', 'fgfg@gmail.com', 89190976585, 7)



# super() позволяет обратиться к любой сущности суперкласса.
# Например, вызвать метод суперкласса.

class A:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def sum(self):
        return self.a + self.b + self.c

    def Print(self):
        print('Hello')

class B(A):
    def __init__(self, a2, b2, c2, d2):
        super().__init__(a2, b2, c2)
        self.d2 = d2

    def Sum(self):
        return 6

    def CheckSuper(self):
        super().Print()

ObjectB = B(2, 3, 4, 5)
# print(ObjectB.sum())
# print(ObjectB.Sum())
# ObjectB.CheckSuper()

# Задание: класс Transport принимает название и скорость (float)

# Класс Auto наследует от Transport, получает свои собственные
# параметры колеса,
# диаметр руля, модель (str)
# Метод ride выводит название и модель
# Метод get_info выводит технические характеристики автомобиля


# Задание: от класса Transport наследует Airplane.
# его метод принимает массу, позволяет вычислить
# прочность шасси относительно скорости
# по формуле: (скорость * масса) / 250 / 100

#

# Задание: от класса Transport наследует Ship
# его метод принимает массу и вычисляет силу Архимеда.
# Плотность самолета принимаем как плотность железа

# Его метод проверяет, есть ли в названии (которое наследуется от Transport)
# слово 'беда',
# а затем вычисляем, с какой вероятностью от отколотого изначального
# названия останется только
# слово Беда. Этот метод должен принять вероятность откалывания
# от названия буквы.
# Проверьте try except, что это float и что он в диапазоне (0, 1]
# Пример: 'Победа'; 'беда' in 'Победа'
# Как вычислить: вероятность возводите в степень (равна количеству букв не в
# беде), умножаете на (1 минус вероятность откалывания) ** 4
# print(0.5 in range(0, 1, 0.01))


# def Archimed(p, m):
# # F = pgV
#     return p * 9.8 * (m/7.8)
#
# def probVex(name , p):
#     if 'беда' in name:
#         return p**4 * (1-p)**(len(name) - 4)
#     else:
#         return 0




# У одного класса может быть много суперклассов

class Living():
    status = 'living'

class NonLiving():
    status = 'nonliving'

class Virus(Living, NonLiving):
    pass

virus = Virus()
# print(virus.status, virus.status)


# Если два суперкласса имеют одинаковые переменные или методы,
# то при объявлении будет вызываться тот, который был задан
# левее в скобках подкласса

class Class1:
    def m(self):
        print("In Class1")


class Class2(Class1):
    def m(self):
        print("In Class2")


class Class3(Class1):
    def m(self):
        print("In Class3")


class Class4(Class2, Class3):
    pass

obj = Class4()
# obj.m()


# class Class1:
#     def m(self):
#         print("In Class1")
#
#
# class Class2(Class1):
#     pass
#
#
# class Class3(Class1):
#     def m(self):
#         print("In Class3")
#
#
# class Class4(Class2, Class3):
#     pass
#
# obj = Class4()
# obj.m()


class Class1:
    def m(self):
        print("In Class1")


class Class2(Class1):
    def m(self):
        print("In Class2")


class Class3(Class1):
    def m(self):
        print("In Class3")


class Class4(Class2, Class3):
    def m(self):
        print("In Class4")

obj = Class4()
# obj.m()
#
# Class2.m(obj)
# Class3.m(obj)
# Class1.m(obj)


class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    def m(self):
        print("In Class2")
        super().m()

class Class3(Class1):
    def m(self):
        print("In Class3")
        super().m()


class Class4(Class2, Class3):
    def m(self):
        print("In Class4")
        super().m()

# obj = Class4()
# obj.m()


# Задание: класс символизирует смесь самолета и корабля, которые вы написали
# создайте экземпляр этого класса, примените все методы из родительских классов



class Human:
    def __init__(self, NSP, birthday, phone_number, country, address):
        self.NSP = NSP
        self.birthday = birthday
        self.phone_number = phone_number
        self.country = country
        self.address = address

    def show_personal_data(self):
        return str('His name is ' + self.NSP + ', he was born in ' + self.birthday)

Human1 = Human('Petr Yan', '12 June 1978', '89349076709', 'Russia', 'Voronezh')
#print(Human1.show_personal_data())


class Country():
    def __init__(self, capital, square, region_quantity, population):
         self.capital = capital
         self.square = square
         self.region_quantity = region_quantity
         self.population = population

    def __str__(self):
        return f'The capital is {self.capital}'

Russia = Country('Moscow', '1893', 85 ,'148000000')
#print(Russia)

# название объекта = название класса()

#   f'Этот программист работает в {self.sphere}, поэтому его стек {self.technologies}'


class Programmer:
    def __init__(self, lan_number, lan_list, sphere, level):
        self.lan_number = lan_number
        self.lan_list = lan_list
        self.sphere = sphere
        self.level = level

    def __str__(self):
        return f'Этот программист работает в {self.sphere}, поэтому он владеет {", ".join(self.lan_list)}'

Misha = Programmer(3, ['HTML', 'CSS', 'JS'], 'frontend', 'middle')
#print(Misha)



class SumNumbers:
    def __init__(self, number):
        self.number = number

    def sum(self, anotherNumber):
        return self.number + anotherNumber

SumNumbersLessThan10 = SumNumbers(2)


class MultiplyNumbers(SumNumbers):
    def __init__(self, number):
        super(MultiplyNumbers, self).__init__(2)
        self.number = super(MultiplyNumbers, self).sum(2)

    def multiply(self, anotherNumber):
        return self.number * anotherNumber

MultiplyNumbersLessThan10 = MultiplyNumbers(2)
#print(MultiplyNumbersLessThan10.multiply(2))


# __add__ позволяет складывать объекты
# class Weight:
#     def __init__(self, kilos):
#         self.kilos = kilos
#
#     def __add__(self, otherWeight):
#         return Weight(self.kilos + otherWeight.kilos)

# По аналогии __sub__, __mul__, __truediv__

# Задание: Создайте класс Число . Класс число хранит внутри одно значение.
# Используя dunder реализуйте для
# него арифметические операции для работы с числом
# (операции +, -, *, /). Добавьте try except, чтобы убедиться, что входной параметр - int



# Задание: Создайте класс Дробь. Используя перегрузку операторов реализуйте
# для него арифметические операции для работы
# с дробями (операции +, -, *, /). Try except, чтобы убедиться, что входной параметр - float
# Сделать __str__, который выводит само число


# Задание: класс Date, который будет содержать информацию о дате (день, месяц, год).
# С помощью механизма
# перегрузки операторов, определите операцию разности
# двух дат (результат в виде количества дней между датами),
# а также операцию увеличения даты на определенное
# количество дней. Сделать метод класса, который позволяет создать объект из списка трех строк
# (проверить в try except,
# что они все конвертируются в числа и что числа в нужных диапазонах)


# Создать базовый класс Employer (служащий) с функцией Print().
# Она должна выводить информацию о служащем. В случае базового класса это может быть строка
# с надписью This is Employer class.
# Создайте от него три производных класса: President,
# Manager, Worker. Переопределите функцию Print() для
# вывода информации, соответствующей каждому типу
# служащего. Для классов  сделать __str__, который выведет какую-нибудь информацию






# Задание: класс персонаж принимает имя, фамилию, прозвище
# Используя property сделать:
# строку имя-прозвище-фамилия
# строку имя-фамилия
# строку фамилия-имя
# строку имя прозвище
# сделать setterы для них
# добавить классовый метод, который создает объект из строк имя-фамилия, прозвище








