# Символ ''' позволяет писать многострочные строки
password = '''1234
1234'''
#print(password, end=' ')



# строки можно складывать и умножать
hello = 'hello'
world = 'world'
# print(hello + ' ' + world)
#
#print(5 * hello)


S = 'Utopia'
# Мы можем обращаться к элементам строки как к элементам списка
# for i in range(len(S)):
#     print(S[i]) # если не указать end,
# то print будет печатать на новой строчке,
# а с end через символ, который мы указали


# Чтобы посчитать количество символа в строке
# Метод str.count('строка которую вы хотите найти')

# Задание: пользователь вводит букву
# Пользователь вводит строку
# Вывести сколько раз она встречается в строке
# string = 'fgfgfgf'  letter = 'f', -> 4
# элемент == 'f'

# inp = input()
# string = 'dfdf aa fgfgf aa fdgfdgf a aa'
# count = 0
# for i in range(len(string)):
#     if string[i] == inp:
#         count += 1
# print(count)


# Элементы строки можем записывать в новую строку
# Но мы не можем изменять элемент уже существующей строки
# S = 'ssss'
# S[0] = 'u' # Нельзя
# print('u' + S[1:])



# Задание: создаете любую строчку.
# В цикле проверяете: если порядковый
# номер символа четный, то
# символ умножаете на два,
# если нечетный, то умножаете на три.
# Печатать новую строчку.
# abab -> aabbbaabbb   0 - четное число, 1 - нечетное
# Строки нельзя менять, но можно брать ее часть и складывать в
# новую строку. Например: string3 += string1[i] * 2

#strinG = 'dfdfdfdfdfd'
#strinG += 'F' добавление символа в конец строки

# if i % 2 == 0 Проверка на четность
# empty_string += string[i] * 2
string = 'Follow me, brothers!'
increased_str = ''
for i in range(len(string)):
    if i % 2 == 0:
        increased_str += string[i] * 2
    else:
        increased_str += string[i] * 3
#print(increased_str)


# string = 'dfdfd'
# new_string = ''
# for i in range(len(string)):
#     if i % 2 == 0:
#         new_string += string * 2
#




# срезы можете делать также, как и со списками
# print('increased_str'[:5])


# Чтобы посмотреть, есть ли какой-либо элемент
# в строке,
# можно воспользоваться операторами in и not in
# print('1' in 'string')




# Задача: если в строке буквы не английского алфавита,
# то не печатать их
# in и not in. many_lang[i] in aphabet.
# in Проверяет есть ли текст в другой строке
alphabet = 'abcdefghijklmnopqrstuvwxyz, '
many_lang = 'hello, я из russia' # -> 'hello, russia'
only_en = ''

for i in range(len(many_lang)):
    if many_lang[i] in alphabet:
        only_en += many_lang[i]
#print(only_en)



# строку можно удалить целиком,
# но нельзя удалять элемент строки
#S = 'dfdfdfd'
#del S[0]
# к строке нельзя применить методы append() и insert()
#password.append('5')



# Чтобы удалить элемент строки из какой-то
# конкретной позиции:
string = 'abcdefgggg'
position = 5
#print(string[:position] + string[(position + 1):]) #удалить на конкретной позиции
# print(string.replace('ggg', '')) # удалить какой-то конкретный элемент.
# a = "hello"
# a = list(a)
# del a[0]
# print("".join(a))

# Задача: имеется список чисел и строк, например:
# [1, 3, '4', 6, 'cloud', 5, 'throne', 'fgfgf'].
# Если элемент в списке - число,
# то сделать из него строку,
# если элемент - строка, то сделать число.
# Если строка не сможет превратиться в число,
# то к строке прибавьте строку '1'
# Чтобы проверить, может ли строчка превратиться в число,
# воспользуйтесь встроенным методом isnumeric()
# Например, string = '4',  string.isnumeric() будет выводить True
# '4'.isdigit()
# list[8] = int(list[8])


# all = [1, 5, 'ddr', 'gddr', '6']
# for i in range(len(all)):
#     if type(all[i]) == int:
#         all[i] = str(all[i])
#     elif type(all[i]) == str:
#         if all[i].isnumeric() == True:
#             all[i] = int(all[i])
#         else:
#             all[i] += '1'
# print(all)




# Для данного списка программа выведет
# ['1', '3', 4, '6', 'cloud1', '5', 'throne1', 'fgfgf1']
str_int_list = [1, 3, '4', 6, 'cloud', 5, 'throne', 'fgfgf']
for i in range(len(str_int_list)):
    if type(str_int_list[i]) == int:
        str_int_list[i] = str(str_int_list[i])
    elif str_int_list[i].isnumeric() == False:
        str_int_list[i] += '1'
    else:
        str_int_list[i] = int(str_int_list[i])
#print(str_int_list)

# Вот таким срезом можно вернуть строку наоборот string[::-1]
# Задание: создать список строк. Проходитесь циклом
# по нему и печатаете все палиндромы (может читаться в обе стороны)
DNA_list = ['aaccaa', 'atta', 'ggccaaaaaaa']
for i in range(len(DNA_list)):
    if DNA_list[i] == DNA_list[i][::-1]:
        #print(DNA_list[i])
        pass



# Строки можно превратить в списки,
# Если использовать метод split
# print('This is Sparta'.split())

# Список можно соединить обратно в строку
# print(' '.join(['This', 'is', 'Sparta']))




# Задание: пользователь вводит инпутом cтроку,
# слово которое нужно добавить,
# слово, которое нужно заменить
# Сделать новую строку с заменой
# 'dfdfdfdfd fdfd dfdfdfd' - текст
# 'Hello' - что нужно добавить
# 'fdfd' - вместо чего
# str.replace(строка которую хотите заменить, строка которая заменит)

#user_str = input('Введите строку: ')
#user_add = input('Введите слово, которое нужно добавить: ')
#user_replace = input('Введите слово для замены: ')
#arr_str = user_str.split(' ')
#for i in range(len(arr_str)):
    #if user_replace not in arr_str:
        #print('В втроке нет такого слова')
        #break
    #else:
        #if arr_str[i] == user_replace:
            #arr_str[i] = user_add
#print(' '.join(arr_str))


# Чтобы проверить количество определенного элемента в строке,
# Можно использовать метод count
# print('AVFDFDFFD'.count('FF'))
# Задание: пользователь вводит букву и число. Подсчитать
# сколько раз в тексте встречается две этих буквы подряд
# a   2     ->  aa

# user_lett = input()
# user_num = input()
# user_text = input()
# mult_lett = user_lett*int(user_num)
# print(user_text.count(mult_lett))

STR = '12345678'
STR = STR[:3] + STR[4:]
print(STR)




# Чтобы в тексте заглавная буква была большой,
# Можно использовать метод capitalize

# Задание: Найти текст. Изменить его так, чтобы
# Все предложения начинались с заглавной буквы.
# Подсчитать сколько раз встречается  число
# Подсчитать сколько раз встречается пунктуация
# Подсчитать сколько раз встречаются восклицательные и вопросительные знаки


# Задание: есть предложение, в нем есть русские и английские слова
# Если слово английское, то заменить его на 'какое-то слово'


# Задание: Дается список списков, в каждом из подсписков есть строчки.
# Найти самое большое слово в каждом
# Из списков и вывести строку из этих слов (с пробелами).
