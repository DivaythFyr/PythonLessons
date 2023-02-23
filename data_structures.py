# Linked Lists (связанные списки)
# - это упорядоченный набор элементов,
# в котором индексы элементов хранятся в самом же списке

# Каждый элемент называется узлом node, хранит два поля:
# 1. Элемент 2. Ссылка на следующий элемент

# Итерация всегда идет с самого первого элемента.
# У последнего элемента референс - none

class node:
    def __init__(self,data=None): # data - значение узла
        self.data=data
        self.next=None # здесь хранится референс на следующий

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node


# Показывает элементы связанного списка в виде обычного списка
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)


# Возвращает длину связанного списка
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

# Возвращает значение по индексу
    def get(self, index):
        if index >= self.length() or index < 0:
            print('Индекс вне диапазона')
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node=cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx+=1

# L = linked_list() # Создание связанного списка
#
# L.append(1)
# L.append(2)
# L.append(3)
# # L.display()

# Задание: Функция принимает количество элементов в связанном списке.
# Создает связанный список с этим количеством элементов
# Значения элементов запрашиваем с помощью input и используем append

from classes import node, linked_list
def Fun_Link(Num):
    List = linked_list()
    for i in range(Num):
        List.append(int(input('Введите число: ')))
    List.display()
    return List
# Fun_Link(6)




# Задание: функция делает тоже самое, но циклом while,
# не принимает никаких аргументов
# На каждом обороте запрашивается input(' Добавить еще элемент? да/нет: ')
# Если да, то запрашиваем значение инпутом и добавляем в список.
# Если нет, то печатаем используя метод display и break



def funcLinkedList2():
    L = linked_list()
    while True:
        vvod = int(input('Добавить в число список?: да/нет? '))
        if vvod == 'yes':
            L.append(int(input('введите значение: ')))
        else:
            L.display()
            break
# print(funcLinkedList2())






# Стэк - коллекция объектов, в которую элементы поступают
# и выходят по принципу last-in first-out


class LinkedStack:
    class _Node:
        __slots__ = '_element', '_next' # Этот dunder метод
        # не позволит создать объекту
    # новые переменные помимо этих
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head) # Создать узел и сделать на него ссылку
        self._size += 1 # Увеличиваем переменную размера списка на один

    def pop(self): # Перезаписываем первый элемент на следующий, тем самым удаляя его из очереди
        answer = self._head._element # self._head - объект, поэтому у него можно посмотреть значение переменной элемента
        self._head = self._head._next
        self._size -= 1
        return answer



S = LinkedStack()
S.push(2)
S.push(3)
S.push(5)
# print(len(S))
# print(S.pop())

# Задание: добавить try/except в pop.
# Вывести, что стэк пуст, если он пуст,
# в противном случае pop выполняется

# Задание: функция принимает список и добавляет его элементы в стек


# Задание: Функция принимает два стека.
# Перекладывает элементы одного стека в другой

# s1 = LinkedStack()
# s2 = LinkedStack()
# def pushSteck(s1, s2):
#     list = []
#     while True:
#         if not s1.is_empty():
#             answer = s1.pop()
#             list.append(answer)
#         else:
#             break
#     for i in range(len(list)):
#         s2.push(list[i])
#     return s2
# print(pushSteck())
# S1 = LinkedStack()
# S2 = LinkedStack()
# S1.push(1)
# S1.push(3)
# S1.push(5)
#
# def FromS1toS2(s1, s2):
#     while True:
#         if not s1.is_empty():
#             s2.push(s1.pop())
#             print(s1.pop())
#         else:
#             break
#     return s2
# FromS1toS2(S1, S2)


# S1 = LinkedStack()
# S2 = LinkedStack()
# def PushStack1(S1,S2):
#     while True:
#         if not S1.is_empty():
#             S2.push(S1.pop)
#             print(S1.pop())
#         else:
#             break
#     return S2
# S1.push(1)
# S1.push(3)
# S1.push(5)
# PushStack1(S1,S2)




# Очередь - первый заходишь - первый выходишь.
class LinkedQueue:

    class _Node:
        __slots__ = '_element', '_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self): # Посмотреть первый элемент
        return self._head._element

    def dequeue(self):
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e): # Добавить элемент в конец очереди
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

# LQ = LinkedQueue()
# LQ.enqueue(1)
# LQ.enqueue(2)
# LQ.enqueue(3)
# LQ.enqueue(4)
# print(LQ.first())


class PriorityQueue:
    def __init__(self):
        self.queue = []

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def delete(self):
        try:
            max_val = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max_val]:
                    max_val = i
            item = self.queue[max_val]
            del self.queue[max_val]
            return item
        except IndexError:
            print()
            exit()


# if __name__ == '__main__':
#     myQueue = PriorityQueue()
#     myQueue.insert(12)
#     myQueue.insert(1)
#     myQueue.insert(14)
#     myQueue.insert(7)
#     print(myQueue)
#     while not myQueue.isEmpty():
#         print(myQueue.delete())



# Задание: Создайте класс очереди с приоритетами для работы
# с символьными значениями. Для этого добавляйте кортеж (int, ''),
# Где первым значением является приоритет, вторым значением является строка
# Требуется создать реализации для операций над элементами очереди:
# ■ IsEmpty — проверка очереди на пустоту.
# ■ IsFull — проверка очереди на заполнение
# ■ InsertWithPriority — добавление элемента c приоритетом в очередь.
# ■ PullHighestPriorityElement — удаление элемента с самым высоким приоритетом из очереди.
# ■ Peek — возврат самого большого по приоритету элемента. Обращаем ваше внимание, что элемент не
# удаляется из очереди.
# ■ Show — отображение всех элементов очереди на экран.
# При показе элемента также необходимо отображать
# приоритет.



# Задание: Необходимо разработать приложение, которое позволит сохранять информацию о логинах пользователей и их
# паролях. Каждому пользователю соответствует пара логин — пароль. Реализовать функции
# ■ Добавить нового пользователя
# ■ Удалить существующего пользователя
# ■ Проверить существует ли пользователь
# ■ Изменить логин существующего пользователя
# ■ Изменить пароль существующего пользователя











