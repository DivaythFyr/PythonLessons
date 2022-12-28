# Рекурсия - это метод решения задач, при котором
# функция вызывает саму себя в процессе исполнения
# Чаще всего это реализуется следующим образом:
# В if прописывается условие, которое затрагивает
# последнее из возможных для решения задач состояний
# в else возвращается вызов функции с видоизмененным аргументом
# (например, меньше на один, чем предыдущий)
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
#print(factorial(3))


# Задача: написать функцию,
# которая суммирует все числа в списке
def list_sum(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:])
#print(list_sum([4, 44, 3]))


# Задача: функция принимает позицию числа
# и возвращает число из последовательности Фибоначчи
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
def Fib(num):
    if num == 1 or num == 2:
        return 1
    else:
        return (Fib(num - 1) + (Fib(num - 2)))
print(Fib(6))
#   Fib(num - 2)  +  Fib(num - 1) = 8


# Задача: функция принимает число и возвращает
# сумму всех ЦИФР внутри него
# Чтобы обратиться к числу более высокого порядка
# (например, к 2 в 24, воспользуйтесь n // 10
# Чтобы обратиться к числу более низкого порядка
# (например, к 4 в 24), воспользуйтесь n % 10
# 111 -> 3 , 24 -> 6, 90 -> 9
def sumDigits(n):
    if n == 0:
        return n
    else:
        return n % 10 + sumDigits(n // 10)
#print(sumDigits(1111))


# Задача: функция принимает число,
# и возвращает сумму n + (n-2) + (n-4)
# пока n - x >= 0
# Например recNsub2sum(4) -> 6, recNsub2sum(6) -> 12
# 4 -> 4 + 2 + 0
# 5 -> 5 + 3 + 1
def recNsub2sum(n):
    if n == 0 or n == 1:
        return n
    else:
        return n + recNsub2sum(n - 2)
#print(recNsub2sum(4))

# Задание: Функция принимает список,
# первый индекс и последний.
# Вывести рекурсией список наоборот
# За основу взять перестановку элементов: a, b = b, a
# В качестве контрольного условия: start < stop - 1
def reverseList(List, start = 0, stop = 2):
    if start < stop -1:
        List[start], List[stop] = List[stop], List[start]
        reverseList(List, start + 1, stop - 1)
    return List
#print(reverseList([2, 4, 3, 6, 7, 8, 23], 0, 6))


# Задача: функция принимает список чисел,
# внутри может быть еще список чисел (внутри
# всех вложенных списков могут быть еще списки)
# Добавить цикл из задачи с суммой чисел
# в списке, чтобы проверять:
# если это список чисел, то используем
# рекурсию по отношению к нему
# если это число, то просто суммируем
# с переменной, которая в начале работы функции равна нулю
def recursive_list_sum(data_list):
	total = 0
	for i, element in enumerate(data_list):
		if type(element) == list:
			total += recursive_list_sum(element)
		else:
			total += element
	return total
#print(recursive_list_sum([3, 3, [2, 2]]))

# for key, value in названиеСловаря.items():
#  названиеСловаря[key], value

def recursive_dict_sum(data_dict):
    total = 0
    for key, value in data_dict.items():
        if type(data_dict[key]) == dict:
            total += recursive_dict_sum(data_dict[key])
        else:
            total += value
    return total
#print(recursive_dict_sum({1:3, 2:{1:2, 2:4}}))


# Задача: функция принимает число и степень, в которую возведется.
# Вывести результат возведения в степень
def findPower(n, p):
    if p == 0:
        return 1
    elif p == 1:
        return n
    else:
        return n * findPower(n, p - 1)
#print(findPower(3, 3))


# Задача: функция принимает два числа: количество элементов, сколько в паре должно быть элементов;
# и считает все возможные комбинации по формуле n! / r!
# Например: n = 4, r = 2 -> 6




def multSTRbyValue(strDict):
    positionOfDict = 0
    finalList = []

    # find a dictionary
    for i, element in enumerate(strDict):
        if type(element) is dict:
            positionOfDict = i
            break

    # find compatible keys and strings
    for key, value in strDict[positionOfDict].items():
        for i, element in enumerate(strDict):
            if type(element) is str and key == i:
                finalList.append(element * value)
                break

    # find another lists to make the recursion
    for i, element in enumerate(strDict):
        if type(element) == list:
             finalList.append(multSTRbyValue(element))

    return finalList
#print(multSTRbyValue(['a', 'b', 'c', {0:2, 1:3, 2:2}, ['a', 'b', 'c', {0:1, 2:1, 3:2}]]))
