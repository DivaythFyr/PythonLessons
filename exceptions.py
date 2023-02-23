import math

#x = 'trtr'
#y = math.sqrt(x)



# Class                     # Description
# Exception                 A base class for most error types
# AttributeError            Raised by syntax obj.foo, if obj has no member named foo
# EOFError                  Raised if “end of file” reached for console or file input
# IOError                   Raised upon failure of I/O operation (e.g., opening file)
# IndexError                Raised if index to sequence is out of bounds
# KeyError                  Raised if nonexistent key requested for set or dictionary
# KeyboardInterrupt         Raised if user types ctrl-C while program is executing
# NameError                 Raised if nonexistent identifier used
# StopIteration             Raised by next(iterator) if no element;
# TypeError                 Raised when wrong type of parameter is sent to a function
# ValueError                Raised when parameter has invalid value (e.g., sqrt(−5))
# ZeroDivisionError         Raised when any division operator used with 0 as divisor


# Когда мы хотим вызвать ошибку вне блока try/ catch мы пользуемся raise
def sqrt(x):
    if not isinstance(x, (int, float)): # isinstance проверяет, относится ли переменная к определенному типу
        raise TypeError('x must be numeric')
    elif x < 0:
        raise ValueError('x cannot be negative')


# Str = 'aa'
# try:
#    Str = int(Str)
# except ValueError:
#     raise ValueError

#
def protectDividingOnZero(number1, number2):
    if number2 != 0:
        print(number1 / number2)
    else:
        print("You can't divide on zero")

#protectDividingOnZero(1, 0)


def TryDividingOnZero(number1, number2):
    try: # пытаемся выполнить рисковое действие
        print(number1/number2)
    except: # если что-то идет не так, то внутри except прописываем, что будем делать
        print("Это ошибка")
#TryDividingOnZero(1, 0)



# Желательно в раздел exception
# прописывать конкретное на какое исключение как реагировать
def dfdf():
    try:
        print(1 / 0)
        print(b + a)
    except:
        print('ошибка')
#dfdf()

def dfdf1():
    try:
        print(1 / 0)
    except ZeroDivisionError:
        print('ошибка')

    try:
        print(b + a)
    except NameError:
        print('Этих переменных не существует')


    try:
        print(b + a)
        print(1 / 0)
    except NameError:
        print('Этих переменных не существует')
    except ZeroDivisionError:
        print('Нельзя делить на ноль')
#dfdf()





def rtr():
    try:
        print(1 / 0)
        print(b + a)
    except NameError:
        print('Ошибка, что это за переменные?')
    except ZeroDivisionError:
        print('нельзя делить на ноль')
# rtr()



# Если вы хотите обработать несколько исключений
# одним и тем же способом,
# перечислите их так except (исключение1, исключение2)
def dfdff():
    try:
        print(1 / 0)
        print(b + a)
    except (NameError, ZeroDivisionError):
        print('Это деление на ноль или неназванные переменные')
    except IOError:
        print('1+1')
#dfdff()

# assert Выводит True или False в зависимости от истинности выражения
List = [1, 2, 1, 1]
try:
    assert List[0] == 2 # слово для проверки искусственных ошибок
except:
    List[0] = 2
# print(List[0])

# try except имеет свой собственный else
# Выполнится, если except не заметит никакой ошибки
try:
    assert 2 / 3 > 0
except ZeroDivisionError:
    print('Нельзя делить')
else:
    print(2 / 3 + 2)


# Функция проходится по списку и выводит тип отдельных элементов

# Предугадайте все возможные ошибки (в том числе не встроенные в Python)
# и обработайте их try/except
# Внести хотя бы один try/except
# Обработать случай, когда аргумент - не список!
# ['dfdfd', 'fdfdfdfd', ['tytyt', 'poihjhjh']] -> ['dfdfd', 'fdfdfdfd', 'tytyt']
#

def PrintType(List):
    try:
        assert type(List) == list
    except AssertionError:
        raise AssertionError
    else:
        for i, element in enumerate(List):
            print(type(element))
#PrintType(['fgfgf', 'fgfgfgf', {}])


# Задание: функция принимает список чисел и число.
# [3, 4, 5], 60 -> 20  15  12
# Нужно вывести результат деления этого числа на все остальные
# Предугадайте все возможные ошибки и обработайте их try/except
print(ZeroDivisionError, 'будет делиться на ноль')


# Функция принимает список слов и слово, которое нужно удалить
# Предугадайте все возможные ошибки и обработайте их try/except
#  list.remove('Hello')

def RemoveWord(str_list, word):
# Сначала мы предусматриваем ошибку
     try:
         assert word == str
     except AssertionError:
         print('Это не слово')
         raise AssertionError
     str_list.remove(word)
     return str_list




# Задача: функция принимает список чисел и строчек,
# если видит строчку,
# то меняет на число. Затем должна вывестись сумма всех чисел.
# Нужно в функции предугадать возможные ошибки, зависящие
# от входных данных

def PrintSum(int_str_list):
    just_int = []

    try:
        assert len(int_str_list) != 0
    except:
        return 'массив ничего не содержит'

    for i, element in enumerate(int_str_list):
        try: # проверяем являются ли все элементы строками или числами
            assert type(element) == int or type(element) == str
        except:
            int_str_list.remove(element) # удаляем элемент, если не так

    for i, element in enumerate(int_str_list):
        if type(element) == int:
            just_int.append(element)
        elif type(element) == str and element.isdigit():
            just_int.append(int(element))
    return sum(just_int)
#print(PrintSum(['sdsdsds']))

# Задача: функция принимает два списка, в нем только строчки.
# Выводится строка, где берется первый элемент первого списка, затем первый второго
# Затем второй первой первого, второй второго и тд
# Пример: ['Hello', 'are'] ['how', 'you']; 'Hello how are you'


def concatTwoStrLists(list1, list2):
    sentence = ''
    try:
        assert len(list1) == len(list2)
    except:

        List3 = []
        for i in range(abs(len(list1) - len(list2))):
            List3.append('')

        if list1 > list2:
            list2 += List3
        else:
            list1 += List3

    for i, element in enumerate(list1):
        sentence += list1[i] + ' '
        sentence += list2[i] + ' '
    return sentence
#print(concatTwoStrLists(['Hello', 'are'], ['how']))
















