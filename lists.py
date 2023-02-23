# два способа создать список
rubbish_list = ['apple', 'pen', 'dust', 'flies']
rubbish_list = list(('apple', 'pen', 'dust', 'flies'))

# Чтобы поменять значение в списке
# нужно воспользоваться
# индексом элемента в квадратных скобках

# rubbish_list[0] = 'pear'
# print(rubbish_list)

# Чтобы добавить элемент в список
# нужно воспользоваться методом append
rubbish_list.append('decaying box')
# print(rubbish_list)

# Переставить элементы
rubbish_list[0], rubbish_list[1] = rubbish_list[1], rubbish_list[0]
# print(rubbish_list)

# print(rubbish_list[0:3] + rubbish_list[2:4])


# Задание: список содержит 6 случайных элементов.
# добавить новый элемент, но чтобы он оказался на третьей позиции.



# Чтобы удалить элемент по индексу
# Используя знак минус можно
# обращаться к элементам с конца
# rubbish_list.pop(0)
# print(rubbish_list)

# Чтобы удалить элемент по значению,
# используем remove
# rubbish_list.remove('dust')
# print(rubbish_list)



# Задание: создать список чисел.
# Просуммировать все числа между собой
# Дополнительно: Сложить все нечетные числа
# между собой
# циклом for проходитесь.

# Создаете переменную = 0,
# туда будете складывать числа
# из списка
# for i in range(len(список)):
#    переменная += список[i]

#number_list = [1, 2, 2, 3, 4, 5, 5]
#Sum = 0
#for i in range(len(number_list)): # len(список)
    #if number_list[i] % 2 != 0:
        #Sum += number_list[i]  # обращение к элементу списка
#print(Sum)



# Задание: создать список чисел.
# Просуммировать максимум и минимум
# max(список)  min(список)



#number_list = [1, 2, 3, 4, 5]
#print(max(number_list) + min(number_list))



# Задание: создать список строк и чисел.
# Посчитать количество строк
# Если строк больше, чем чисел, вывести:
# 'Строк больше, чем чисел',
# Если нет, то 'строк меньше', else 'поровну'
# if type(список[i]) == str/int/float/bool:
# проверить тип


# if type(list[i]) ==

#n_str_list = [1, 2, 'hello', 'good morning']
#n_number = 0
#str_number = 0
#for i in range(len(n_str_list)):
    #if type(n_str_list[i]) == str:
        #str_number += 1
    #else:
        #n_number += 1
#if n_number > str_number:
    #print('Чисел больше в списке ')
#elif str_number > n_number:
    #print('Строк больше в списке ')
#else:
    #print('Поровну')



# Задание: сделать список строк.
# Пройтись циклом и удалить дупликаты
# Строчки можно сравнить друг с другом оператором ==
# Создайте пустой список
# # if L[i] not in list:
# 1. Создаете основной список
# 2. Создаете пустой список
# 3. Проходитесь по основному списку,
# если элемента еще нет во
# втором, то удаляете.
# Можно этот же элемент удалить по значению
# в оригинальном списке.

# str_list = ['ss', 'sss', 'ss', 'sssss', 'sss']
# no_duplicates = []
#
# for i in range(len(str_list)):
#     if str_list[i] not in no_duplicates:
#         no_duplicates.append(str_list[i])
# print(no_duplicates)



# Задание: Создать любой список и пустой список
#  Циклом for скопировать все элементы в пустой
#  список (методом append).  список.append(элемент)





# str_list = ['ss', 'sss', 'ss', 'sssss', 'sss']
# List = []
# for i in range(len(str_list)):
#     List.append(str_list[i])
# print(List)


# Задание: Список строк, целых и дробных чисел.
# Если элемент - целое, меняем его на строку.
# Если дробное, меняем его на целое
# Если строка может превратиться в целое,
# меняем на целое
# Если нет, то меняем строку на длину ее символов len()
# Проверяем могут ли строки перейти в числа,
# если могут, то переводим
# if Str.isdigit() == True: проверка можно ли перевести строку
# в целое число int(элемент)

spis=['car','bmw','77','99','21']
for i in range(len(spis)):
    if spis[i].isdigit()==True:
        spis[i]= int(spis[i])
#print(spis)


# в дробное число float(элемент)
List = [1, 2, 'dfdf', 3.6, '5', '1']
for i in range(len(List)):
    if type(List[i]) == int:
        List[i] = str(List[i])
    elif type(List[i]) == float:
        List[i] = int(List[i])
    else:
        if List[i].isdigit() == True: # if string == int(string):
            List[i] = int(List[i])
        else:
            List[i] = len(List[i])
#print(List)




# Чтобы сделать срез списка list[:4],
# при этом последнее число не включается
L = [1, 2, 3, 'aaa', 'aa']
# print(L[1:4])
# print(L[3:])

# Задание: создать два списка.
# У первого списка взять элементы от
# первого до середины
# У второго от середины до конца
# Сложить эти срезы

List1 = [1, 2, 3, 4, 5, 6]
List2 = [1, 2, 3, 4, 6, 7]

mid1 = round(len(List1) / 2)
mid2 = round(len(List2) / 2)
#print(List1[:mid1] + List2[mid2:len(List2)+1])

# Сформировать третий список,
# содержащий элементы общие для двух списков
# L = []    K = []   L + K -> [L, K]



# Сформировать третий список,
# содержащий только уникальные элементы каждого из списков.
# if L2[i] not in L1  - проверяем, есть ли
# элемент в списке один
# L1 = [], L2 = []

# Задание: создаете список, в нем любые элементы
# L2 = L1
# Создать копию списка. В копии списка
# вы меняете любой элемент
# Сделать print первого списка


# Простым копированием списка не создается нового списка
# А уже на существующий ведут две переменные
hogwash_list = ['aaaaa', 'aaaaa', 'aaaaaaaa']
hogwash_list2 = hogwash_list[:]
hogwash_list2[0] = 'aa'
#print(hogwash_list)


