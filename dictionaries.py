# Словарь - структура данных,
# пишется через фигурные скобки {}
# В каждом словаре есть ключ
# и подходящее ему значение
# в качестве ключа может быть целое число
# или строчка
# Пример:
# {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday'}


# {'бегать': ['run', 'jog', 'sprint'],
# 'run': ['бегать', 'запускать']}


# Найти значение можно по ключу.
# В квадратных скобках указываем название ключа.
weekDict = {1: 'Monday', 2: 'Tuesday',
            3: 'Wednesday',
            'The Fourth day': 'Thursday'}
# Если список[число],
# то словарь[ключ]
# print(weekDict['The Fourth day'])
# print(weekDict[3])


# Менять значение можно следующим образом
weekDict[1] = 'Sunday'
# print(weekDict)

# в качестве значения  можно указывать
# любой тип данных,
# даже другие структуры данных: список, словарь, кортеж и тд.
D = {1: [1, 2, 0, 1, 4], 2: {1:2, 2:4, 3:5}}


# Чтобы обратиться к элементу списка
# внутри словаря:
# print(D[1][2])



# Обратиться к значению словаря внутри словаря
#print(D[2][1])


# чтобы вернуть все значения словаря
# / все ключи словаря
# print(D.values())
# print(D.keys())

# метод items() возвращает все ключи и значения.
# Пара ключ-значение оборачивается в кортеж
# print(D.items())


# если мы хотим пройтись циклом по ключам и значениям,
# то нам нужно использовать следующую конструкцию
# for key, value in словарь.items():
# D = {1: [1, 2, 3, 4], 2: {1:2, 2:4, 3:5}, 'fgfgf':"dfgfgfg", 5: 'fgfgfgf', '77': 77}
# for key, value in D.items():
#
# print(D)
# печатем значение словаря, которое находится под ключом


# Как изменить ключ
D = {1: [1, 2, 3, 4], 2: {1:2, 2:4, 3:5}, 'fgfgf':"dfgfgfg", 5: 'fgfgfgf', '77': 77}
D[100] = D.pop(1)



# Задача: Функция принимает словарь,
# ключи и значения которых являются цифрами.
# Каждое значение увеличиваете на единицу
# Например: {1:2, 2:3, 4:5, 6:44} становится
# {1:3, 2:4, 4:5, 6:45}

def DictPlusOne(d):
    for key, value in d.items():
        d[key] += 1
    return d
# print(DictPlusOne({1:2, 2:3, 3:4, 5:78}))


# Задача: на том же самом словаре перемножаете все
# значения словаря между собой
# и печатаете его
def DictMultiplyValues(d):
    y = 1 # сохранит в себе перемножение всех значений словаря
    for key, value in d.items(): # открываем цикл
        y *= value # на каждом обороте берем значение по ключу key и домножаем его в переменную y
    return y # возвращаем значение

#print(DictMultiplyValues
# (DictPlusOne({1:2, 2:3, 3:4, 5:78})))




# Задача: функция принимает словарь,
# где значения - это строки.
# Если строка может стать числом,
# то превращаете ее в число
# строка.isdigit() (проверка на возможность превратиться в число)


def DictConvert(d):
    for key, value in d.items():
        if d[key].isdigit() == True:
            d[key] = int(d[key])
    return d
# print(DictConvert({1:'233', 2:'3erere'}))



# Задача: Функция принимает список
# и словарь
# Находит все числа и там и там
# Сравниваете суммы чисел и там и там
# Пример: [1, 'fdgfgf', True, 2], {1:'dfdfd', 2:10} ->
# -> сумма в словаре больше
# Дополнительно: А еще выводит, где больше других типов данных
# (все не int будут засчитываться)




def CompareListDict(L, D):
    L_count = 0
    D_count = 0

    for i, element in enumerate(L):
        if type(element) == int:
            L_count += 1

    for key, value in D.items():
        if type(value) == int:
            D_count += 1

    L_other = len(L) - L_count
    D_other = len(D) - D_count

    return (max(L_count, D_count), max(L_other, D_other))
#print(CompareListDict(['aa', 2, 3], {1: 2, 2: 'aa', 3: 'aa'}))





# Чтобы сделать словарь из двух списков
# dict(zip(list1, list2))

# list1 = ['Monday', 'Tuesday', 'Wednesday']
# list2 = [1, 2, 3]
# print(dict(zip(list2, list1)))

# Задание: функция принимает два списка,
# выводит словарь
# В первом списке должны быть
# только строки или int

def CreateDictFromLists(list1, list2):
    for i, element in enumerate(list1):
        if type(element) == str or type(element) == int:
            continue
        else:
            return "Can't be used as keys"
    if len(list1) != len(list2):
        return "They are not equal"
    return dict(zip(list1, list2))
#print(CreateDictFromLists([4, 2, 3], [2, 5, 6]))

# for i in range(len(list)): порядковый номер
# for i in list элемент
# for i, element in enumerate(list): создает и порядковый номер и сам элемент
#for i, element in enumerate(['aa', 'bb', 'cc']):
    #print(f'{i}:{element}' )

genetic_code = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}
# Функция принимает строку 'GCACCCAAA'
# Переводим строку ДНК в строку белка
# string[i:i+2]


# GGGCCGATGCGCG




# Функция принимает два словаря,
# сравнивает, где больше всего строк
# {1: 'dfdfd', 2:'dfdfd'}  {1:2}

d1 = {1: 'dfdfd', 2: 2, 3:'dfdfdfd'}
d2 = {1: 'dfdfd', 2:'dfdfdfd', 3:'dfdfdfd'}


def compareDicts(d1, d2):
    count1 = 0
    count2 = 0

    for key, value in d1.items():
        if type(value) == str:
            count1 += 1

    for key, value in d2.items():
        if type(value) == str:
            count2 += 1

    if count1 > count2:
        print('В первом словаре больше')
    elif count1 < count2:
        print('Во втором словаре больше')
    else:
        print('Они одинаковы')
compareDicts({1: 'dfdfd', 2: 2, 3:'dfdfdfd'}, {1: 'dfdfd', 2:'dfdfdfd', 3:'dfdfdfd'})