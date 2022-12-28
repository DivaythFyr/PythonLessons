from time import perf_counter, sleep
from threading import Thread
import concurrent.futures
# Синхронное выполнение программы подразумевает
# последовательное выполнение операций.


# Асинхронное – предполагает возможность
# независимого выполнения задач.

# Конкурентность предполагает выполнение нескольких задач
# одним исполнителем

# Параллельность
#  предполагает параллельное выполнение задач
#  разными исполнителями.


# Существует два типа задач: связанные с вводом-выводом (IO-bound)
# или связанные с процессором (CPU-bound)


# Процессы, связанные с вводом/выводом,
# тратят больше времени на ввод/вывод, чем на
# вычисления. Примеры: сетевые запросы, соединения
# с базами данных, ввод/вывод файлов.


# Процессы, привязанные к процессору, тратят больше времени
# на вычисления, чем на запросы ввода-вывода.
# Примеры: умножение матриц, поиск простых чисел, сжатие
# видео, потоковое видео.
# from time import sleep, perf_counter
# start_time = perf_counter()
# def task():
#     print('Задача начинает выполняться')
#     sleep(1)
#     print('Выполнено')

# task()
# task()
# task()

# end_time = perf_counter()
# print(f'Выполнение заняло {end_time - start_time: 0.2f} секунд')


# Поток - класс
# Многопоточность
# Для создания потока нужно импортировать из встроенного модуля
# threading класс Thread и инициализировать экземпляр потока
# target - функция для выполнения в новом потоке
# args - аргументы функции. Представляет собой кортеж

# new_thread = Thread(target=<fn>, args=<args_tuple>) инициализируем объект потока
# new_thread.start() Запуск потока.
# new_thread.join() если хотим дождаться завершения потока в главном потоке.
#
# from threading import Thread
# from time import sleep, perf_counter
#
# def task():
#     print('Задача начинает выполняться')
#     sleep(1)
#     print('Выполнено')
#
# start_time = perf_counter()
#
# ## создаем потоки
# t1 = Thread(target=task)
# t2 = Thread(target=task)
# t3 = Thread(target=task)
#
# # запускаем потоки
# t1.start()
# t2.start()
# t3.start()

# ждем, когда потоки выполнятся с помощью join(), чтобы можно было посмотреть время работы
# t1.join()
# t2.join()
# t3.join()
#
# end_time = perf_counter()
# print(f'Выполнение заняло {end_time - start_time: 0.2f} секунд')


# Передача аргументов в потоки
#
# def task(id):
#     print(f'Задача {id} начинает выполняться')
#     sleep(1)
#     print(f' {id} Выполнено ')
#
# start_time = perf_counter()
#
# threads = []
# for n in range(1,11):
#     t = Thread(target=task, args=(n,)) # Подаем n как аргумент, так как у task есть этот аргумент
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()
#
# end_time = perf_counter()
#
# print(f'Выполнение заняло {end_time - start_time: 0.2f} секунд')

# Задание: Преобразовать код так, чтобы вместо аргумента id
# Был аргумент sleep_seconds, который указывает,
# сколько времени будет спать вызов функции


# Аргументы класса Thread модуля threading (threading.Thread)
# Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
#  group. Имеет значение None, зарезервирована для будущего расширения
# при реализации класса ThreadGroup.
#  target. Это функция, которая выполняется в потоке с помощью метода
# run(), если передано значение None, ничего не вызывается.
#  name. Это имя потока, по умолчанию оно принимает значение «Thread-
# X», где X – десятичное число. Программист может задать имя вручную.
#  args. Это кортеж, в котором хранятся аргументы, передаваемые в
# вызываемую функцию.
#  kwargs. Это словарь, в котором хранятся аргументы, передаваемые в
# функцию.
#  daemon. Это параметр, который устанавливает, является ли поток
# демоническим. По умолчанию имеет значение None, тогда свойство
# daemonic наследуется от текущего потока. Программист может
# самостоятельно установить значение параметра.


# Примеры однопоточной и многопоточной реализации
# Код заменяет внутри файлов подстроки

