# Взаимодействие с файлом можно охарактеризовать четырьмя основными операциями
# 1. открыть файл
# 2. чтение из потока - часть файла извлекается и помещается в
# какую-нибудь область памяти (как правило, переменную)
# 3. запись - из области памяти информация записывается в файл
# 4. закрытие файла

# Для открытия потока используются три основных режима:
# 1. режим чтения: разрешает только операции чтения; попытка запи-
# си в поток вызовет исключение (которое называ-
# ется UnsupportedOperation, оно наследует OSError
# и ValueError и является потомком модуля io);
#
# 2. режим записи: поток, открытый в этом режиме, раз-
# решает только операции записи; попытка прочитать
# поток вызовет исключение, упомянутое выше;
#
# 3. режим обновления: поток, открытый в этом режиме,
# разрешает и запись, и чтение.
#
#

# Открытие потока:
# stream = open(file, mode = 'w', encoding = None)
# mode - что именно делать с файлом при открытии.
# Есть несколько параметров mode:
# r: чтение
# w: запись. Файл, в который мы хотим что-то засунуть, не обязан существовать. Если его не было, то он создастся.
# a: дозапись. Добавить информацию в конец файла без удаления предыдущей инфы
# r+: чтение и обновление
# w+: запись и обновление

# если в конце добавить букву t - text mode, если b - binary mode

def ProperFileOpen(filename):
    try:
        stream = open(r"C:\Users\aisin\Desktop\RR.txt", 'rt')
        # здесь происходит обработка
    except FileNotFoundError as exc:
        print("Cannot open the file:", exc)
    except Exception as exc:
        print('Something went wrong', exc)
    else: # этот код выполняется, если ошибок нет
        print(stream.read())
        stream.close()
    finally: # этот код будет выполняться всегда
        print('Executed finally')
#ProperFileOpen()


# выявить количество символов в файле
def PrintNumberOfCharacters():
    try:
        cnt = 0
        s = open(r"C:\Users\aisin\Desktop\file.txt", 'rt')
        content = s.read()
        for characters in content:
                cnt += 1
        s.close()
        print(f'There are {cnt} characters in this' )
    except FileNotFoundError as exc:
        print("Cannot open the file:", exc)
    except Exception as exc:
        print('Something went wrong', exc)
    else:
        new_file = open(r"C:\Users\aisin\Desktop\file.txt", 'at')
        new_file.write(f' (There are {cnt} characters in this file except for this sentence)')
        new_file.close()
#PrintNumberOfCharacters()
#s = open(r"C:\Users\aisin\Desktop\file.txt", 'rt')
#content = s.read()
#print(content)


# если нужно обработать файл как набор строк, а не символов
# то пользуемся readlines()
#s = open(r"C:\Users\aisin\Desktop\file.txt", 'rt')
#print(s.readlines(3))


# с помощью этого модуля можно простым образом выявлять ошибки записи и чтения
from os import strerror

def writeSomething():
    try:
        fo = open(r"C:\Users\aisin\Desktop\file.txt", 'wt')
        for i in range(10):
            s = 'line #' + str(i + 1) + '\n'
            for ch in s: # обращаемся к каждому отдельному элементу строчки
                fo.write(ch) # запись одного символа
        fo.close()
    except IOError as e:
        print('error occured ', + strerror(e.errno))
#writeSomething()
#ProperFileOpen('file.txt')



# Удобная конструкция для записи из одного файла в другой
# # with позволяет автоматически закрывать файл без close()
with open(r'C:\Users\aisin\Desktop\file.txt','rt') as firstfile, open(r'C:\Users\aisin\Desktop\copy_file.txt','wt') as secondfile:
    for line in firstfile:
        for element in line:
                secondfile.write(element)



# Задание:
# Вы создаете файл на рабочем столе, в котором много чисел
# with open(путь к рабочему столу, 'at') as f:
#   for i in range(10):
#       f.write(i)
# with open(r'C:\Users\aisin\Desktop\file.txt','rt') as firstfile, open(r'C:\Users\aisin\Desktop\copy_file.txt','wt') as secondfile:
#     for line in firstfile:
#         for element in line:
#                 secondfile.write(element)

# Задание:
# произвести запись в другой файл, но только семерок
# file.read()
# for symbol in file:
#   текст += symbol


# Задача: функция принимает список строк.
# Нужно произвести запись в файл, чтобы
# Каждая строка была на отдельной линии
# Enter в Python -  r'\n'


# Задача: в текстовом файле рандомные строки.
# Нужно сделать запись в новый файл,
# но порядок строк обратный
# s = pxp.read()
# s = pxp[::-1]


# Задание:
# string -> list .   string.split(' ')
# Из файла  переписать все слова, в которых больше 5 букв

# Задание:
# Добавить в файл * после последней из запятой
# Если запятых нет, то поместить ее в конец


def function6():
    with open('test.txt', 'rt') as file_1, open('test2.txt', 'wt') as file_2:
        str1 = ''
    #   str1 = file_1.read()
        for line in file_1:
            for symbol in line:
                str1 += symbol
        for i in range(len(str1)):
            if str1[i] == ',':
                index = i
        if index != 0:
            file_2.write(f'{str1[0:index+1]}* {str1[index+1:len(str1)]}')
        else:
            file_2.write(f'{str1}*')


# # Дан текстовый файл, содержащий целые числа.
# # Удалить из него все четные числа.