# Однопоточная реализация
# from time import perf_counter
#
# def replace(filename, substr, new_substr):
#     print(f'Processing a file {filename}')
#
#     with open(filename, 'r') as f:
#         content = f.read()
#     # replace a string by a new substring
#     content = content.replace(substr, new_substr)
#
# #     write to a file
#     with open(filename, 'w') as f:
#         f.write(content)
#
# def main():
#     filenames = [
#         r"C:\Users\aisin\Desktop\test1.txt",
#         r"C:\Users\aisin\Desktop\test2.txt",
#         r"C:\Users\aisin\Desktop\test3.txt",
#         r"C:\Users\aisin\Desktop\test4.txt",
#         r"C:\Users\aisin\Desktop\test5.txt",
#         r"C:\Users\aisin\Desktop\test6.txt"
#     ]
#
#     for filename in filenames:
#         replace(filename, 'ids', 'id')
#
# start_time = perf_counter()
#
# main()
#
# end_time = perf_counter()


# Многопоточная реализация
# from time import perf_counter
#
# def replace(filename, substr, new_substr):
#     print(f'Processing a file {filename}')
#
#     with open(filename, 'r') as f:
#         content = f.read()
#     # replace a string by a new substring
#     content = content.replace(substr, new_substr)
#
# #     write to a file
#     with open(filename, 'w') as f:
#         f.write(content)
#
# def main():
#     filenames = [
#         r"C:\Users\aisin\Desktop\test1.txt",
#         r"C:\Users\aisin\Desktop\test2.txt",
#         r"C:\Users\aisin\Desktop\test3.txt",
#         r"C:\Users\aisin\Desktop\test4.txt",
#         r"C:\Users\aisin\Desktop\test5.txt",
#         r"C:\Users\aisin\Desktop\test6.txt"
#     ]
#
#
#     # create threads
#     threads = [Thread(target=replace, args=(filename, 'id', 'ids')) for filename in filenames]
#
# #     start threads
#     for thread in threads:
#         thread.start()
#
# # await the finish
#     for thread in threads:
#         thread.join()
#
# start_time = perf_counter()
#
# main()
#
# end_time = perf_counter()




# Задание: Преобразовать вышележащий код так, чтобы filenames
# был генератором списка

# Задание: Функция инициализирует список из 10
# потоков. Пусть значения индекса i-го потока передаётся в качестве
# аргумента в функцию, которая выводит сведения о запуске
# соответствующего потока


# Задание: Создайте три экземпляра потока.
#  Каждый из них принимает какую-нибудь функцию (какую угодно)
# Оценить время работы вызовов трех потоков




# Задание:  Два потока параллельно выводят каждый в свой файл заданное
# число строк. Напишите функцию, выполняющая соответствующие
# действия. Аргументами целевой функции будут число строк и имя
# текстового файла для записи. Определите время, затраченное на
# выполнение данных потоков.

# def function(file, string):
#     with open(fr"C:\Users\Виталий\Desktop\Study\Lessons_Python\Lessons 24.12.22 - 25.12.22\{file}", "wt") as file1:
#         for i in range(string):
#             file1.write("Hello World""\n")
#
#
# start_time = perf_counter()
# t1 = Thread(target=function, args=("file1.txt", 10,))
# t2 = Thread(target=function, args=("file2.txt", 20,))
#
# t1.start()
# t2.start()
#
# t1.join()
# t1.join()
#
# end_time = perf_counter()
# print(f'{end_time - start_time} секунд')







# Пусть имеется два текстовых файла(«text1.txt» и «text2.txt»).
# Создайте три потока таким образом, чтобы:
#  Первый поток записывал текст в файл «text1.txt».
#  Второй поток записывал текст в «text2.txt».
#  Третий поток пытался считывать эти «txt» файлы.


# Задание:  подкласс MyThreadClass, который наследуется из самого
# класса Thread.
#  Определите конструктор __init__
# инициализирующий два параметра: name - название потока и
# duration - продолжительность выполнения потока, которые будут
# использованы в методе run. Значение параметра duration
# вычисляется на основании функции randint, которая выводит
# некое случайное целое от 1 до 10. Метод run выводит сведения о
# потоке: название потока и текущий идентификатор процесса с
# помощью функции os.getpid(). Создайте десять экземпляров класса
# MyThreadClass – потоков. Определите время, затраченное на
# выполнение этих потоков.





# deamon-threads - потоки-демоны
# это режим, при котором задача выполняется в фоновом режиме

# Пример недемонического потока
from threading import Thread
from time import sleep

# def func():
#     for i in range(5):
#         print(f'thread number {i}')
#         sleep(0.5)
# th = Thread(target=func())
# th.start()
# print('App stop')


# def func():
#     for i in range(5):
#         print(f'thread number {i}')
#         sleep(0.5)
# th = Thread(target=func(), daemon=True)
# th.start()
# print('App stop')

# Поток-демон — это поток, который выполняет задачи в фоновом режиме.
#  Потоки-демоны полезны для выполнения задач, которые не являются критическими.
#  Программа не ждет завершения работы потока-демона перед завершением.
#  При завершении программы поток-демон автоматически завершается.

# Встроенный модуль queue позволяет безопасно обмениваться данными между
# несколькими потоками. Класс Queue из модуля queue реализует всю необходимую
# семантику блокировки.
from queue import Queue
# queue = Queue()

# Чтобы создать очередь с ограничением по размеру,
# можно использовать параметр maxsize
queue = Queue(maxsize=10)

# Чтобы добавить элемент в очередь
# queue.put(item=)

# Чтобы получить элемент из очереди
# item = queue.get()

# Чтобы посмотреть количество элементов
size = queue.qsize()

# Элемент, который вы добавляете в очередь, представляет собой единицу работы или
# задачу.
# Когда поток вызывает метод get() для получения элемента из очереди, ему может
# потребоваться обработать его, прежде чем задача будет считаться выполненной.
# После завершения поток может вызвать метод task_done(), чтобы указать, что он
# полностью обработал задачу
# item = queue.get()
# queue.task_done()

# Чтобы дождаться завершения всех задач в очереди, можно вызвать метод join() на
# объекте очереди
# queue.join()

# Пример потокобезопасной очереди
# import time
# from queue import Empty, Queue
# from threading import Thread
#
# def producer(queue):
#     for i in range(1, 6):
#         print(f'Add element {i} to queue')
#         time.sleep(1)
#         queue.put(i)
#
# def consumer(queue):
#     while True:
#         try:
#             item = queue.get()
#         except Empty:
#             continue
#         else:
#             print(f'Process element {item}')
#             time.sleep(2)
#             queue.task_done()
#
# queue = Queue()
#
# # Create thread-producer (поток производитель) and run it
# producer_thread = Thread(target=producer, args=(queue,))
# producer_thread.start()
#
# # Create thread_consumer and run it
# consumer_thread = Thread(target=consumer, args=(queue, ), daemon=True)
# consumer_thread.start()
#
# # Wait when all tasks will be appended to the queue
# producer_thread.join()
#
# # Wait when all tasks in the queue will be ended
# queue.join()


# Класс Thread полезен, когда вы хотите создавать потоки вручную.
# Однако ручное
# управление потоками неэффективно,
# поскольку частое создание и уничтожение
# множества потоков требует больших вычислительных затрат


# Пул потоков (Thread Pool) —
# это шаблон для автоматического эффективного
# управления потоками в программе.


# Для создания пулов потоков используется класс ThreadPoolExecutor из модуля
# concurrent.futures.

# У класса Executor есть три метода для управления пулом потоков:
#  submit() — отправляет функцию на выполнение и возвращает объект Future.
# Метод submit() принимает функцию и выполняет ее асинхронно.
#  map() — асинхронно выполняет функции для каждого элемента итерабельной
# таблицы.
#  shutdown() — завершает работу исполнителя.


# Объект Future
# Future — это объект, который представляет собой конечный результат
# асинхронной операции. У класса Future есть два полезных метода:
# result() — возвращает результат асинхронной операции.
# exception() — возвращает исключение асинхронной операции
# в случае возникновения исключения.

# from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor
#
# def task(id):
#     print(f'Start task {id}')
#     sleep(1)
#     return f'Task {id} is completed'
#
# start = perf_counter()
#
# with ThreadPoolExecutor() as executor:
#     f1 = executor.submit(task, 1)
#     f2 = executor.submit(task, 2)
#
#     print(f1.result())
#     print(f2.result())
#
# finish = perf_counter()
#
# print(f'Execution took {finish - start} seconds')


# Используя list_comprehension. И цикл for для вывода.
# with ThreadPoolExecutor() as executor:
#     results = [executor.submit(task, 1) for i in range(1, 11)]
#
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())








































